# Define the function
def greater_than(x, y):
    if x > y:
        return True
    else:
        return False

# First test: a = 2, b = 3
a = 2
b = 3
result = greater_than(a, b)

# Print result for first test
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))

# Second test: a = 10, b = 6
a = 10
b = 6
result = greater_than(a, b)

# Print result for second test
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))
