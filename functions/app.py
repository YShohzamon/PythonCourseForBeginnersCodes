def greeting():
    print("Hello")

greeting()

def greeting2(name, surname):
    print(f"Hello {name} {surname}")
greeting2("shohzamon", "yaqubov")

def greeting3(name, surname):
    print(f"Hello {name} {surname}")
greeting3("shohzamon", surname="yaqubov") #positional then keyword


def pow(n):
    return n * n

print(pow(3))
