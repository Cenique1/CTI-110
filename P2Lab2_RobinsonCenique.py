# Your Name
# Cenique Robinson
# Date
# 2/26/2025
# P2Lab2

my_dict = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

print(my_dict.keys())

vehicle = input("Enter a vehicle to see its mpg: ")

mpg = my_dict[vehicle]
print(f"The {vehicle} gets {mpg} mpg.")

miles = float(input(f"How many miles will you drive the {vehicle}? "))

gallons_needed = miles / mpg
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")
