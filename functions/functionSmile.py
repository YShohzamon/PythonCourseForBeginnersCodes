def converter_emoji(massage):
    words = massage.split()
    emojes = {
        ":)": "😊",
        ":(": "😢"
    }
    output = ""
    for word in words:
        output += emojes.get(word, word) + " "

    return output
massage = input(">")
print(converter_emoji(massage))