from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
repetitions = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    checkmarks.config(text="")
    global repetitions
    repetitions = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global repetitions
    repetitions += 1

    if repetitions % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif repetitions % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60) if len(str(math.floor(count / 60))
                                              ) >= 2 else f"0{math.floor(count / 60)}"
    count_sec = count % 60 if count % 60 != 0 else "00"

    canvas.itemconfig(timer_text, text=f"{count_min}: {count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(repetitions/2)
        for _ in range(work_sessions):
            marks += CHECKMARK
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.grid_rowconfigure([0, 1, 2, 3, 4], pad=20)
window.grid_columnconfigure([0, 1, 2, 3, 4], pad=20)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW,
                    font=(FONT_NAME, 36, "bold"))
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", font=(FONT_NAME, 24, "bold"), fill="white")
canvas.grid(row=1, column=1)

start_button = Button(text="Start", bg="white", font=(
    FONT_NAME, 8, "italic"), border=1, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg="white", font=(
    FONT_NAME, 8, "italic"), border=1, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

checkmarks = Label(fg=GREEN, bg=YELLOW,
                   font=(FONT_NAME, 12, "bold"))
checkmarks.grid(row=3, column=1)

window.mainloop()
