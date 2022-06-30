profile = {"name": "Chris", "age": 13, "food": "banana", "pet": "dinosaur"}
keys = ("age", "pet", "account")

age, pet, account = [profile.get(key) for key in keys]

print(type(age)) # int
print(age) # 13

print(type(pet)) # str
print(pet) # dinosaur

print(type(account)) # NoneType
print(account) # None
