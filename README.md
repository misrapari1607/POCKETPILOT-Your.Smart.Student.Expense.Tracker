# POCKETPILOT-Your.Smart.Student.Expense.Manager
# OVERVIEW:
Smart Expense TRacker is a Python-based expense management application designed to help college students and hostellers manage their monthly budget.
The project provides an interactive calendar-based interface where users can select a particular date and record expenses alone with their category, payment method, and notes.
The system also provides daily and monthly ananlysis using tables, budget calculations, warnings and pie-charts.
# FEATURES:
1. Calendar-Based Date Selection-
    The application provides an interactive calendar using ipywidgets. Users can select the date on which an expense occured.
2. Montly Budget Management-
    The user enters the total amount of money available for the month.The system uses this amount to calculate spending and remaining budget.
3. Expense Recording-
    - Expense Amount
    - Expense Category: 
        Available categories:-
            Food, Transportation, Utilities, Necessities, other
    - Payment Method:
        The application supports:-
            Cash, Credit Card, Debit Card, Bank Transfer, UPI, Other
    - Notes
    - Expense date
4. Expense Table-
    Saved Expenses are displayed in a structured table containing:
        Date, Amount, Category, Payment Method, Notes, Running Total, Remaining Budget
5. Dashboard-
    The dashboard provides daily analysis including:
        Daily budgets, Total expenses recorded, savings, pie-chart(Using matplotlib.pyplot)
6. Budget Warnings-
    THis application provides warnings when spending crosses predefined limits.
7. End-of-Month Summary-
    At the end of the month, the system displays:
        Total monthly budget, Total expenses, Remaining budget, MOnthly spending warning, Monthly budget pie chart
# Technologies/Tool used:
1. Programming Language:
    Python
2. Libraries:
    calendar, ipywidgets, tabulate, IPython.display, matplotlib
# Steps to install and run the project:
1. INSTALLATION:
    Step 1: Install Python
        Install Python 3.x on your computer.
    Step 2: Install Required Libraries
        Open Command Prompt or Terminal and run:
        pip install ipywidgets tabulate matplotlib
    Step 3: Start Jupyter Notebook
        Run:
        jupyter notebook
    Step 4: Open the Project
        Open the project notebook containing the Smart Expense Tracker code.
2. RUN THE CODE:
    1.Run the Python/Jupyter Notebook.
    2.Enter the total amount of money available for the month.
    3.Enter the required year.
    4.Enter the required month.
    5.Select a date from the calendar.
    6.Click Add Expense.
    7.Enter:
        Amount
        Category
        Payment Method
        Notes
    8.Click Save Expense.
    9.View the saved expense in the expense table.
    10.Click Dashboard to view daily analysis.
    11.View the spending and remaining budget through the pie chart.
    12.At the end of the month, click End Month to view the monthly summary.
# Instructions for testing:
    1.Ensure that Python 3.x and the required libraries are installed.
    2.Install the required libraries using:
        pip install ipywidgets matplotlib tabulate
    3.Keep all project .py modules in the same project folder.
    4.Open the project through Jupyter Notebook/JupyterLab when using the ipywidgets interface.
    5.Import the required functions from the Python modules.
    6.Run the main program and enter the monthly available amount.
    7.Select a date using the calendar.
    8.Use the Add Expense button to enter and save expense details.
    9.Verify that the saved expenses are displayed correctly.
    10.Add multiple expenses and verify the updated remaining budget.
    11.Test different dates, categories, payment methods, income, and savings values.
    12.If charts are included, verify that the charts represent the entered data correctly.
    13.Test different inputs and verify that the expected results are produced without errors.
    14.Check the results on different dates.