from tkinter import *
import datetime


def update():
    clock = datetime.datetime.now().strftime("%I:%M:%S %p")
    clock_lable.config(text=clock)

    day = datetime.datetime.now().strftime('%A')
    day_lable.config(text=day)

    date = datetime.datetime.now().strftime('%B %d, %Y')
    date_lable.config(text=date)

    window.after(1000, update)



window = Tk()

clock_lable = Label(window, text="", font=("Arial", 50), fg='green', bg='black')
clock_lable.pack()

day_lable = Label(window, text="", font=("Arial", 25))
day_lable.pack()

date_lable = Label(window, text="", font=("Arial", 24))
date_lable.pack()


update()
window.mainloop()