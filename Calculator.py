from tkinter import *

def press_button(num):
    global equation
    equation += str(num)
    equation_variable.set(equation)

def equals():
    global equation
    try:
        result = eval(equation)
        equation_variable.set(result)
    except ZeroDivisionError:
        equation = ''
        equation_variable.set('arithmetic error')
    except SyntaxError:
        equation = ''
        equation_variable.set('syntax error')

def clear():
    global equation
    equation = ''
    equation_variable.set(equation)


window = Tk()
window.title('Calculator')
window.geometry('500x500')

equation = ''
equation_variable = StringVar()

screen = Label(window, textvariable=equation_variable, font=('Arial', 20), width=18, bg='white', height=1)
screen.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, font=('Arial', 18), bg='white', fg='black', width=2, height=1,
                 command= lambda :press_button(1))
button1.grid(row=0, column=0, padx=5, pady=5)

button2 = Button(frame, text=2, font=('Arial', 18), bg='white', fg='black', width=2, height=1,
                 command= lambda :press_button(2))
button2.grid(row=0, column=1, padx=5, pady=5)

button3 = Button(frame, text=3, font=('Arial', 18), bg='white', fg='black', width=2, height=1,
                 command= lambda :press_button(3))
button3.grid(row=0, column=2, padx=5, pady=5)

button4 = Button(frame, text=4, font=('Arial', 18), bg='white', fg='black', width=2, height=1,
                 command= lambda :press_button(4))
button4.grid(row=1, column=0, padx=5, pady=5)

button5 = Button(frame, text=5, font=('Arial', 18), bg='white', fg='black', width=2, height=1,
                 command= lambda :press_button(5))
button5.grid(row=1, column=1, padx=5, pady=5)

button6 = Button(frame, text=6, font=('Arial', 18), bg='white', fg='black', width=2, height=1,
                 command= lambda :press_button(6))
button6.grid(row=1, column=2, padx=5, pady=5)

button7 = Button(frame, text=7, font=('Arial', 18), bg='white', fg='black', width=2, height=1,
                 command= lambda :press_button(7))
button7.grid(row=2, column=0, padx=5, pady=5)

button8 = Button(frame, text=8, font=('Arial', 18), bg='white', fg='black', width=2, height=1,
                 command= lambda :press_button(8))
button8.grid(row=2, column=1, padx=5, pady=5)

button9 = Button(frame, text=9, font=('Arial', 18), bg='white', fg='black', width=2, height=1,
                 command= lambda :press_button(9))
button9.grid(row=2, column=2, padx=5, pady=5)

button0 = Button(frame, text=0, font=('Arial', 18), bg='white', fg='black', width=2, height=1,
                 command= lambda :press_button(0))
button0.grid(row=3, column=1, padx=5, pady=5)

plus = Button(frame, text='+', font=('Arial', 18), bg='white', fg='black', width=2, height=1,
              command= lambda :press_button('+'))
plus.grid(row=0, column=3, padx=5, pady=5)

minus = Button(frame, text='-', font=('Arial', 18), bg='white', fg='black', width=2, height=1,
              command= lambda :press_button('-'))
minus.grid(row=1, column=3, padx=5, pady=5)

devision = Button(frame, text='/', font=('Arial', 18), bg='white', fg='black', width=2, height=1,
              command= lambda :press_button('/'))
devision.grid(row=2, column=3, padx=5, pady=5)

dot = Button(frame, text='.', font=('Arial', 18), bg='white', fg='black', width=2, height=1,
              command= lambda :press_button('.'))
dot.grid(row=3, column=0, padx=5, pady=5)

multiply = Button(frame, text='*', font=('Arial', 18), bg='white', fg='black', width=2, height=1,
              command= lambda :press_button('*'))
multiply.grid(row=3, column=2, padx=5, pady=5)

equal = Button(frame, text='=', font=('Arial', 18), bg='white', fg='black', width=2, height=1,
              command=equals)
equal.grid(row=3, column=3, padx=5, pady=5)

clear_button = Button(window, text='clear', font=('Arial', 18), bg='white', fg='black', height=1,
               command=clear)
clear_button.pack()



window,mainloop()