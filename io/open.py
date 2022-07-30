with open("close.txt", "r") as file:
    # default is read mode
    lines = file.readlines()

for line in lines:
    print(line, end="")
