try:
    with open("nonexist.txt", "r") as file:
        data = file.read()
except FileNotFoundError:print("File not found. Please check the filename.")