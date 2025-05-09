# Your Name

# Cenique Robinson

# Date 4/19/2025

# Assignment Name

# P5LAB

# A Brief Description of program

# Use of loops, functions and module import

import random

def disperse_change(change):
    cents = int(round(change * 100))

    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    pennies = cents

    print()
    print("    " + str(dollars) + " Dollars")
    print("    " + str(quarters) + " Quarters")
    print("    " + str(pennies) + " Pennies")

def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print()
    print("    You owe $" + str(round(amount_owed, 2)))

    cash = float(input("    How much cash will you put in the self-checkout? "))
    change = round(cash - amount_owed, 2)

    if change < 0:
        print("    Not enough cash. Please try again.")
    else:
        print("    Change is: $" + str(round(change, 2)))
        disperse_change(change)

main()
