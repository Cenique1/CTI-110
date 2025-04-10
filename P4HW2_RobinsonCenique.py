# Your Name

# Cenique Robinson

# Date

# 4/10/2025

# A brief desscription of the project

# edit and enhance programs

# Pseudocode:

# Start

# Set total number of employees to 0

# Set total overtime pay to 0

# Set total regular pay to 0

# Set total gross pay to 0

# Ask user to enter employee's name or "Done" to end

# While employee's name is not "Done":

# Ask how many hours the employee worked

# Ask what the employee's pay rate is

# If hours worked is more than 40:

# Set overtime hours = hours worked - 40

# Set regular hours = 40

# Else:

# Set overtime hours = 0

# Set regular hours = hours worked

# Calculate overtime pay = overtime hours * pay rate * 1.5

# Calculate regular pay = regular hours * pay rate

# Calculate gross pay = overtime pay + regular pay

# Display the employee's pay details

# Add 1 to total number of employees

# Add overtime pay to total overtime pay

# Add regular pay to total regular pay

# Add gross pay to total gross pay

#Ask for the next employee's name or "Done" to end

# Display total number of employees

# Display total overtime pay

# Display total regular pay

# Display total gross pay

# End

total_employees = 0
total_overtime = 0.0
total_regular = 0.0
total_gross = 0.0

name = input('Enter employee\'s name or "Done" to terminate: ')

while name != "Done":
    hours = float(input(f"How many hours did {name} work? "))
    rate = float(input(f"What is {name}'s pay rate? "))

    if hours > 40:
        overtime_hours = hours - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours

    overtime_pay = overtime_hours * rate * 1.5
    regular_pay = regular_hours * rate
    gross_pay = overtime_pay + regular_pay

    print()
    print("Employee name:", name)
    print()
    print("Hours Worked  Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
    print("-------------------------------------------------------------------------------")
    print(f"{hours:<13} {rate:<10.2f} {overtime_hours:<10} ${overtime_pay:<14.2f} ${regular_pay:<13.2f} ${gross_pay:<.2f}")
    print()

    total_employees += 1
    total_overtime += overtime_pay
    total_regular += regular_pay
    total_gross += gross_pay

    name = input('Enter employee\'s name or "Done" to terminate: ')

print("Total number of employees entered:", total_employees)
print(f"Total amount paid for overtime: ${total_overtime:.2f}")
print(f"Total amount paid for regular hours: ${total_regular:.2f}")
print(f"Total amount paid in gross: ${total_gross:.2f}")
