index = input("Enter an index: ")
testing_string = f'Crazy{["","_"+str(index)][index>0]}'
print(testing_string)

# If index <= 0
# print Crazy

# If index > 0
# print Crazy_{{ index }}
# e.g. Crazy_1

# Scenario 1: "" (empty string)
# Scenario 2: _{{ index}} (underscore and index)
# Scenario 1 and 2 make a list
# If index > 0, it's true, and true = 0
# If index <= 0, it's false, and false = 1
# so use condition to determine whether to use index 0 or 1 of the previous list
# took me some time to figure it out :/ brain teaserrrrrrrrr