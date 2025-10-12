from tkinter import *

def submit():
    username = name_entry.get()
    age = age_entry.get()
    degree = degree_entry.get()
    job = job_entry.get()

    data_list = [username, age, degree, job]
    if '' in data_list:
        print('fill all parts')

    else:
        with open('userInfo.txt', 'w') as file:
            for i in range(4):
                file.write(data_list[i] + '\n')



window = Tk()
window.title('Save User Info')
window.geometry('500x500')
frame = Frame(window)
frame.pack()

name_lable = Label(frame, text="Name", font=("Helvetica",15))
name_lable.grid(row=0, column=0)

name_entry = Entry(frame, font=("Helvetica",12), fg='blue', width=20)
name_entry.grid(row=0, column=1)


age_lable = Label(frame, text="Age", font=("Helvetica",15))
age_lable.grid(row=1, column=0)

age_entry = Entry(frame, font=("Helvetica",12), fg='blue', width=20)
age_entry.grid(row=1, column=1)


degree_lable = Label(frame, text="Degree", font=("Helvetica",15))
degree_lable.grid(row=2, column=0)

degree_entry = Entry(frame, font=("Helvetica",12), fg='blue', width=20)
degree_entry.grid(row=2, column=1)


job_lable = Label(frame, text="Job", font=("Helvetica",15))
job_lable.grid(row=3, column=0)

job_entry = Entry(frame, font=("Helvetica",12), fg='blue', width=20)
job_entry.grid(row=3, column=1)


submit_button = Button(window, text="Save", font=("Helvetica",15), fg='red', command=submit)
submit_button.pack()

window.mainloop()