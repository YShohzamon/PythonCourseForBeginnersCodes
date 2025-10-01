price = 1000000
is_good_credit = False
if is_good_credit:
    price =price + price * 0.1
else:
    price =price + price * 0.2
print("Result:",price)