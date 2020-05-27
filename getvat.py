from tkinter import *


def copy_values():
    return txt_name.get()
    return txt_surname.get()


window_1 = Tk()

window_1.title('Notepad')
window_1.geometry('250x300')
name = Label(window_1, text="Enter your name", font=("Arial Bold", 12))
name.grid(column=0, row=0)
surname = Label(window_1, text="Enter your surname", font=("Arial Bold", 12))
surname.grid(column=0, row=2)

txt_name = Entry(window_1, width=20)
txt_name.grid(column=0, row=1)
txt_surname = Entry(window_1, width=20)
txt_surname.grid(column=0, row=3)

btn = Button(window_1,
             text='Hi',
             command=copy_values,
             )
btn.grid(column=0, row=4)

copy_values()
with open("getval.txt", "a") as file:
    file.write(str(copy_values()))

window_1.mainloop()
