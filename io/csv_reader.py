import csv

people = []

with open("people.csv") as file:
    reader = csv.reader(file)
    for name, occupation in reader:
        people.append({"name": name, "occupation": occupation.lower()})

    # or
    # for row in reader:
    #     people.append({"name": row[0], "occupation": row[1]})


for person in sorted(people, key=lambda person: person["name"]):
    print(f"{person['name']} is a(n) {person['occupation']}")
