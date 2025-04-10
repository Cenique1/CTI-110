# Your name

# Cenique Robinson

# Date

# 4/10/2025

# Assignment Name

# P4LAB2

# a brief description of assignment

# write code that displays information to users using loops

repeat = "yes"

while repeat == "yes":
    number = int(input("Enter an integer: "))

    if number < 0:
        print("This program does not handle negative numbers.")
    else:
        for i in range(1, 13):
            print(number, "*", i, "=", number * i)

    repeat = input("Would you like to run the program again? ").lower()  # .lower() makes the input case-insensitive
    if repeat != "yes":
        print("Exiting program...")

