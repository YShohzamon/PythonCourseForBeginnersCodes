massage = input(">")
words = massage.split()
emojes = {
    ":)": "😊",
    ":(": "😢"
}

output = ""
for word in words:
    output += emojes.get(word,word) + " "

print(output)