#CIS-30A Final Project Option 2: Personal Finance Tracking Program
#Julian Pina



import tkinter as tk
from tkinter import messagebox
from finance_module import displayAmount #Import function from extra module

#Define a class
class Finance1:
    def __init__(self, budget, income, expenses, savings):
        self.budget = budget
        self.income = income
        self.expenses = expenses
        self.savings = savings

    def calculateRemaining(self):
        return self.income - (self.expenses + self.savings)

#The subclass will display the summary
class Finance2(Finance1):
    def showSummary(self):
        summary = (
            "Budget: " + displayAmount(self.budget) + "\n"
            "Income: " + displayAmount(self.income) + "\n"
            "Expenses: " + displayAmount(self.expenses) + "\n"
            "Savings: " + displayAmount(self.savings) + "\n"
            "Remaining Amount: " + displayAmount(self.calculateRemaining())
        )
        return summary

#Function to save Finance data to a file
def saveFile(financeData):
    with open('finance_tracker.txt', 'w') as file:
        file.write('Personal Finance Summary\n')
        file.write(financeData.showSummary())

#Function for user input
def financeInput():
    try:
        budget = float(input_budget.get())
        income = float(input_income.get())
        expenses = float(input_expenses.get())
        savings = float(input_savings.get())

        financeData = Finance2(budget, income, expenses, savings)
        summary = financeData.showSummary()

        saveFile(financeData)

        messagebox.showinfo('Finance Report', summary)
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers.')

#Integrate Tkinter UI
root = tk.Tk()
root.title('My Finance Tracker')

#UI Labels
tk.Label(root, text ='Enter your budget: ').grid(row=0, column=0)
input_budget = tk.Entry(root)
input_budget.grid(row=0, column=1)

tk.Label(root, text='Enter your income: ').grid(row=1, column=0)
input_income = tk.Entry(root)
input_income.grid(row=1, column=1)

tk.Label(root, text='Enter your expenses: ').grid(row=2, column=0)
input_expenses = tk.Entry(root)
input_expenses.grid(row=2, column=1)

tk.Label(root, text='Enter your savings goal: ').grid(row=3, column=0)
input_savings = tk.Entry(root)
input_savings.grid(row=3, column=1)

#Submit Button
tk.Button(root, text='Save and View Report', command=financeInput).grid(row=4, column=0, columnspan=2)

#Run Tkinter UI
root.mainloop()





                        
