# Your name

# Cenique Robinson

# Date

# 3/25/2025

# Assignment Name

# P3HW2

# A brief description of assignment

# Understanding of decision structures

# Pseudocode:

# Get employee's name

# Get hours worked

# Get pay rate

# If hours > 40:

# - regular hours = 40

# - overtime hours = hours - 40

# Else:

# - regular hours = hours

# - overtime hours = 0

# regular pay = regular hours * pay rate

# overtime pay = overtime hours * pay rate * 1.5

# gross pay = regular pay + overtime pay

# Print all the info in a table

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * (pay_rate * 1.5)
gross_pay = regular_pay + overtime_pay

print("\nEmployee name:", employee_name)

print("\nHours Worked  Pay Rate    OverTime   OverTime Pay   RegHour Pay   Gross Pay")
print("----------------------------------------------------------------------------")

print(f"{hours_worked:<12.1f} {pay_rate:<10.1f} {overtime_hours:<10.1f} ${overtime_pay:<12.2f} ${regular_pay:<12.2f} ${gross_pay:<12.2f}")

