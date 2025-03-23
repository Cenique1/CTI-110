# Your name

# Cenique Robinson

# Date

# 3/22/2025

# Assignment Name

# P3LAB

# A Brief description of assignment

# Branching


amount = float(input("Enter a dollar amount as a float: "))
cents = int(amount * 100)

dollars = cents // 100
cents = cents % 100
if dollars > 0:
    if dollars == 1:
        print("1 dollar")
    else:
        print(f"{dollars} dollars")

quarters = cents // 25
cents = cents % 25
if quarters > 0:
    if quarters == 1:
        print("1 quarter")
    else:
        print(f"{quarters} quarters")

dimes = cents // 10
cents = cents % 10
if dimes > 0:
    if dimes == 1:
        print("1 dime")
    else:
        print(f"{dimes} dimes")

nickels = cents // 5
cents = cents % 5
if nickels > 0:
    if nickels == 1:
        print("1 nickel")
    else:
        print(f"{nickels} nickels")

pennies = cents
if pennies > 0:
    if pennies == 1:
        print("1 penny")
    else:
        print(f"{pennies} pennies")
