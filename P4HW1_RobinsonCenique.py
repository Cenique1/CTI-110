# Your Name

# Cenique Robinson

# Date 4/10/2025

# Assignment Name

# P4HW1

# A brief description of assignment

# edit and enhance exiting programs

# Pseudocode

# Ask the user how many scores they want to enter

# Create an empty list to store scores

# Repeat for the number of scores:

# Ask the user to enter a score

# If the score is not between 0 and 100:

# Keep asking until a valid score is entered

# Add the valid score to the list

# Find the lowest score

# Show the lowest score

# Remove the lowest score from the list

# Show the list after removing the lowest score

# Calculate the average of the remaining scores

# Show the average

# Decide the letter grade based on the average

# Show the letter grade

# End the program

num_scores = int(input("How many scores would you like to enter? "))
valid_scores = []

for i in range(num_scores):
 score = float(input(f"Enter score {i+1}: "))
 while score < 0 or score > 100:
  print("Invalid score! Please enter a score between 0 and 100.")
  score = float(input(f"Enter score {i+1}: "))
 valid_scores.append(score)

lowest_score = min(valid_scores)
print(f"\nLowest score entered: {lowest_score}")
valid_scores.remove(lowest_score)

print("\nScore list after dropping the lowest score:")
print(valid_scores)

average_score = sum(valid_scores) / len(valid_scores)
print(f"\nAverage of remaining scores: {average_score:.2f}")

if average_score >= 90:
 letter_grade = 'A'
else:
 if average_score >= 80:
  letter_grade = 'B'
 else:
  if average_score >= 70:
   letter_grade = 'C'
  else:
   if average_score >= 60:
    letter_grade = 'D'
   else:
    letter_grade = 'F'

print(f"Letter grade for the average: {letter_grade}")

