def main():
    print("Welcome to the Dictionary Operations Program")

    # Creating and inserting into the dictionary
    dictionary = {}
    print("\nCreating and inserting into the dictionary:")
    num_entries = int(input("How many entries do you want to add? "))
    for _ in range(num_entries):
        key = input("Enter key: ")
        value = input("Enter value: ")
        dictionary[key] = value
    print("Dictionary after insertion:", dictionary)

    # Updating the dictionary
    print("\nUpdating the dictionary:")
    update_key = input("Enter the key to update: ")
    if update_key in dictionary:
        new_value = input("Enter the new value: ")
        dictionary[update_key] = new_value
        print("Dictionary after update:", dictionary)
    else:
        print(f"Key '{update_key}' not found in dictionary.")

    # Deleting from the dictionary
    print("\nDeleting from the dictionary:")
    delete_key = input("Enter the key to delete: ")
    if delete_key in dictionary:
        del dictionary[delete_key]
        print("Dictionary after deletion:", dictionary)
    else:
        print(f"Key '{delete_key}' not found in dictionary.")

    # Looping in the dictionary
    print("\nLooping through the dictionary:")
    for key, value in dictionary.items():
        print(f"Key: {key}, Value: {value}")

    # Sorting the dictionary
    print("\nSorting the dictionary by keys:")
    sorted_dictionary = dict(sorted(dictionary.items()))
    print("Dictionary after sorting:", sorted_dictionary)

if __name__ == "__main__":
    main()
