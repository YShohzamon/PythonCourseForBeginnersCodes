weight = input("Enter your weight: ")
weight_type = input("(L)lbs or (K)kg:")

if weight_type =="L" or weight_type == "l":
    print(f"Your weight is: {float(weight) * 0.45}kg")
elif weight_type == "K" or weight_type == "k":
    print(f"Your weight is: {float(weight) / 0.45}lbs")
else:
    print("Enter K or L please!")
