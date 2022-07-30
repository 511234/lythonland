with open("people.csv") as file:
    for line in file:

        name, occupation = line.strip().split(",")
        print(f"{name} is a {occupation}")

        # or
        # row = line.strip().split(",")
        # print(f"{row[0]} is a {row[1]}")


# Adam is a Doctor
# Bernice is a Pilot
# Cynthia is a Playwright
# Desmond is a Editor
