# Python program
# Course-End Project: Personal Expense Tracker

import os
    
def expense_input() :
    expense={}
    print("\n## Add Expense ##\n")
    print("Please enter below details for expense tracking")
    e_date=input        ("Date (YYYY-MM-DD)             : ")
    e_category=input    ("Category: (Food/Travel/Books) : ")
    e_description=input ("Description                   : ")
    e_amount=float(input("Amount spent                  : "))
    print("\n## Added Expense Done.##\n")
    expense['date']=e_date
    expense['category']=e_category
    expense['amount']=e_amount
    expense['description']=e_description
    expenses.append(expense)
        
def expenses_store():
    print("\n## Storing Expenses ##\n")    
    expenses_file = 'expenses.csv'
    with open(expenses_file, "w+") as f:
        for expense in expenses:
            f.write("{},{},{},{}\n".format(expense['date'],expense['category'],expense['amount'],expense['description']))
        
def expenses_view():
    print("\n## Expenses View ##\n")    

    if not expenses:
        print("No expenses stored.. you need to add first")
        return
    
    print("Date\t\tCategory\tAmount\tDescription")
    for expense in expenses:
            if not (expense['date'] or expense['category'] or expense['amount'] or expense['description']):
                print("There are incomplete information.. skipping")
                return
            
            print(f"{expense['date']:<10}\t{expense['category']:<10}\t{expense['amount']:>10}\t{expense['description']}")
        
def expenses_load():    
    expenses_file = 'expenses.csv'
    if os.path.exists(expenses_file):
        mode='r'
    else:
        return 
    with open(expenses_file, mode) as f:
        expenses_readline=f.read()
        
    for r in expenses_readline.splitlines():
            r_date,r_category,r_amount,r_description=r.strip().split(',')
            expens1={}
            expens1['date'],expens1['category'],expens1['description'],expens1['amount']=r_date,r_category,r_description,float(r_amount)
            expenses.append(expens1)

def budget_track():   
    total_expenses=0
    print("\n## Budget Tracker ##\n")    
    budget=float(input("Enter total monthly budget: "))
    for expense in expenses:
        total_expenses+=expense['amount']
    
    total=budget-total_expenses
    if (total<=0):
        print(f"Warning: you have exceeded the budget: {total}")
    else:
        print(f"You are within budget, total balance : {total}")
            
## main

expenses=[]
expenses_load()

while True:
    print("\n## Personal Expense Tracker ##\n")
    print("1.. Add   Expense\n2.. View  Expenses\n3.. Track Budget\n4.. Save Expenses\n5.. Exit\n\n")
    choice=int(input("Enter your choice: "))
    
    if choice==1:
        user_expense=expense_input()
    elif choice==2:
        expenses_view()
    elif choice==3:
        budget_track()
    elif choice==4:
        expenses_store()
    elif choice==5:
        print("\nExiting.. the program..\n\n")
        break
    else:
        print("Invalid choice..")
    
## Done.
