with open("Daniel.txt", "w") as file:
    file.write("Hello Daniel.")

with open("Daniel.txt", "r") as file:
    content = file.read()
    print(content)