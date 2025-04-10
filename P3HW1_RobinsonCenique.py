# Your name

# Cenique Robinson

# Date

# 3/25/2025

# Assignment Name

# P3HW1

# a brief description of assignment

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
mod_1 = float(input('Enter grade for module 1: '))
mod_2 = float(input('Enter grade for module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))  

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average for grades
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# Determine letter grade
if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'F'

# Print results in the required format
print('\nResults\n')
print(f'Lowest Grade: {low:.1f}')
print(f'Highest grade: {high:.1f}')
print(f'Sum of grades: {total:.1f}')
print(f'Average: {avg:.2f}')
print(f'\nyour grade is: {grade}')
