# # Importing the random module
# import random
# # Importing the string module
# import string
#
# # Create a list of random number of dicts (from 2 to 10)
# # Generate a random number of dicts between 2 and 10
# dict_quantity = random.randint(2, 10)
#
# # Printing random number of dicts
# print(f"Random number of dicts {dict_quantity}")
#
# # Creating an empty list to populate with dictionaries
# dict_list = []
#
# # Loop to create dictionaries
# for i in range(dict_quantity):
#     # Generate a random number of items for the current dictionary (between 1 and 6)
#     item_quantity = random.randint(1, 6)
#     # Create a dictionary with random keys and values (numbers 0-100)
#     # Creating an i-th empty dictionary
#     dictionary = {}
#     # While loop to populate the dictionary with items
#     while len(dictionary) < item_quantity:
#         # Random keys are letters
#         key = random.choice(string.ascii_letters)
#         # Random values are numbers from 0 to 100
#         value = random.randint(0, 100)
#         dictionary[key] = value
#     # Add the dictionary to the list
#     dict_list.append(dictionary)
#
# # Printing the list of dictionaries
# print(f"List of dictionaries {dict_list}")
#
# # Get previously generated list of dicts and create one common
#
# # Creating an empty dictionary to count occurrences of each key
# key_count = {}
#
# # Loop through each dictionary with its index
# for index_dict, dict in enumerate(dict_list):
#     # Loop through each key in the current dictionary
#     for key in dict:
#         if key in key_count:
#             # Add a tuple with the number of the dictionary and its value to the existing list
#             key_count[key].append((index_dict, dict[key]))
#         else:
#             # First item addition
#             key_count[key] = [(index_dict, dict[key])]
#
# # Printing the list of dictionaries
# print(f"Keys count dictionary {key_count}")
#
# # Creating an empty dictionary to store the final result
# result_dict = {}
#
# # Result dictionary populating
# for key, value_list in key_count.items():
#     # If the key appears once
#     if len(value_list) == 1:
#         # Adding item to the result dictionary
#         result_dict[key] = value_list[0][1]
#         # If the key appears in several dictionaries
#     else:
#         # Maximum value and its dictionary index
#         # Initialize the first tuple as maximum
#         max_value = value_list[0]
#         for item in value_list:
#             # Compare the next value
#             if item[1] > max_value[1]:
#                 # Update maximum value if a bigger value is found
#                 max_value = item
#         # Rename the key with the dictionary number, underscore and index of the dictionary with max value
#         result_dict[f"{key}_{max_value[0] + 1}"] = max_value[1]
#
# # Printing the result dictionary
# print(f"Result dictionary {result_dict}")


# Importing the random module
import random
# Importing the string module
import string
# Importing the JSON module
import json


# Generates a list of dictionaries with random keys and values.
def generate_random_dicts():
    try:
        dict_quantity = random.randint(2, 10)
        dict_list = []
        for i in range(dict_quantity):
            item_quantity = random.randint(1, 6)
            dictionary = {}
            while len(dictionary) < item_quantity:
                key = random.choice(string.ascii_letters)
                value = random.randint(0, 100)
                dictionary[key] = value
            dict_list.append(dictionary)
        return dict_list
    except Exception as e:
        print(f"An unexpected error occurred when generating random dictionaries: {e}")
        return []


# Aggregates dictionaries by keeping the maximum value for each key.
def aggregate_dicts(dict_list):
    result_dict = {}
    key_data = {}

    if not type(dict_list) is list:
        raise TypeError('Only lists are allowed.')
    for index, current_dict in enumerate(dict_list):
        if not type(current_dict) is dict:
            raise TypeError('Only dictionaries in the list are allowed.')
        for key, value in current_dict.items():
            if not type(key) is str:
                raise TypeError('Only strings as a key in the dictionaries are allowed.')
            if not type(value) is int:
                raise TypeError('Only integers as a value in the dictionaries are allowed.')
            if key in key_data:
                if value > key_data[key]["max_value"]:
                    key_data[key] = {"max_value": value, "index": index}
            else:
                key_data[key] = {"max_value": value, "index": index}

    for key, data in key_data.items():
        if sum(1 for d in dict_list if key in d) == 1:
            result_dict[key] = data["max_value"]
        else:
            result_dict[f"{key}_{data['index'] + 1}"] = data["max_value"]

    return result_dict



# Main function to generate dictionaries and aggregate them.
def main():
    dict_list = generate_random_dicts()
    print(f"List of dictionaries: {json.dumps(dict_list, indent=2)}")
    result_dict = aggregate_dicts(dict_list)

    if not result_dict:
        print("Result dictionary is empty.")
    else:
        print(f"Result dictionary: {json.dumps(result_dict, indent=2)}")


if __name__ == "__main__":
    main()
