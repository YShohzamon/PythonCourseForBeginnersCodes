me = {
    "name": "shohzmon",
    "surname":"yaqubov",
    "age": "19",
    "is_married": False
}

print(len(me))
print(me["age"])
print(me.get("birthday", "Feb 15 2006"))  #set a default
# print(me["birthday"]) error
me["birthday"] = "Feb 15 2006"
print(me)