# Your name

# Cenique Robinson

# Date

# 3/13/2025

# Assignment Name

# P2HW1

# a brief description of the project

# Travel expenses

budget = float(input("Enter Budget: "))
destination = input("\nEnter your travel destination: ")
fuel = float(input("\nHow much do you think you will spend on gas? "))
accommodation = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

remaining_balance = budget - (fuel + accommodation + food)

print("\n------------Travel Expenses------------")
print(f"{'Location:':20} {destination}")
print(f"{'Initial Budget:':20} ${budget:,.2f}")
print(f"{'Fuel:':20} ${fuel:,.2f}")
print(f"{'Accommodation:':20} ${accommodation:,.2f}")
print(f"{'Food:':20} ${food:,.2f}")
print("----------------------------------------")
print(f"{'Remaining Balance:':20} ${remaining_balance:,.2f}")

