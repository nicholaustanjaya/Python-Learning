with open("my_notes.txt", "w") as file:
    file.write("This is my first Python file.\n")
    file.write("I’m learning file handling!\n")
with open("my_notes.txt", "r") as file:
    contents = file.read()
    print(contents)
