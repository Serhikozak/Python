from tkinter import *
import random
import time

#  line = random.choice(open('Lyrics.txt').readlines())  #  in case if Entry is working no correct
from Xlib.protocol import event

count = 0
current_time = time.monotonic()


def return_val():
    window = Toplevel(root)
    # lbox = Listbox(window, width=60)
    # lbox.pack()
    return Listbox(width=60)  #(width=60).pack()


def line_label():
    line = random.choice(open('Lyrics.txt').readlines())
    return Label(text=line, font=("Arial Bold", 12)).grid(column=0, row=6)


# def at_the_beginning(event):
#     current_time = time.time()
#     return current_time


def press_backspace(event):
    global count
    count = count + 1
    return Label(text=f'Backspace was clicked {count} times!!!', font=("Arial Bold", 12)).grid(column=0, row=12)


class Mainwindow:
    def __init__(self, master):
        self.master = master
        # self.current_time = time.monotonic()
        # lb = Listbox(self)
        self.master.title('check enter text')
        # self.label1 = Label(master).grid(column=0, row=1)
        #  label1.grid(column=0, row=1).grid(column=0, row=1)
        self.enter_str = Entry(master, width=20)
        self.enter_str.grid(row=7, column=0)
        self.enter_str.bind('<Key>', self.at_the_beginning)
        self.enter_str.bind('<Return>', self.spend_time)
        self.enter_str.bind('<BackSpace>', press_backspace)
        self.start_btn = Button(master,
                                text="start",
                                command=line_label)
        self.start_btn.grid(row=8, column=0)

        self.score_Btn = Button(text="Score", command=return_val)
        self.score_Btn.grid(row=9, column=0)

    def at_the_beginning(self, event):

        return Label(text=current_time, font=("Arial Bold", 12)).grid(column=0, row=10)

    def spend_time(self, event):

        current_time2 = time.monotonic() - current_time
        # current_time3 = current_time2 - current_time

        return Label(text=float('{:.2f}'.format(current_time2)), font=("Arial Bold", 12)).grid(column=0, row=11)





class Start(Mainwindow):
    """Class to start of game"""
    def __init__(self, master, times):
        """Initiate start of game"""
        super().__init__(master)
        self.times = times


root = Tk()
# Добавляем название окна(програмы)

root.geometry('250x300')

app = Mainwindow(root)



root.mainloop()

