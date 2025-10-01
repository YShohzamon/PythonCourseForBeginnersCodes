# if elif else

is_hot = True
is_cold  = False

if is_hot:
    print("today is hot day")
elif is_cold:
    print("today is cold day")
else:
    print("today is normal day")
print("enjoy your day")

if is_hot and is_cold:
    print("It is impossible situation!!!")

if is_hot or is_cold:
    print("It is possible situation.")

if not is_cold:
    print("This information is lying you. Today is hot!")
