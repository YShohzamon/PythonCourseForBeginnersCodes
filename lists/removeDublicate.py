names = ["saloh", "behruz" , "aziz" , "suxron", "ali", "doston", "aziz", "saloh"]
names.sort()
for name in names:
    count = 0
    for i in range(len(names)):
        if names[i] == name:
            count += 1

    if count > 1:
        names.remove(name)
print(names)

print("Mathod 2")
numbers = [1, 2, 1, 4, 5, 7, 7, 5, 9, 3]
numbers2 = []

for number in numbers:
    if number not in numbers2:
        numbers2.append(number)
print(numbers2)