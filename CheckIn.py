import sys
from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
import tkinter.ttk as ttk
con = sql.connect("skiSlopeDatabase11.db")
cur = con.cursor()


class UI():  # UI layer

    def __init__(self, main):

        # frame setup
        self.main = main  # Defining the window as "main"
        self.main.title("Check In")  # Giving the form a title
        self.main.geometry("300x200")  # Setting the dimensions of the window

        self.frame1 = Frame(main)
        self.frame1.pack()
        self.frame2 = Frame(main)
        self.frame2.pack()
        self.frame3 = Frame(main)
        self.frame3.pack()
        self.frame4 = Frame(main)
        self.frame4.pack()
        self.frame5 = Frame(main)
        self.frame5.pack()
        self.frame6 = Frame(main)
        self.frame6.pack()
        self.frame7 = Frame(main)

        # customer id entry search box

        self.customerIdLabel = Label(self.frame1, text='Customer ID')
        self.customerIdLabel.pack(side=LEFT)
        self.customerIdEntry = Entry(self.frame1)
        self.customerIdEntry.pack(side=RIGHT)



        self.customerFname = Label(self.frame2, text='First Name')
        self.customerFname.pack(side=LEFT)
        self.customerSname = Label(self.frame3, text='Surname')
        self.customerSname.pack(side=LEFT)
        self.sessionDate = Label(self.frame4, text='Session Date')
        self.sessionDate.pack(side=LEFT)
        self.sessionTime = Label(self.frame5, text='Session Time')
        self.sessionTime.pack(side=LEFT)
        self.checkIn = Label(self.frame6, text='Checked In')
        self.checkIn.pack(side=LEFT)
        #self.CheckIn = Button(self.frame1, text='Check In',)
        #self.CheckIn.pack(side=RIGHT)


class Controller:
    def __init__(self):
        # Controller class, initiates the GUI window
        main = Tk()
        menu = UI(main)
        main.mainloop()



Controller()  # Call controller to initiate window