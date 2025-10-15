from tkinter import *
import datetime


def save():
    today_text = text.get('1.0', END)
    today_date = datetime.date.today()
    with open(f'{today_date}.txt', 'w') as f:
        f.write(today_text)

window = Tk()
window.title('Diary')
window.geometry('500x500')


text = Text(window, background='light yellow',
            fg='purple', font=('Segoe Script', 10), width=50, height=20)
text.pack()

save_button = Button(window, text='Save', command=save, fg='red', bg='pink', font=('Arial', 15))
save_button.pack()

window.mainloop()