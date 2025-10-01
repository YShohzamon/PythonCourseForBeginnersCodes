numbers = [71, 94, 73, 41, 152, 625, 47, 81, 92, 10]
max_number = numbers[0]
for number in numbers:
    if max_number <= number:
        max_number = number
print(max_number)