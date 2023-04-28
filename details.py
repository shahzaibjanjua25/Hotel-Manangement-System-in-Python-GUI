from ast import Pass
from email.mime import message
from ipaddress import collapse_addresses
from msilib import text
from pickletools import TAKEN_FROM_ARGUMENT1
from tkinter import *
from webbrowser import get
import mysql.connector
import tkinter
import random
from tkinter.tix import COLUMN
from PIL import Image 
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from time import strftime
from datetime import datetime


class DetailsRoom :
    def __init__ ( self , root ) :
        self.root = root
        self.root.title ( " Hospital Management Systen " )
        self.root.geometry ( "1200x556" )
        
        #title
        
        lbl_title=Label(self.root,text="Room Booking Details",font=("times new roman",18,"bold"),bg="black",fg="white")  
        lbl_title.place(x=1,y=0,width=1198,height=50)
        #label
        lbFrm2=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",padx=2,font=("times new roman",12,"bold"))
        lbFrm2.place(x=5,y=50,width=540,height=380)
        
        #==========label and entry
        lbfloor=Label(lbFrm2,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbfloor.grid(row=0,column=0)  
        #variables
        self.var_floor=StringVar()
        
        efloor=ttk.Entry(lbFrm2,textvariable=self.var_floor,font=("arial",12,"bold"),width=20)
        efloor.grid(row=0,column=1,sticky=W)
        # Room No
        lb1_RoomNo = Label ( lbFrm2,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        lb1_RoomNo.grid ( row = 1 , column = 0 , sticky = W , padx = 20 )
        self.var_roomNo=StringVar()                          
        enty_RoomNo=ttk.Entry ( lbFrm2,textvariable=self.var_roomNo, font = ( " arial " , 13 , " bold") , width = 20 )
        enty_RoomNo.grid ( row = 1 , column = 1 , sticky = W )
        #Room Type
        lb1_RoomType=Label(lbFrm2,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lb1_RoomType.grid (row=2,column=0,sticky=W,padx=20)
        self.var_roomType=StringVar() 
        enty_RoomType=ttk.Entry(lbFrm2,textvariable=self.var_roomType,font=("arial",13,"bold"),width=20)
        enty_RoomType.grid(row=2,column=1,sticky=W)
        
        
        enty_RoomType.grid(row=2,column=1,sticky=W)
                     #==== btns =====
        btn_frame =Frame(lbFrm2,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=378,height=40)
        btnAdd=Button(btn_frame,command=self.add_data,text="Add",font=("arial",11,"bold"),bg="black",fg="white",width=9)
        btnAdd.grid(row=0,column=0,padx=1)
        btnUpadate=Button(btn_frame,command=self.update,text="Update",font=("arial",11,"bold"),bg="black",fg="white",width=9)
        btnUpadate.grid(row=0,column=1,padx=1)
        btnDelete=Button(btn_frame,command=self.delete,text="Delete",font=("arial",11,"bold"),bg="black",fg="white",width=9)
        btnDelete.grid(row=0,column=2,padx=1)
        btnreset=Button(btn_frame,command=self.reset,text="Reset",font=("arial",11,"bold"),bg="black",fg="white",width=9)
        btnreset.grid(row=0,column=3,padx=1) 
        
        lbFrmR2=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",padx=2,font=("times new roman",12,"bold"))
        lbFrmR2.place(x=600,y=55,width=600,height=350)
        
        #scrool bar
        scbarx=ttk.Scrollbar(lbFrmR2,orient=HORIZONTAL)
    
        scbary=ttk.Scrollbar(lbFrmR2,orient=VERTICAL)
        self.details_table=ttk.Treeview(lbFrmR2,columns=("Floor","RoomNo","roomtype"),xscrollcommand=scbarx.set)
    
        #self.details_table=ttk.Treeview(lbFrmR2,columns=("Floor","RoomNo","roomtype"),yscrollcommand=scbary.set)
    
        scbarx.pack(side=BOTTOM,fill=X)
        scbary.pack(side=RIGHT,fill=Y)
    
        scbarx.config(command=self.details_table.xview)
        scbary.config(command=self.details_table.yview)
        
        self.details_table.heading("Floor",text="Floor")
        self.details_table.heading("RoomNo",text="Room No")
        self.details_table.heading("roomtype",text="Room Type")
        
        self.details_table["show"]="headings"
        
        self.details_table.column("Floor",width=100)
        self.details_table.column("RoomNo",width=100)
        self.details_table.column("roomtype",width=100)

        
        self.details_table.pack(fill=BOTH,expand=1)
        self.details_table.bind ( "<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()
        
    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomType.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root) 
        else:
         try:
             


            conn = sqlite3.connect('mcsdb1.db')
            c=conn.cursor()

            c.execute("insert into details (Floor,RoomNo,RoomType) values(?,?,? )",(
                                                                    self.var_floor.get(),
                                                                    self.var_roomNo.get(),
                                                                    self.var_roomType.get()
                                                                    
                                                            
                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","New Room added successfully",parent=self.root)
         except Exception as es:
            messagebox.showwarning("warning",f"Something went wrong:{str(es)}",parent=self.root) 
     #========fetch data=====\
    def fetch_data(self):
             


            conn = sqlite3.connect('mcsdb1.db')
            c=conn.cursor()  
            c.execute("select * from details")   
            rows=c.fetchall()
            if len(rows)!=0:
              self.details_table.delete(*self.details_table.get_children())
              for i in rows:
                  self.details_table.insert("",END,values=i)
              conn.commit()
              conn.close() 
    def get_cursor(self,event=""):
        cursor_row=self.details_table.focus()
        cont=self.details_table.item(cursor_row)
        row=cont["values"]
        
        self.var_floor.set(row[0]),
        self.var_roomNo.set(row[1]),
        self.var_roomType.set(row[2])
     
        
    def update(self):
            if self.var_floor.get()=="":
                messagebox.showerror("Error","Please enter room number",parent=self.root)
            else:
                    
                
                 
                conn = sqlite3.connect('mcsdb1.db')
                c=conn.cursor()  
                c.execute("update details set Floor=?,RoomType=? where RoomNo=?",(
                                                                    
                                                                    
                                                                    self.var_floor.get(),
                                                                    
                                                                    self.var_roomType.get(),
                                                                    self.var_roomNo.get()

                    
                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Updated Successfully",parent=self.root)
          
    def delete(self):
         delete=messagebox.askyesno("Hotel Management System", "Do YOU want to delte room details",parent=self.root)
         if delete>0:
             


            conn = sqlite3.connect('mcsdb1.db')
            c=conn.cursor()   
            query="delete from details where RoomNO=?" 
            value=(self.var_roomNo.get(),)
            c.execute(query,value)
         else:
          if not delete:
             return
          conn.commit()
         self.fetch_data()
         conn.close()
    def reset(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_roomType.set("")
                               
                     

if __name__ == "__main__":
    root = Tk()
    obj= DetailsRoom(root)
    root.mainloop()