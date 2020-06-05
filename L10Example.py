from tkinter import *
import requests
import os


def copy_reference():
    r = requests.get(data_ref.get())  # https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_960_720.jpg
    name = os.path.basename(data_ref.get())
    pf = path_to_file.get()
    nf = name_to_file.get()

    # Check empty entry path_to_file
    if not pf:
        pass
    elif path_to_file.get() == path_to_file.get():
        os.makedirs(pf)

    if not nf:
        if not pf:
            with open(f'{name}', 'wb') as file:
                file.write(r.content)
        if pf == pf:
            with open(f'{pf}/{name}', 'wb') as file:
                file.write(r.content)
    elif nf == nf:
        if not pf:
            with open(f'{nf}', 'wb') as file:
                file.write(r.content)
        if pf == pf:
            with open(f'{pf}/{nf}', 'wb') as file:
                file.write(r.content)

    
root = Tk()

# Добавляем название окна(програмы)
root.title('Save_File')
root.geometry('600x500')

reference = Label(root, text="Enter your reference", font=("Arial Bold", 12)).grid(row=0, column=0)
data_ref = Entry(root, width=80)
data_ref.grid(row=1, column=0)

Path_for_save = Label(root, text="Path to file", font=("Arial Bold", 12)).grid(row=2, column=0)
path_to_file = Entry(root, width=80)
path_to_file.grid(row=3, column=0)

Name_file = Label(root, text="Filename", font=("Arial Bold", 12)).grid(row=4, column=0)
name_to_file = Entry(root, width=80)
name_to_file.grid(row=5, column=0)
btn = Button(root,
             command=copy_reference,
             text="Save"
             )
btn.grid(column=0, row=8)

root.mainloop()
