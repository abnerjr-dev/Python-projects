from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import random as r
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
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
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    pass_list = []

    [pass_list.append(r.choice(letters)) for _ in range(r.randint(8, 10))]
    [pass_list.append(r.choice(symbols)) for _ in range(r.randint(2, 5))]
    [pass_list.append(r.choice(numbers)) for _ in range(r.randint(2, 5))]

    r.shuffle(pass_list)

    password = "".join(pass_list)

    if password_input.get() == "":
        password_input.insert(0, password)
    else:
        password_input.delete(0, END)
        password_input.insert(0, password)
    password_input.clipboard_clear()
    password_input.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_input.get()
    email = user_input.get()
    password = password_input.get()
    new_data = {website: {"email": email, "password": password}}

    if (
        website_input.get() != ""
        and password_input.get() != ""
        and user_input.get() != ""
    ):
        is_ok = messagebox.askokcancel(
            title=website_input.get(),
            message=f"This is the information entered: \nEmail: {email} \nPassword: {password} \nIs it Ok to save?",
        )
        if is_ok:
            try:
                with open("intermediate/password-manager-app/data.json", "r") as file:
                    data = json.load(file)  # read the old data
                    data.update(new_data)  # update it
            except:
                with open("intermediate/password-manager-app/data.json", "w") as file:
                    json.dump(new_data, file, indent=4)  # save the update to json file
            else:
                with open("intermediate/password-manager-app/data.json", "w") as file:
                    json.dump(data, file, indent=4)  # save the update to json file
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()
    else:
        pop_up()


def pop_up():
    popup = Toplevel()
    popup.title("!!!!!!!!!!!!")
    label = Label(popup, text="You forgot to fill all the information!")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Ugh, Fine!", command=popup.destroy)
    B1.pack()
    popup.mainloop()


def search():
    website = website_input.get()
    try:
        with open("intermediate/password-manager-app/data.json", "r") as file:
            data = json.load(file)
            print(data[website])
        
    except KeyError:
        messagebox.showerror(title="Error", message="No Data Found.")

    else:
        messagebox.showinfo(title= website, message=f"email: {data[website]["email"]} \npassword: {data[website]["password"]}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "dark")

# canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="intermediate/password-manager-app/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels
website_lbl = Label(text="Website:")
website_lbl.grid(row=1, column=0, sticky="E")

user_lbl = Label(text="Email/Username:")
user_lbl.grid(row=2, column=0, sticky="E")

password_lbl = Label(text="Password:")
password_lbl.grid(row=3, column=0, sticky="E")

# entries
website_input = Entry()
website_input.focus()
website_input.grid(row=1, column=1, columnspan=1, sticky="WE")

user_input = Entry()
user_input.insert(0, "barbosa5@msu.edu")
user_input.grid(row=2, column=1, columnspan=2, sticky="WE")

password_input = Entry()
password_input.grid(row=3, column=1, sticky="WE")

# buttons
password_btn = Button(text="Generate Password", command=generate_password)
password_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=50, command=add_password)
add_btn.grid(row=4, column=1, columnspan=2)

search_btn = Button(text="Search", command=search)
search_btn.grid(row=1, column=2, sticky="WE")

window.mainloop()
