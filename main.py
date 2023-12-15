import tkinter
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
repetitions = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    timer_label.config(text = "Timer")
    checkmarks_label.config(text = "")
    repetitions = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global repetitions
    work_duration = WORK_MIN * 60
    short_break_duration = SHORT_BREAK_MIN * 60
    long_break_duration = LONG_BREAK_MIN * 60
    repetitions += 1
    if repetitions % 8 == 0:
        timer_label.config(text = "Long Break", fg = RED)
        countdown(long_break_duration)
    elif repetitions % 2 == 0:
        timer_label.config(text = "Short Break", fg = PINK)
        countdown(short_break_duration)
    else:
        timer_label.config(text = "Work")
        countdown(work_duration)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    canvas.itemconfig(timer_text, text = f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        checkmark = ""
        work_sessions = math.floor(repetitions/2)
        for i in range(work_sessions):
            checkmark += "✓"
        checkmarks_label.config(text = f"{checkmark}")

# ---------------------------- UI SETUP ------------------------------- #
#Window
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

#Canvas
canvas = tkinter.Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = tkinter.PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)

#Labels
timer_label = tkinter.Label(text = "Timer", font = (FONT_NAME, 35, "bold"), fg = GREEN, bg = YELLOW)
timer_label.grid(row = 0, column = 1)

checkmarks_label = tkinter.Label(font = (FONT_NAME, 25, "bold"), fg = GREEN, bg = YELLOW)
checkmarks_label.grid(row = 3, column = 1)

#Buttons
start_button = tkinter.Button(text = "Start", font = (FONT_NAME, 12, "normal"), highlightthickness = 0, command = start_timer)
start_button.grid(row = 2, column = 0)

reset_button = tkinter.Button(text = "Reset", font = (FONT_NAME, 12, "normal"), highlightthickness = 0, command = timer_reset)
reset_button.grid(row = 2, column = 2)

window.mainloop()