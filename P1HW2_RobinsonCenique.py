# Your name

# Cenique Robinson

# Date

# 2/26/2025

# Program that does basic math on numbers that are entered

"""
Pseudocode Logic:

START
    PRINT "This program calculates and displays travel expenses"
    
    PROMPT user for budget, destination, gas, accommodation, and food expenses
    STORE user input for each of these values

    CALCULATE total expenses (gas + accommodation + food)
    CALCULATE remaining balance (budget - total expenses)

    DISPLAY the destination, initial budget, each expense, and remaining balance
END
"""

print("This program calculates and displays travel expenses")

budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas_expense = float(input("How much do you think you will spend on gas? "))
accommodation_expense = float(input("Approximately, how much will you need for accomodation/hotel? "))
food_expense = float(input("Last, How much do you need for food? "))

total_expenses = gas_expense + accommodation_expense + food_expense
remaining_budget = budget - total_expenses

print("\n---------Travel Expenses---------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print(f"Fuel: {gas_expense}")
print(f"Accommodation: {accommodation_expense}")
print(f"Food: {food_expense}")
print(f"Remaining Balance: {remaining_budget}")


  
