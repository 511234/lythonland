animals = ["cat", "dog", "horse", "elephant", "tiger"]

# Mundane

# animals2 = []
# for animal in animals:
#     if len(animal) > 4:
#         animals2.append(animal)

# One-liner

print([animal for animal in animals if len(animal) > 4])
