# Importing the random module
import random
# Importing the string module
import string

# Create a list of random number of dicts (from 2 to 10)
# Generate a random number of dicts between 2 and 10
dict_quantity = random.randint(2, 10)

# Printing random number of dicts
print(f"Random number of dicts {dict_quantity}")

# Creating an empty list to populate with dictionaries
dict_list = []

# Loop to create dictionaries
for i in range(dict_quantity):
    # Generate a random number of items for the current dictionary (between 1 and 6)
    item_quantity = random.randint(1, 6)
    # Create a dictionary with random keys and values (numbers 0-100)
    # Creating an i-th empty dictionary
    dictionary = {}
    # While loop to populate the dictionary with items
    while len(dictionary) < item_quantity:
        # Random keys are letters
        key = random.choice(string.ascii_letters)
        # Random values are numbers from 0 to 100
        value = random.randint(0, 100)
        dictionary[key] = value
    # Add the dictionary to the list
    dict_list.append(dictionary)

# Printing the list of dictionaries
print(f"List of dictionaries {dict_list}")

# Get previously generated list of dicts and create one common

# Creating an empty dictionary to count occurrences of each key
key_count = {}

# Loop through each dictionary with its index
for index_dict, dict in enumerate(dict_list):
    # Loop through each key in the current dictionary
    for key in dict:
        if key in key_count:
            # Add a tuple with the number of the dictionary and its value to the existing list
            key_count[key].append((index_dict, dict[key]))
        else:
            # First item addition
            key_count[key] = [(index_dict, dict[key])]

# Printing the list of dictionaries
print(f"Keys count dictionary {key_count}")

# Creating an empty dictionary to store the final result
result_dict = {}

# Result dictionary populating
for key, value_list in key_count.items():
    # If the key appears once
    if len(value_list) == 1:
        # Adding item to the result dictionary
        result_dict[key] = value_list[0][1]
        # If the key appears in several dictionaries
    else:
        # Maximum value and its dictionary index
        # Initialize the first tuple as maximum
        max_value = value_list[0]
        for item in value_list:
            # Compare the next value
            if item[1] > max_value[1]:
                # Update maximum value if a bigger value is found
                max_value = item
        # Rename the key with the dictionary number, underscore and index of the dictionary with max value
        result_dict[f"{key}_{max_value[0] + 1}"] = max_value[1]

# Printing the result dictionary
print(f"Result dictionary {result_dict}")
