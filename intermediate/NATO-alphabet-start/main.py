import pandas as pd


code_df = pd.read_csv("intermediate/NATO-alphabet-start/nato_phonetic_alphabet.csv")
code_dict = {row.letter: row.code for (index, row) in code_df.iterrows()}

# user_input = input("Enter a word or type 'exit': ").upper()

while True:
    user_input = input("Enter a word: ").upper()
    try:
        code_list = [code_dict[letter] for letter in user_input]

    except KeyError:
        print("Sorry, only letters in the alphabet please.")

    else:
        print(code_list)
        break
