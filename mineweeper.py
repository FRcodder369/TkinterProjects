from tkinter import *
import random


def choose_mines():
    mines = []
    for x in range(5):
        i = random.randrange(5)
        j = random.randrange(5)
        while (i, j) in mines:
            i = random.randrange(5)
            j = random.randrange(5)
        mine = (i, j)
        mines.append(mine)

    return mines

mines = choose_mines()



def press_button(i, j):
    global mines
    if (i, j) in mines:
        for x in mines:
            row, col = x
            buttons[row][col].config(text="💣")

    else:
        buttons[i][j].config(text='X')

    if empty():
        screen_lable.config(text="you won")



def empty():
    global mines
    for row in range(5):
        for col in range(5):
            if (row, col) not in mines:
                if buttons[row][col]['text'] == '':
                    return False
    return True



window = Tk()


buttons = [[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]

frame = Frame(window)
frame.pack()

for row in range(5):
    for col in range(5):
        buttons[row][col] = Button(frame, text='', width=10, height=5, font=('Arial', 15), fg='red',
                                   command=lambda row=row, col=col: press_button(row, col))
        buttons[row][col].grid(row=row, column=col)

screen_lable = Label(window, font=('Arial', 15), fg='red')
screen_lable.pack()

window.mainloop()
