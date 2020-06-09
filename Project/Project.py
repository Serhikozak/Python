from tkinter import *
import random

#  line = random.choice(open('Lyrics.txt').readlines())  #  in case if Entry is working no correct

count = 0


def return_val():
    window = Toplevel(root)
    # lbox = Listbox(window, width=60)
    # lbox.pack()
    return Listbox(width=60)  #(width=60).pack()


class Mainwindow:
    def __init__(self, master):
        self.master = master

        # lb = Listbox(self)
        self.master.title('check enter text')
        # self.label1 = Label(master).grid(column=0, row=1)
        #  label1.grid(column=0, row=1).grid(column=0, row=1)
        self.enter_str = Entry(master, width=20)
        self.enter_str.grid(row=7, column=0)
        self.enter_str.bind('<BackSpace>', self.press_btn)
        self.start_btn = Button(master, text="start")
        self.start_btn.grid(row=8, column=0)
        self.start_btn.bind('<Button-1>', self.start)
        self.score_Btn = Button(text="Score", command=return_val)
        self.score_Btn.grid(row=9, column=0)

    def press_btn(self, event):
        global count
        count = count + 1
        return Label(text=f'Backspace was clicked {count} times!!!', font=("Arial Bold", 12)).grid(column=0, row=10)

    def start(self, event):
        line = random.choice(open('Lyrics.txt').readlines())
        return Label(text=line, font=("Arial Bold", 12)).grid(column=0, row=6)


root = Tk()
# Добавляем название окна(програмы)

root.geometry('250x300')

app = Mainwindow(root)



root.mainloop()

