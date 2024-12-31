# Personal Expense Tracker
# Course-End Project Problem Statement

## User Menu

```
## Personal Expense Tracker ##

1.. Add   Expense
2.. View  Expenses
3.. Track Budget
4.. Save Expenses
5.. Exit


Enter your choice: 
```
## Program description
Program for personal expense tracker, it allows user to 
- Add Expense
  - User can add data, category, amount, description, values are stored as hash in an array
- View Expenses
  - It can be viewed in tabular format
- Track Budget
  - track budget after providing monthly budget it calculates expenses to tell if user is within or exceeded the budget
- Save Expenses
  - All data is in memory, as we keep adding the expenses, once Save option is selected it is stored in csv format
  - when we next time load the program all the expenses from csv is stored into hash array, and program works as expected
  - file is re-written when new entry is added, so we dont have duplicated
- Exit allows to exit the program 
  - if invalid option is give the menu re-appears for valid choice
  