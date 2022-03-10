from display import *
from update import *
from tkinter import *
import sqlite3
import tkinter.messagebox



# connect to the databse.
conn = sqlite3.connect('database.db')
# cursor to move around the databse
c = conn.cursor()


ids = []


# tkinter window
class Application:
    def __init__(self, master):
        self.master = master

        # creating the frames in the master
        self.left = Frame(master, width=800, height=720, bg='lightgreen')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

        # labels for the window
        self.heading = Label(self.left, text="APOLLO Hospital Appointments", font=('Courier 35 bold'), fg='navy blue',
                             bg='lightgreen',borderwidth=3,relief=SUNKEN)
        self.heading.place(x=5, y=4)
        # patients name
        self.name = Label(self.left, text="Patient's Name", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.name.place(x=0, y=100)

        # age
        self.age = Label(self.left, text="Age", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.age.place(x=0, y=140)

        # gender
        self.gender = Label(self.left, text="Gender", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.gender.place(x=0, y=180)

        # location
        self.location = Label(self.left, text="Location", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.location.place(x=0, y=220)

        # appointment time
        self.time = Label(self.left, text="Appointment Time", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.time.place(x=0, y=260)

        # phone
        self.phone = Label(self.left, text="Phone Number", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.phone.place(x=0, y=300)

        # Entries for all labels============================================================
        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=250, y=110)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=150)

        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=250, y=190)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=230)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=250, y=270)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=310)

        # button to perform a command
        self.submit = Button(self.left, text="Add Appointment", width=40, height=2, bg='steelblue',
                             command=self.add_appointment,fg="lightgreen",font="courier 12 bold")
        self.submit.place(x=210, y=380)

        # getting the number of appointments fixed to view in the log
        sql2 = "SELECT ID FROM appointments "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        # ordering the ids

        self.final_id =len(ids)
        # displaying the logs in our right frame
        self.logs = Label(self.right, text="Logs", font=('Courier 28 bold'), fg='yellow', bg='steelblue')
        self.logs.place(x=150, y=0)

        self.box = Text(self.right, width=45, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END, "Total Appointments till now :  " + str(self.final_id))

    # funtion to call when the submit button is clicked
    def add_appointment(self):
        # getting the user inputs
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()

        # checking if the user input is empty
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            # now we add to the database
            sql = "INSERT INTO 'appointments' (name, age, gender, location, scheduled_time, phone) VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            tkinter.messagebox.showinfo("Successfully created", "Appointment for " + str(self.val1) + " has been created")

            self.box.insert(END, '\nAppointment fixed for ' + str(self.val1) + ' at ' + str(self.val5))

def displayapp():
    root.destroy()
    mainfile()
def updateapp():
    root.destroy()
    updatefile()
# creating the object
root = Tk()
b = Application(root)
root.title("Apollo Management System")

# resolution of the window
root.geometry("1200x720+0+0")

root.next = Button(root, text="Appointment serial", width=20, height=2, bg='steelblue',command=displayapp,fg="lightgreen",font="courier 12 bold")
root.next.place(x=100, y=500)

root.update = Button(root, text="Update Details", width=20, height=2, bg='steelblue',command=updateapp,fg="lightgreen",font="courier 12 bold")
root.update.place(x=490, y=500)
# preventing the resize feature
root.resizable(False, False)


# end the loop
root.mainloop()