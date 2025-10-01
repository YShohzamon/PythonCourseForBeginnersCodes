class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello {self.name}")


person1 = Person("shohzamon")
person1.talk()

class Animals:
    def wolk(self):
        print("Animal is wolking.")

class Dog(Animals):
    def bark(self):
        print("Dog is barking.")

class Cat(Animals):
    def hungry(self):
        print("Cat is hungry.")

cat = Cat()
cat.hungry()