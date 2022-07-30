import csv

name = input("What is your name? ")
occupation = input("What do you you for a living? ")

with open("people_dict.csv", "a", newline="\n") as file:
    writer = csv.writer(file)
    writer.writerow([name, occupation])
