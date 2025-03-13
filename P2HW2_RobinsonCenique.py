# Your name

# Cenique Robinson

# Date

# 3/13/2025

# Assignment Name

# P2HW2

# Brief Description of assignment

# Grades

# Pseudocode:

# Prompt the user to enter grades for Module 1 to Module 6 separately.

# Store the grades in a list.

# Calculate the lowest grade using the min() function.

# Calculate the highest grade using the max() function.

# Calculate the sum of all grades using the sum() function.

# Calculate the average by dividing the sum of grades by the number of modules.

# Display the results with correct formatting and two decimal places for the average.

grades = [
    float(input("Enter grade for Module 1: ")),
    float(input("Enter grade for Module 2: ")),
    float(input("Enter grade for Module 3: ")),
    float(input("Enter grade for Module 4: ")),
    float(input("Enter grade for Module 5: ")),
    float(input("Enter grade for Module 6: "))
]

print("\n------------Results------------")
print(f"{'Lowest Grade:':20} {min(grades):.1f}")
print(f"{'Highest Grade:':20} {max(grades):.1f}")
print(f"{'Sum of Grades:':20} {sum(grades):.1f}")
print(f"{'Average:':20} {sum(grades)/len(grades):.2f}")
print("--------------------------------")
