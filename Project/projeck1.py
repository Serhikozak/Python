from tkinter import *
import random
from datetime import datetime

count = 0
temp = 0
after_id = ''


class Mainwindow:
    def __init__(self, master):

        self.label_root = Label(master, width=5, font=('Ubuntu', 40), text='00:00')
        self.label_root.grid(row=10, column=0)
        self.enter_str = Entry(master, width=30)
        self.enter_str.grid(row=7, column=0)
        self.enter_str.bind('<Return>', self.stop_countdown)
        self.enter_str.bind('<BackSpace>', self.press_backspace)
        self.start_btn = Button(master,
                                text="Start",
                                width=17,
                                height=1,
                                bd=3,
                                fg='violet',
                                font=("Verdana", 14, "bold"),
                                command=self.line_label)
        self.start_btn.grid(row=8, column=0)

    def tick(self):
        global temp, after_id
        after_id = root.after(1000, self.tick)
        f_temp = datetime.fromtimestamp(temp).strftime('%M : %S')
        self.label_root.configure(text=str(f_temp))
        temp += 1

    def line_label(self):
        line = random.choice(open('Lyrics.txt').readlines())  #  in case if Entry is working no correct
        self.tick()
        return Label(text=line, font=('Arial', 15)).grid(column=0, row=0)

    def press_backspace(self, event):
        global count
        count = count + 1
        return Label(text=f'Backspace was clicked {count} times!!!', font=('Arial', 14, 'bold')).grid(column=0, row=12)

    def stop_countdown(self, event):
        root.after_cancel(after_id)


root = Tk()
root.title('Check correct enter')
root.geometry('250x300')

app = Mainwindow(root)

root.mainloop()

