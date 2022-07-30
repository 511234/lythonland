name = input("What is your name? ")

with open("with.txt", "a") as file:
    file.write(name + "\n")

