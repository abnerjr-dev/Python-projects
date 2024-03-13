from tkinter import *
import pandas as pd
import random as r
from gtts import gTTS
import os
import playsound


BACKGROUND_COLOR = "#B1DDC6"
known_words = []

words = pd.read_csv("intermediate/flash-card-project/data/french_words.csv")
words_dict = words.to_dict(orient="records")

try:
    words_to_learn = pd.read_csv(
        "intermediate/flash-card-project/data/words_to_learn.csv"
    )

except FileNotFoundError:
    words.to_csv("intermediate/flash-card-project/data/words_to_learn.csv", index=False)
    words_to_learn = pd.read_csv(
        "intermediate/flash-card-project/data/words_to_learn.csv"
    )

finally:
    dict_to_learn = words_to_learn.to_dict(orient="records")


def know_word():
    global dict_to_learn
    dict_to_learn.remove(card)
    pd.DataFrame(dict_to_learn).to_csv(
        "intermediate/flash-card-project/data/words_to_learn.csv", index=False
    )
    new_card()


def new_card():
    global card
    lang = "fr"
    try:
        card = r.choice(dict_to_learn)
    except IndexError:
        canvas.itemconfig(card, image=back_img)
        canvas.itemconfig(lang, text="Congrats", fill="white")
        canvas.itemconfig(
            word, text="You speak French Now", fill="white", font=("Arial", 30, "bold")
        )
        x_button.config(state="disabled")
        check_button.config(state="disabled")
    else:
        current_language = list(card)[0]
        canvas.itemconfig(card_img, image=front_img)
        canvas.itemconfig(language, text=current_language, fill="black")
        canvas.itemconfig(word, text=card[current_language], fill="black")
        x_button.config(state="disabled")
        check_button.config(state="disabled")

        audio_output = gTTS(text=card["French"], lang=lang)
        audio_output.save(
            "C:/Users/Abner/OneDrive/Desktop/Udemy/Python/intermediate/flash-card-project/french_word.mp3"
        )
        playsound.playsound(
            "C:/Users/Abner/OneDrive/Desktop/Udemy/Python/intermediate/flash-card-project/french_word.mp3",
            True,
        )
        os.remove(
            "C:/Users/Abner/OneDrive/Desktop/Udemy/Python/intermediate/flash-card-project/french_word.mp3"
        )

        window.after(5000, flip_card, card)


def flip_card(card):
    lang = "en"
    current_language = list(card)[1]
    canvas.itemconfig(card_img, image=back_img)
    canvas.itemconfig(language, text=current_language, fill="white")
    canvas.itemconfig(word, text=card[current_language], fill="white")

    audio_output = gTTS(text=card["English"], lang=lang)
    audio_output.save(
        "C:/Users/Abner/OneDrive/Desktop/Udemy/Python/intermediate/flash-card-project/english_word.mp3"
    )
    playsound.playsound(
        "C:/Users/Abner/OneDrive/Desktop/Udemy/Python/intermediate/flash-card-project/english_word.mp3",
        True,
    )
    os.remove(
        "C:/Users/Abner/OneDrive/Desktop/Udemy/Python/intermediate/flash-card-project/english_word.mp3"
    )

    x_button.config(state="normal")
    check_button.config(state="normal")


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="intermediate/flash-card-project/images/card_front.png")
back_img = PhotoImage(file="intermediate/flash-card-project/images/card_back.png")
card_img = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)

word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
language = canvas.create_text(400, 150, text="title", font=("Arial", 40, "italic"))

# buttons

x_image = PhotoImage(file="intermediate/flash-card-project/images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, borderwidth=0, command=new_card)
x_button.grid(row=1, column=0)

check_image = PhotoImage(file="intermediate/flash-card-project/images/right.png")
check_button = Button(
    image=check_image, highlightthickness=0, borderwidth=0, command=know_word
)
check_button.grid(row=1, column=1)

new_card()


window.mainloop()
