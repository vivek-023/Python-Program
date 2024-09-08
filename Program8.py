import os

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Content written to {file_path}")

def read_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    print(f"Content read from {file_path}:\n{content}")
    return content

def append_to_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)
    print(f"Content appended to {file_path}")

def rename_file(old_name, new_name):
    os.rename(old_name, new_name)
    print(f"File renamed from {old_name} to {new_name}")

def delete_file(file_path):
    os.remove(file_path)
    print(f"File {file_path} deleted")

def file_operations_demo():
    file_path = 'file.txt'
    new_file_path = 'renamed_file.txt'
    content = "Hello, this is a test file.\n"
    additional_content = "Appending some more text.\n"

    # Writing to a file
    write_to_file(file_path, content)

    # Reading from the file
    read_from_file(file_path)

    # Appending to the file
    append_to_file(file_path, additional_content)

    # Reading from the file again
    read_from_file(file_path)

    # Renaming the file
    rename_file(file_path, new_file_path)

    # Reading from the renamed file
    read_from_file(new_file_path)

    # Deleting the file
    delete_file(new_file_path)

if __name__ == "__main__":
    file_operations_demo()
