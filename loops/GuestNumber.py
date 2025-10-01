# number = 0
# guest_count = 3
# while not(guest_count == 0 or number == 7) :
#     number = int(input(f"Guest number (attamps({guest_count})):"))
#     guest_count = guest_count - 1
#
# if number == 7:
#     print("You win!")
# else:
#     print("You lose!")

number = 7
cout_g = 0
chance = 3

while cout_g < chance:
    guest =  int(input("guest:"))
    if guest == number:
        print("you win!")
        break
    elif cout_g == chance-1:
        print("you lost!")

    cout_g += 1
