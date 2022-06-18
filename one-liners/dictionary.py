colors = {
    "cat": "gray",
    "dog": "white",
    "pig": "pink",
    "horse": "gray",
    "elephant": "gray",
    "monkey": "brown",
}

# Mundane

# animals = []
# for k, v in colors.items():
#     if v == "gray":
#         animals.append(k)

# One-liner

print([k for k, v in colors.items() if v == "gray"])
