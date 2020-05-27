from tkinter import *
from datetime import date, datetime


def copy_values():
    current_time = datetime.now().time()
    with open("getval.txt", "a") as getval:
        getval.write(str(f'\n{current_time} : {data_name.get()} {data_surname.get()}'
                         f' {data_phone.get()} {data_address.get()}'))


window_1 = Tk()

# Добавляем название окна(програмы)
window_1.title('Notepad')
window_1.geometry('250x300')

name = Label(window_1, text="Enter your name", font=("Arial Bold", 12)).grid(column=0, row=0)
data_name = Entry(window_1, width=20)
data_name.grid(row=1, column=0)

surname = Label(window_1, text="Enter your surname", font=("Arial Bold", 12)).grid(column=0, row=2)
data_surname = Entry(window_1, width=20)
data_surname.grid(row=3, column=0)

phone = Label(window_1, text=" Enter your number phone", font=("Arial Bold", 12)).grid(column=0, row=4)
data_phone = Entry(window_1, width=20)
data_phone.grid(row=5, column=0)

address = Label(window_1, text="Enter your address", font=("Arial Bold", 12)).grid(column=0, row=6)
data_address = Entry(window_1, width=20)
data_address.grid(row=7, column=0)

# Add enter windows to needed location
# for r in range(1, 9, 2):
#     txt = Entry(window_1, width=20)
#     txt.grid(row=r, column=0)

btn = Button(window_1,
             command=copy_values,
             text="Save your info"
             )
btn.grid(column=0, row=8)


window_1.mainloop()
