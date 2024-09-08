# Writing to a file ("w" mode)
with open("example.txt", "w") as file:
    file.write("This is some text that we are writing to the file.\n")
    file.write("This is another line of text.\n")

# Reading from a file ("r" mode)
with open("example.txt", "r") as file:
    content = file.read()
    print("Content of the file:")
    print(content)

# Appending to a file ("a" mode)
with open("example.txt", "a") as file:
    file.write("Appending some more text to the file.\n")
    file.write("This is the final line.\n")

# Reading the updated file ("r" mode)
with open("example.txt", "r") as file:
    updated_content = file.read()
    print("\nUpdated content of the file:")
    print(updated_content)
