# # Importing the random module
# import random
#
# # Create list of 100 random numbers from 0 to 1000
# # Creating an empty list
# random_numbers = []
#
# # For loop to populate the list with 100 random numbers between 0 and 1000
# for i in range(100):
#     random_numbers.append(random.randint(0, 1000))
#
# # Printind the populated list
# print(f"Before sorting {random_numbers}")
#
# # Sort the list from Min to Max without using the sort() function
# # The number of elements in the list determining
# n = len(random_numbers)
# # Bubble Sort algorithm
# for i in range(n):
#     for j in range(n - i - 1):
#         if random_numbers[j] > random_numbers[j + 1]:
#             # Swapping the current element if it is greater than the next one
#             temp = random_numbers[j]
#             random_numbers[j] = random_numbers[j + 1]
#             random_numbers[j + 1] = temp
#
# # Printing the sorted list
# print(f"After sorting {random_numbers}")
#
# # Calculate the average for even and odd numbers
#
# # Variables initializing
# count_even = 0
# sum_even = 0
# count_odd = 0
# sum_odd = 0
#
# # Sum and count of even and odd numbers calculating
# for i in random_numbers:
#     if i % 2 == 0:
#         # If the remainder is 0, add to even sum
#         sum_even += i
#         # Increment even count
#         count_even += 1
#     else:
#         # Add to odd sum if the number is odd
#         sum_odd += i
#         # Increment odd count
#         count_odd += 1
#
# # Average of even numbers calculation
# # Check if count_even to avoid division by zero
# if count_even > 0:
#     average_even = sum_even / count_even
# else:
#     average_even = 0
#
# # Average of odd numbers calculation
# # Check if count_odd > 0 to avoid division by zero
# if count_odd > 0:
#     average_odd = sum_odd / count_odd
# else:
#     average_odd = 0
#
# # Printing the average of even numbers rounded to two decimal places
# print(f"Average of even numbers: {round(average_even, 2)}")
# # Printing the average of odd numbers rounded to two decimal places
# print(f"Average of odd numbers: {round(average_odd, 2)}")

import random


def generate_random_numbers(count=100, min_value=0, max_value=1000):
    """Generates a list of 'count' random numbers within a given range."""
    return [random.randint(min_value, max_value) for _ in range(count)]


def bubble_sort(arr):
    """Sorts a list using the Bubble Sort algorithm."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swapping in one line
                swapped = True
        if not swapped:
            break  # If no swaps were made, the list is already sorted


def calculate_averages(arr):
    """Calculates the average for even and odd numbers in the list."""
    evens = [num for num in arr if num % 2 == 0]
    odds = [num for num in arr if num % 2 != 0]

    avg_even = sum(evens) / len(evens) if evens else 0
    avg_odd = sum(odds) / len(odds) if odds else 0

    return round(avg_even, 2), round(avg_odd, 2)


# Generate a list of random numbers
random_numbers = generate_random_numbers()

print(f"Before sorting: {random_numbers}")

# Sort the list
bubble_sort(random_numbers)

print(f"After sorting: {random_numbers}")

# Calculate averages
average_even, average_odd = calculate_averages(random_numbers)

print(f"Average of even numbers: {average_even}")
print(f"Average of odd numbers: {average_odd}")