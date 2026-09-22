# Tyrese Nogess
# Personal Budget Advisor
# This program helps calculate monthly expenses and savings.

print("Personal Budget Advisor")
print("-----------------------")

Name = input("What is your name? ")

Income = float(input("Enter your monthly income: $"))

Rent           = float(input("How much do you pay for rent? $"))
Food           = float(input("How much do you spend on food? $"))
Transportation = float(input("How much do you spend on transportation? $"))
Entertainment  = float(input("How much do you spend on entertainment? $"))
Other          = float(input("Enter any other expenses: $"))

SavingsGoal = float(input("How much do you want to save each month? $"))

TotalExpenses = Rent + Food + Transportation + Entertainment + Other

MoneyLeft = Income - TotalExpenses

print()
print("Budget Results")
print("-----------------------")
print("Name:", Name)
print("Income: $", Income)
print("Total Expenses: $", TotalExpenses)
print("Money Left: $", MoneyLeft)
print("Savings Goal: $", SavingsGoal)

print()

if MoneyLeft < 0:
    print("You are over your budget.")
    print("You should try to lower your expenses.")

elif MoneyLeft < SavingsGoal:
    print("You are under your savings goal.")
    print("You may need to spend less money.")

else:
    print("You are on track with your budget.")
    print("You have enough money left for your savings goal.")

print()

if TotalExpenses > Income:
    print("Budget Status: Over Budget")

elif TotalExpenses >= Income * 0.75:
    print("Budget Status: High Spending")

elif TotalExpenses >= Income * 0.50:
    print("Budget Status: Moderate Spending")

else:
    print("Budget Status: Low Spending")

print()
print("Thanks for using the Personal Budget Advisor!")
