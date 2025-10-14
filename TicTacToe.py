from tkinter import *

def press_cube(i, j):
    players_turn = turn()
    buttons[i][j]['text'] = players_turn

    status = over_win()






i = -1
def turn():
    global i
    i += 1
    if i % 2 == 0:
        return "X"
    else:
        return "O"

def over_win():
    if buttons[0][0]['text'] == buttons[0][1]['text'] == buttons[0][2]['text'] != '':
        buttons[0][0].config(bg='green')
        buttons[0][1].config(bg='green')
        buttons[0][2].config(bg='green')
        return buttons[0][0]['text']
    elif buttons[1][0]['text'] == buttons[1][1]['text'] == buttons[1][2]['text'] != '':
        buttons[1][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[1][2].config(bg='green')
        return buttons[1][0]['text']
    elif buttons[2][0]['text'] == buttons[2][1]['text'] == buttons[2][2]['text'] != '':
        buttons[2][0].config(bg='green')
        buttons[2][1].config(bg='green')
        buttons[2][2].config(bg='green')
        return buttons[2][0]['text']
    elif buttons[0][0]['text'] == buttons[1][0]['text'] == buttons[2][0]['text'] != '':
        buttons[0][0].config(bg='green')
        buttons[1][0].config(bg='green')
        buttons[2][0].config(bg='green')
        return buttons[0][0]['text']
    elif buttons[0][1]['text'] == buttons[1][1]['text'] == buttons[2][1]['text'] != '':
        buttons[0][1].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][1].config(bg='green')
        return buttons[0][1]['text']
    elif buttons[0][2]['text'] == buttons[1][2]['text'] == buttons[2][2]['text'] != '':
        buttons[0][2].config(bg='green')
        buttons[1][2].config(bg='green')
        buttons[2][2].config(bg='green')
        return buttons[0][2]['text']
    elif buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        buttons[0][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][2].config(bg='green')
        return buttons[0][0]['text']
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        buttons[0][2].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][0].config(bg='green')
        return True

buttons = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]



window = Tk()
window.title('TicTacToe')

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text='', font=('Arial', 15) , bg='white' , width= 10, height=3,
                                      command= lambda row=row, column=column: press_cube(row, column))
        buttons[row][column].grid(row=row, column=column)


status_button = Button(window, text='', font=('Arial', 15) , bg='white')
status_button.pack()



window.mainloop()