with open("example.txt", "w") as file:
    file.write("This is some text that we are writing to the file.\n")
    file.write("This is another line of text.\n")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

with open("example.txt", "a") as file:
    file.write("Appending some more text to the file.\n")
    file.write("This is the final line.\n")

with open("example.txt", "r") as file:
    updated_content = file.read()
    print(updated_content)
