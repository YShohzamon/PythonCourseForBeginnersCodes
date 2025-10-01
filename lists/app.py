names = ["shohzamon", "behruz", "salohiddin", "ozodbek", "ruslan"]
print(names[:2])

names.append("doston")
names.insert(2, "alisher")
names.remove("alisher")
names.pop()
names.sort()
names2 = names.copy()
names2.clear()

print('behruz' in names)
print(names)
print(names2)

print(names.count(""))

# tuples like lists. but you can't modify them.
num  = (1,3,5)
x,y,z = num
print(x,y,z)