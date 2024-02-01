from cipher_art import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar(direction, text, shift):
    cipher_text = ""
    for char in text:
        if char.isalpha():
            letter_index = alphabet.index(str(char))
            if direction == "encode":
                cipher_text += alphabet[letter_index + shift]
            elif direction == "decode":
                cipher_text += alphabet[letter_index - shift]
        else:
            cipher_text += char

    print(f"The {direction}d text is {cipher_text}")


print(logo)

keep_running = True
while keep_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = shift % 26

    caesar(
        direction,
        text,
        shift,
    )
    keep_going = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n"
    ).lower()
    if keep_going == "yes":
        pass
    else:
        print("Bye!")
        keep_running = False
