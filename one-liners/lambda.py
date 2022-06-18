num = [1, 2, 3, 4, 5]

# Mundane

# new_list = []
# def numb(nlist):
#     for n in nlist:
#         new_list.append(n**2 + 5)
#     return new_list
# print(numb(num))

# One-liner

myFunc = lambda myList: [n**2 + 5 for n in myList]
print(myFunc(num))

# Or

print(list(map(lambda n: n**2 + 5, num)))
