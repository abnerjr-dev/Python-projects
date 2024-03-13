from tkinter import *
from tkinter.ttk import *


window = Tk()
window.minsize(width=150, height=150)
window.title("Distance Converter")
window.config(padx=20, pady=20)
FONT = ("Arial", 18, "bold")


def reset():
    from_txt.config(text="")
    to_txt.config(text="")
    input.delete(first=0, last=END)
    result.config(text="0")


def miles_to_km():
    from_txt.config(text="Mile")
    to_txt.config(text="Km  ")
    final_result = round(float(input.get()) * 1.609, 2)
    result.config(text=f"{final_result}")


def km_to_m():
    from_txt.config(text="Km  ")
    to_txt.config(text="m  ")
    final_result = round(float(input.get()) * 1000, 2)
    result.config(text=f"{final_result}")


def m_to_km():
    from_txt.config(text="m  ")
    to_txt.config(text="Km  ")
    final_result = round(float(input.get()) / 1000, 4)
    result.config(text=f"{final_result}")


def km_to_miles():
    from_txt.config(text="Km  ")
    to_txt.config(text="Mile")
    final_result = round(float(input.get()) / 1.609, 2)
    result.config(text=f"{final_result}")


def m_to_miles():
    from_txt.config(text="m  ")
    to_txt.config(text="Mile")
    final_result = round(float(input.get()) / 1609, 4)
    result.config(text=f"{final_result}")


def miles_to_m():
    from_txt.config(text="Mile")
    to_txt.config(text="m  ")
    final_result = round(float(input.get()) * 1609, 2)
    result.config(text=f"{final_result}")


def calculate():
    if input.get() != "":
        conversion = conversions_dict[listbox.get(listbox.curselection())]
        conversion()


instructions = Label(text="Click the Option to Convert", font=FONT)
instructions.grid(column=1, row=0)
instructions.config(padding=[10, 10])

input = Entry(width=10, font=FONT)
input.focus()
input.grid(column=1, row=1)

from_txt = Label(text="", font=FONT)
from_txt.grid(column=2, row=1)
from_txt.config(padding=[10, 10])

equal_txt = Label(text="is equal to: ", font=FONT)
equal_txt.grid(column=0, row=2)

result = Label(text="", font=FONT)
result.grid(column=1, row=2)
result.config(padding=[20])

to_txt = Label(text="", font=FONT)
to_txt.grid(column=2, row=2)

reset_btn = Button(text="Reset", command=reset)
reset_btn.grid(column=0, row=3)

calculate_btn = Button(text="Calculate", command=calculate)
calculate_btn.grid(column=1, row=3)


conversions_dict = {
    "Miles to Kilometer": miles_to_km,
    "Kilometer to Miles": km_to_miles,
    "Kilometer to Meter": km_to_m,
    "Meter to Kilometer": m_to_km,
    "Meter to Miles": m_to_miles,
    "Miles to Meter": miles_to_m,
}

listbox = Listbox(height=5)
options = [
    "Kilometer to Miles",
    "Kilometer to Meter",
    "Meter to Kilometer",
    "Meter to Miles",
    "Miles to Kilometer",
    "Miles to Meter",
]
for item in options:
    listbox.insert(options.index(item), item)
listbox.grid(column=0, row=1)

window.mainloop()
