import csv

people = []

with open("people_dict.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        people.append({"name": row["name"], "occupation": row["occupation"]})


for person in sorted(people, key=lambda person: person["name"]):
    print(f"{person['name']} is a(n) {person['occupation']}")
