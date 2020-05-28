from tkinter import *
from datetime import date, datetime


def copy_values():
    current_time = datetime.now().time()
    with open("getval.txt", "a") as getval:
        getval.write(f'\n{current_time} : {data_name.get()} {data_surname.get()}'
                     f' {data_phone.get()} {data_address.get()}')


def create_window():
    def clear_values():
        clearval = open("/home/vagrant/TaskPython/Python/getval.txt", "w")
        clearval.close()

    window = Toplevel(root)
    lbox = Listbox(window, width=60)
    lbox.pack()
    getval = open("/home/vagrant/TaskPython/Python/getval.txt")
    lbox.insert(END, getval.read())
    clear = Button(window,
                   command=clear_values,
                   text="Clear"
                   )
    clear.pack()


root = Tk()

# Добавляем название окна(програмы)
root.title('Notepad')
root.geometry('250x300')

name = Label(root, text="Enter your name", font=("Arial Bold", 12)).grid(column=0, row=0)
data_name = Entry(root, width=20)
data_name.grid(row=1, column=0)

surname = Label(root, text="Enter your surname", font=("Arial Bold", 12)).grid(column=0, row=2)
data_surname = Entry(root, width=20)
data_surname.grid(row=3, column=0)

phone = Label(root, text=" Enter your number phone", font=("Arial Bold", 12)).grid(column=0, row=4)
data_phone = Entry(root, width=20)
data_phone.grid(row=5, column=0)

address = Label(root, text="Enter your address", font=("Arial Bold", 12)).grid(column=0, row=6)
data_address = Entry(root, width=20)
data_address.grid(row=7, column=0)

# Add enter windows to needed location
# for r in range(1, 9, 2):
#     txt = Entry(window_1, width=20)
#     txt.grid(row=r, column=0)

btn = Button(root,
             command=copy_values,
             text="Save your info"
             )
btn.grid(column=0, row=8)
b = Button(root,
           text="My Contacts",
           command=create_window
           )
b.grid(column=0, row=9)


root.mainloop()
