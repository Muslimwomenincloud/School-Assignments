# Fatimatou Ibrahim - Module 6 Assignment
# This program checks whether numbers in a list are odd or even.

# Step 1: Create a list of 15 numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Step 2: Loop through the list
for number in numbers:
    # Step 3: Check if the number is even or odd
    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")
