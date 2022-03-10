from tkinter import *
import sqlite3


# connection to database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# empty lists to append later
number = []
patients = []

sql = "SELECT * FROM appointments"
res = c.execute(sql)
for r in res:
    ids = r[0]
    name = r[1]
    number.append(ids)
    patients.append(name)


# window
class Application:
    def __init__(self, master):
        self.master = master

        self.x = 0
        self.left = Frame(master, width=800, height=720, bg='lightgreen')
        self.left.pack(fill=BOTH)
        # heading
        self.heading = Label(master, text="Appointments", font=('Courier 60 bold'), fg='navy blue',bg='lightgreen')
        self.heading.place(x=370, y=0)
        self.token = Label(master, text="Token No: ", font=('Courier 30 bold'), fg='red', bg='lightgreen')
        self.token.place(x=300, y=200)
        self.tname = Label(master, text="Name: ", font=('Courier 30 bold'), fg='red', bg='lightgreen')
        self.tname.place(x=390, y=440)

        # button to change patients
        self.change = Button(master, text="Next Patient", width=50, height=2, bg='steelblue',font="courier 20 bold" ,command=self.func)
        self.change.place(x=300, y=600)

        # empty text labels to later config
        self.n = Label(master , font=('courier 200 bold'),bg='lightgreen')
        self.n.place(x=550, y=100)

        self.pname = Label(master, font=('courier 50 bold'),bg='lightgreen')
        self.pname.place(x=550, y=400)


    def func(self):
        self.n.config(text=str(number[self.x]))
        self.pname.config(text=str(patients[self.x]))


        print(str(number[self.x]))
        print(str(patients[self.x]))
        self.x += 1

def mainfile():
    root = Tk()
    b = Application(root)
    root.title("Appointment Serial")
    root.geometry("1366x768+0+0")
    root.resizable(False, False)
    root.mainloop()