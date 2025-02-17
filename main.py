# Importing the random module
import random

# Create list of 100 random numbers from 0 to 1000
# Creating an empty list
random_numbers = []

# For loop to generate and add 100 random numbers between 0 and 1000 to the list
for i in range(100):
    random_numbers.append(random.randint(0, 1000))

# Printind the populated list
print(f"Before sorting {random_numbers}")

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
print(f"After sorting {random_numbers}")

# Calculate the average for even and odd numbers

# Variables initializing
count_even = 0
sum_even = 0
count_odd = 0
sum_odd = 0

# Sum and count of even and odd numbers calculating
for i in random_numbers:
    if i % 2 == 0:
        # If the remainder is 0, add to even sum
        sum_even += i
        # Increment even count
        count_even += 1
    else:
        # Add to odd sum if the number is odd
        sum_odd += i
        # Increment odd count
        count_odd += 1

# Average of even numbers calculation
if count_even > 0:
    average_even = sum_even / count_even
else:
    average_even = 0

# Average of odd numbers calculation
if count_odd > 0:
    average_odd = sum_odd / count_odd
else:
    average_odd = 0

# Print the average of even and odd numbers rounded to two decimal places
print(f"Average of even numbers: {round(average_even, 2)}")
print(f"Average of odd numbers: {round(average_odd, 2)}")