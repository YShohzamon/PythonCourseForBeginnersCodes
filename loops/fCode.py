numbers = [5,2,5,2,2]

for item in numbers:
    print(item * "X")

print("second method")
for x_count in numbers:
    xs = ""
    for item in range(x_count):
        xs +="x"
    print(xs)