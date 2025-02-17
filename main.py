# Importing the random module
import random

# Creating an empty list
random_numbers = []

# For loop to generate and add 100 random numbers between 0 and 1000 to the list
for i in range(100):
    random_numbers.append(random.randint(0, 1000))

# Printind the populated list
print(random_numbers)