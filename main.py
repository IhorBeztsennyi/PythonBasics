# Importing the random module
import random

# Create list of 100 random numbers from 0 to 1000
# Creating an empty list
random_numbers = []

# For loop to generate and add 100 random numbers between 0 and 1000 to the list
for i in range(100):
    random_numbers.append(random.randint(0, 1000))

# Printind the populated list
print('Before sorting', random_numbers)

# Sort the list from Min to Max without using the sort() function
# Bubble Sort algorithm
# The number of elements in the list determining
n = len(random_numbers)
for i in range(n):
    for j in range(n - i - 1):
        if random_numbers[j] > random_numbers[j + 1]:
            # Swapping the current element if it is greater than the next one
            temp = random_numbers[j]
            random_numbers[j] = random_numbers[j + 1]
            random_numbers[j + 1] = temp

# Printind the sorted list
print('After sorting', random_numbers)