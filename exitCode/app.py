try:
    age = int(input("Age: "))
    years = 20000
    print(years/age)
except ZeroDivisionError:
    print("Age can't be zero")
except ValueError:
    print("You didn't enter a number.")