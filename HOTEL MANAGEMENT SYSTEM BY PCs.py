from distutils.cmd import Command
from tkinter import *
import tkinter
from tkinter import messagebox
from PIL import Image 
from PIL import ImageTk
from  cutomer import customers
from room import RoomBooking
from details import DetailsRoom
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import Tk, Button


class hotelmangsys():
    def __init__ (self,root):
        self.root=root
        self.root.title("Hotel Management system")
        self.root.geometry("863x475+220+70")
             
    
        
      



        lab_tit=Label(text="WELCOME TO OUR \nHOTEL MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,width=40)
        lab_tit.place(x=0,y=0)


        self.root=Frame(bd=4,relief=RIDGE)
        self.root.place(x=0,y=99,width=860,height=660)
#..................Button.......
        book=Button(self.root,text="Customer",command=self.custdetails,width=13,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        book.grid(column=8,row=2,pady=1)

        room=Button(self.root,text="Room",command=self.roombooking,width=13,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        room.grid(column=8,row=3,pady=1)
#syntax Button(win, text="Button-1",height= 5, width=10).pack()

        roomser=Button(self.root,command=self.detailsroom,text="Details",width=13,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        roomser.grid(column=8,row=4,pady=1)

        Payment=Button(self.root,command=self.showinfo,text="Report",width=13,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        Payment.grid(column=8,row=5,pady=1)

        
        
        
        record=Button(self.root,text="Menu",width=15,font=("times new roman",13,"bold"),bg="black",fg="gold",bd=0,height=2,cursor="hand1")
        record.grid(column=8,row=0,pady=1)
        
        

#..............photframe.......
        logo_frame=Frame(bd=4,relief=RIDGE)
        logo_frame.place(x=150,y=99,width=739,height=388)
#............ee dept..................
        image1=Image.open("D:/BESE26/Summer Semester/DSA/Project/mcslogo.png")
        image1=image1.resize((710,370),Image.ANTIALIAS)
        test=ImageTk.PhotoImage(image1)
        bgImage=tkinter.Label(image=test)
        bgImage.image=test
        bgImage.place(x=150,y=99)
#.........mcs logo........
        image2=Image.open("D:/BESE26/Summer Semester/DSA/Project/mcslogo1.jpg")
        image2=image2.resize((140,140),Image.ANTIALIAS)
        test=ImageTk.PhotoImage(image2)
        bgImage=tkinter.Label(image=test)
        bgImage.image=test
        bgImage.place(x=5,y=315)
        

    def custdetails(self):
        self.new_window=Toplevel(self.root)
        self.app=customers(self.new_window)
        
    def roombooking(self):
            self.new_window=Toplevel(self.root)
            self.app=RoomBooking(self.new_window)
    def detailsroom(self):
            self.new_window=Toplevel(self.root)
            self.app=DetailsRoom(self.new_window)   
        
    def showinfo(self):
             messagebox.showinfo("Hello","\t\t\t\t\t\t\t\tDescription\nIn this project we are going to create a gui based python project which will help a hotel to keep records of newly entered people and the rooms alloted to them.\nThe project will use ‘mysql’ database to store the entries for future use.\n\t\t\t\t\t\t\t\tDeliverables\n\tThe project will have features of :\nLogin system\nHome  \nCustomer \nRoom booking \nDetails \nLogout\n\t\t\t\t\t\t\t\tUses\nThe home page will contain \nMenu\nCustomer tBooking\nAdding new room\nReport\nLogout\n\t\t\t\t\t\t\t\t\n\nCustomer details:\nThis page will show the details of the customers like \nName of customer\nMother’s name\nGender\nMobile no\nCnic no \nIt will also enable the admin of the system to update or delete a customer’s record\nIt will allow admin to search a customer through certain filters\nThe customer details page will also have option of ‘adding a new customer’\n\nBooking \nThis page will allow admin to allot a room to a customer\nIt will ask for the admin details to identify a admin\nIt will allow to update, delete a customer etc \n\nAdding a new room\n This page will allow admin to add more rooms to the system\nIt will ask for necessary details of the room and then add it to the system\nIt will allow to update, delete a room etc\n\t\t\t\t\t\t\t\tDetails:\n\nThis seciton will provide some kind of admin manual which will have all of the necessary details about the system which a new admin needs to know in order to use the system\n\t\t\t\t\t\t\t\tSoftware Requirements:\nPython\nPython IDE ( most preferably VS Code)\nMySql database\nA SQL server\nPython Libraries like Tkinter and Pymysql\n\t\t\t\t\t\t\t\tDeadline :\n\n As per requirements of the semester due time, the project have to be completed in a due month of about 4-5 weeks( insha allah)\n",parent=self.root) 
        


    
    
if __name__ == "__main__":
    root=Tk()
    obj=hotelmangsys(root)
    root.mainloop()
