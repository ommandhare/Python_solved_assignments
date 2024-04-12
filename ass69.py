my_list = [1, 2, 3, 4, 1, 2, 3, 5, 1, 2, 6, 7, 8, 6, 7, 8, 9]

def count_occurrences(lst):
    # Initialize an empty dictionary to store occurrences
    occurrences = {}

    # Iterate through the list
    for number in lst:
        # Check if the number is already in the dictionary
        if number in occurrences:
            # Increment the count if the number is already present
            occurrences[number] += 1
        else:
            # Add the number to the dictionary with count 1 if not present
            occurrences[number] = 1

    return occurrences



result = count_occurrences(my_list)


for number, count in result.items():
    print(f"{number}: {count} occurrences")
