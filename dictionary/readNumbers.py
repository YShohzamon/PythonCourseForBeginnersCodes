numbers = {
    0: "zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
}

words = ""
num = int(input("Enter number: "))

if num:
    while num > 0:
        last = num % 10
        words = numbers[last] + " " + words
        num = num // 10
else:
    print("No number")

print(words)