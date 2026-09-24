import calendar as cal
import ipywidgets as widgets
from IPython.display import display, clear_output,Javascript
from tabulate import *
import matplotlib.pyplot as plt
selected_date=None
output=widgets.Output()
result_output=widgets.Output()

Total_money_month=float(input("Enter your total money for the month: "))
list_of_expenses_daily = []
list_of_savings = []
list_of_cartegories_daily = []
list_of_Paymentmethods_daily = []
list_of_Notes_daily = []
list_of_dates_daily = []

list_of_expenses_daily_month = []


def process_selected_date(date):
    pass


def select_date(date):
    global selected_date
    selected_date = date
    with output:
        output.clear_output()
        print(f"Selected date: {selected_date}")
    process_selected_date(selected_date)


def create_calendar():
    global year
    year= int(input("Enter year (e.g., 2026): "))
    global month
    month = int(input("Enter month (1-12): "))
    print(f"Calendar for {month}/{year}:\n")

    month_calendar = cal.monthcalendar(year, month)
    headers = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    header_buttons = [
        widgets.Button(
            description=day,
            disabled=True,
            layout=widgets.Layout(width='60px', height='35px', margin='2px')
        )
        for day in headers
    ]

    buttons = []
    for week in month_calendar:
        for day in week:
            if day == 0:
                btn = widgets.Button(
                    description='',
                    disabled=True,
                    layout=widgets.Layout(width='60px', height='40px', margin='2px')
                )
            else:
                btn = widgets.Button(
                    description=str(day),
                    layout=widgets.Layout(width='60px', height='40px', margin='2px')
                )
                btn.style.button_color = "#84cb91"
                btn.on_click(
                    lambda b, d=day: 
                    select_date(f"{year}-{month:02d}-{d:02d}")
                )
            buttons.append(btn)

    calendar_grid = widgets.GridBox(
        children=header_buttons + buttons,
        layout=widgets.Layout(
            grid_template_columns='repeat(7, 60px)',
            grid_gap='4px',
            align_items='stretch'
        )
    )
    display(calendar_grid,output)

def expense_tracker():
    global selected_date
    if selected_date is None:
        print("Please select a date from the calendar first.")
        return

    with output:
        output.clear_output()
        print("EXPENSE TRACKER")
        print("Enter your expense details below:")
        list_of_dates_daily.append(selected_date)
        global amount
        amount=widgets.FloatText(description="Amount:") 
        global category
        category=widgets.Dropdown(description="Category:", options=["Food", "Transportation", "Entertainment", "Utilities","Necessities","Other"])
        global payment_method
        payment_method=widgets.Dropdown(description="Payment Method:", options=["Cash", "Credit Card", "Debit Card", "Bank Transfer","UPI","Other"])
        global notes                    
        notes=widgets.Text(description="Notes:")
        display(amount, category, payment_method, notes)

    print_expenses()

def print_expenses():
    with result_output:
        clear_output(wait=True)
        
        if not list_of_expenses_daily:
            print("No expenses recorded.")
            return
        table_data = []
        running_total = 0
        remaining_budget = 0
        for i in range(len(list_of_expenses_daily)):
            running_total += list_of_expenses_daily[i]
            remaining_budget = Total_money_month - running_total
            table_data.append([
                list_of_dates_daily[i],
                list_of_expenses_daily[i],
                list_of_cartegories_daily[i],
                list_of_Paymentmethods_daily[i],
                list_of_Notes_daily[i],
                running_total,
                remaining_budget
            ])
        headers=["Date","Amount", "Category", "Payment Method", "Notes", "Running Total", "Remaining Budget"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

        if running_total > 0.03*Total_money_month:
            print("Warning: You have spent more than 3 percent of your monthly budget for a day!")

add_expense_button = widgets.Button(description="Add Expense", button_style='success')
def add_expense_clicked(b):
    with output:
        output.clear_output()
        print("Button clicked!")
        print("Selected date:", selected_date)
    expense_tracker()
    
add_expense_button.on_click(add_expense_clicked)
Save_button = widgets.Button(description="Save Expense", button_style='info')
def save_expense_clicked(b):
    if selected_date is None:
        with output:
            output.clear_output()
            print("Please select a date from the calendar first.")
        return
    with output:    
        output.clear_output()
        print("Expense saved successfully!")
        print("Selected date:", selected_date)
        list_of_expenses_daily.append(amount.value)
        list_of_cartegories_daily.append(category.value)
        list_of_Paymentmethods_daily.append(payment_method.value)
        list_of_Notes_daily.append(notes.value)

    print_expenses()


remaining_budget = Total_money_month
def dashboard():
    global remaining_budget
    remaining_budget = remaining_budget - sum(list_of_expenses_daily)
    with output:
        output.clear_output()
        
        print("DASHBOARD")
        print("Total Money for the daily:", ((3*Total_money_month)/100))
        print("Total Expenses Recorded:", sum(list_of_expenses_daily))
        print("Remaining Budget:", remaining_budget)
        print("Number of Expenses Recorded:", len(list_of_expenses_daily))
        if sum(list_of_expenses_daily) > 0.03* Total_money_month:
            print("Warning: You have spent more than the day's budget!")

        list_of_expenses_daily_month.append(sum(list_of_expenses_daily))
        
        values=[sum(list_of_expenses_daily),remaining_budget]
        labels=["Spent","Remaining"]
        plt.pie(values,labels=labels,autopct="%1.1f%%")
        plt.title("Budget status")
        plt.show()

        list_of_expenses_daily.clear()
        list_of_cartegories_daily.clear()
        list_of_Paymentmethods_daily.clear()    
        list_of_Notes_daily.clear()
        
Dashboard_button = widgets.Button(description="Dashboard", button_style='primary')
def dashboard_clicked(b):
     with output:
            output.clear_output()
            print("Dashboard!")
     dashboard()

def end_month():
    with output:
        output.clear_output()
        print("End of Month Summary:",month,",",year)
        print("Total Money for the Month:", Total_money_month)
        print("Total Expenses Recorded:", sum(list_of_expenses_daily_month))
        print("Remaining Budget:", Total_money_month - sum(list_of_expenses_daily_month))
        if sum(list_of_expenses_daily_month) > 0.8* Total_money_month:
            print("Warning: You have spent more orr equal to 80 percent of your monthly budget!Please be careful from next month")
        else:
            print("Excellent! You saved a handful amount of your monthly budget") 
        dictmonth = {
            "Month": month,
            "Total Money for the Month": Total_money_month,
            "Total Expenses Recorded": sum(list_of_expenses_daily_month),
            "Remaining Budget": Total_money_month - sum(list_of_expenses_daily_month),
        }
        values=[sum(list_of_expenses_daily_month),(Total_money_month - sum(list_of_expenses_daily_month))]
        labels=["Spent","Remaining"]
        plt.pie(values,labels=labels,autopct="%1.1f%%")
        plt.title("Budget Status Monthly")
        plt.show()
        
       
End_month_button = widgets.Button(description="End Month", button_style='danger')   
def end_month_clicked(b):
    with output:
                output.clear_output()
    end_month()
End_month_button.on_click(end_month_clicked)
Dashboard_button.on_click(dashboard_clicked)
Save_button.on_click(save_expense_clicked)
create_calendar()
display(add_expense_button)
display(Save_button)
display(result_output)
print("Click to get daily analysis:")
display(Dashboard_button)
print("Click to get monthly analysis:")
display(End_month_button)

