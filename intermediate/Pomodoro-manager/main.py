from tkinter import *
from tkinter.ttk import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = "✔"
reps = 0
updated_checks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global updated_checks
    global reps

    start_btn.config(state="normal")
    reset_btn.config(state="disabled")

    window.after_cancel(timer)
    timer_lbl.config(text="TIMER", foreground=GREEN)
    canvas.itemconfig(timer_txt, text="00:00")
    updated_checks = ""
    check_lbl.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global updated_checks
    start_btn.config(state="disabled")
    reset_btn.config(state="normal")
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        countdown(work_sec)
        timer_lbl.config(
            text="Work!",
            foreground=GREEN,
        )
        reps += 1
    elif reps % 2 != 0 and reps != 7:
        countdown(short_sec)
        timer_lbl.config(
            text="Rest!",
            foreground=PINK,
        )
        updated_checks += CHECK
        check_lbl.config(text=updated_checks)
        reps += 1
    elif reps == 7:
        countdown(long_sec)
        timer_lbl.config(
            text="Rest more!",
            foreground=RED,
        )
        reps = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer

    count_min = count // 60
    if int(count_min) < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if int(count_sec) < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        window.state("normal")  # Restore if window is minimized
        window.attributes("-topmost", 1)  # Bring to top level above all windows
        window.attributes("-topmost", 0)  # Allows other windows to top level again
        window.bell()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg=YELLOW)


timer_lbl = Label(
    text="TIMER", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 40, "bold")
)
timer_lbl.grid(row=0, column=1)

check_lbl = Label(
    text="", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 14, "bold")
)
check_lbl.grid(row=3, column=1)


canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
img = PhotoImage(file="intermediate/Pomodoro-manager/tomato.png")
canvas.create_image(100, 112, image=img)
timer_txt = canvas.create_text(
    100, 132, text="00:00", fill="white", font=(FONT_NAME, 30, "bold")
)
canvas.grid(row=1, column=1)

start_btn = Button(text="start", command=start_timer, state="normal")
start_btn.grid(row=2, column=0)

reset_btn = Button(text="reset", command=reset_timer, state="disabled")
reset_btn.grid(row=2, column=2)

window.mainloop()
