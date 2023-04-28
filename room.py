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

class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1200x550+20+20")
        lbl_title=Label(self.root,text="Billing Details",font=("times new roman",18,"bold"),bg="black",fg="white")  
        lbl_title.place(x=1,y=0,width=1198,height=50)
        #========variable=======
         
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        
        
         
         
        #label
        lbFrm2=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking details",padx=2,font=("times new roman",12,"bold"))
        lbFrm2.place(x=5,y=50,width=425,height=480)
        #lbFrm3=LabelFrame(self.root,bd=2,relief=RIDGE,text="Data",padx=2,font=("times new roman",12,"bold"))
        #lbFrm3.place(x=435,y=50,width=800,height=230)
        #custcontactFim
        
        lbl_cust_contact=Label(lbFrm2,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)  
        elb_cust=ttk.Entry(lbFrm2,textvariable=self.var_contact,font=("arial",12,"bold"),width=20)
        elb_cust.grid(row=0,column=1,sticky=W)
        
        #FeatchDataButton
        
        
       # FeatchDataButton=Button(lbFrm2,command=self.fetch_contact,text="Fetch Data",font=("arial",10,"bold"),bg="black",fg="white",width=9)
       # FeatchDataButton.place(x=335,y=4)
        
        #checkIndate
        checkin1=Label(lbFrm2,text="Check In Date",font=("arial",12,"bold"),padx=2,pady=6)
        checkin1.grid(row=1,column=0,sticky=W)  
        echeckin=ttk.Entry(lbFrm2,textvariable=self.var_checkin,font=("arial",12,"bold"),width=29)
        echeckin.grid(row=1,column=1) 
        #checoutdate
        checoutdate=Label(lbFrm2,text="Check out Date",font=("arial",12,"bold"),padx=2,pady=6)
        checoutdate.grid(row=2,column=0,sticky=W)  
        echecoutdate=ttk.Entry(lbFrm2,textvariable=self.var_checkout,font=("arial",12,"bold"),width=29)
        echecoutdate.grid(row=2,column=1,sticky=W) 
        #roomType
        roomtype=Label(lbFrm2,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        roomtype.grid(row=3,column=0,sticky=W)  
        eroomtype=ttk.Entry(lbFrm2,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27)
        eroomtype.grid(row=3,column=1,sticky=W) 
        
        
       ## combox_room["value"]=("Single","Double","Luxury")
        ##combox_room=ttk.Combobox(lbFrm2,font=("arial",12,"bold"),width=27,state="readonly")
       ## combox_room.current(0)
        
       # combox_room.grid(row=3,column=1,sticky=W) 
        #availableRoom 
        av_room=Label(lbFrm2,text="Room Available",font=("arial",12,"bold"),padx=2,pady=6)
        av_room.grid(row=4,column=0,sticky=W)  
         


        conn = sqlite3.connect('mcsdb1.db')
        c2=conn.cursor()  
        c2.execute("select RoomNo from details")   
        rows2=c2.fetchall()
        
        combox_roomNO=ttk.Combobox(lbFrm2,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=27,state="readonly")
        combox_roomNO["value"]=rows2
        combox_roomNO.grid(row=4,column=1) 
        
        #meal
        meal=Label(lbFrm2,text="Meal",font=("arial",12,"bold"),padx=2,pady=6)
        meal.grid(row=5,column=0,sticky=W)  
        emeal=ttk.Entry(lbFrm2,textvariable=self.var_meal,font=("arial",12,"bold"),width=29)
        emeal.grid(row=5,column=1,sticky=W) 
        #no of days
        NoOfDays=Label(lbFrm2,text="No Of Days",font=("arial",12,"bold"),padx=2,pady=6)
        NoOfDays.grid(row=6,column=0,sticky=W)  
        eNoOfDays=ttk.Entry(lbFrm2,textvariable=self.var_noofdays,font=("arial",12,"bold"),width=29)
        eNoOfDays.grid(row=6,column=1,sticky=W) 
        #paid tax
        paidTax=Label(lbFrm2,text="Paid Tax",font=("arial",12,"bold"),padx=2,pady=6)
        paidTax.grid(row=7,column=0,sticky=W)  
        epaidTax=ttk.Entry(lbFrm2,textvariable=self.var_paidtax,font=("arial",12,"bold"),width=29)
        epaidTax.grid(row=7,column=1,sticky=W) 
        #sub total
        SubTotal=Label(lbFrm2,text="Sub Total",font=("arial",12,"bold"),padx=2,pady=6)
        SubTotal.grid(row=8,column=0,sticky=W)  
        eSubTotal=ttk.Entry(lbFrm2,textvariable=self.var_actualtotal,font=("arial",12,"bold"),width=29)
        eSubTotal.grid(row=8,column=1,sticky=W) 
        #total cost
        totalCost=Label(lbFrm2,text="Total Cost",font=("arial",12,"bold"),padx=2,pady=6)
        totalCost.grid(row=9,column=0,sticky=W)  
        etotalCost=ttk.Entry(lbFrm2,textvariable=self.var_total,font=("arial",12,"bold"),width=29)
        etotalCost.grid(row=9,column=1,sticky=W) 
       
        
   
        btFrm=Frame(lbFrm2,bd=2,relief=RIDGE)
        btFrm.place(x=0,y=370,width=412,height=80)
         #==============bill butons==========
        btbutt=Button(btFrm,text="Bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="white",width=9)
        btbutt.grid(row=10,column=0,padx=1,sticky=W)
           #...........buttons.............      
        btadd=Button(btFrm,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="white",width=9)
        btadd.grid(row=0,column=0,padx=1)
    
        btup=Button(btFrm,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="white",width=9)
        btup.grid(row=0,column=1,padx=1)
    
        btdel=Button(btFrm,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="white",width=9)
        btdel.grid(row=0,column=2,padx=1)
    
        btreset=Button(btFrm,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="white",width=9)
        btreset.grid(row=0,column=3,padx=1)
        #===========rightside Image====
        #image2=Image.open(r"C:\Users\shahz\OneDrive\Desktop\prIm.jpg")
       # image2=image2.resize((420,200),Image.ANTIALIAS)
        #test=ImageTk.PhotoImage(image2)
       # bgImage2=ttk.Label(image=test)
       # bgImage2.image=test
       # bgImage2.place(x=760,y=70,width=520,height=200)
        
        
        #=============table 2==
        lbFrmR2=LabelFrame(self.root,bd=2,relief=RIDGE,text="View details and Search",padx=2,font=("times new roman",12,"bold"))
        lbFrmR2.place(x=435,y=50,width=760,height=760)
    
    
    
        lsearchby=Label(lbFrmR2,font=("arial",12,"bold"),text="Search by",bg="red",fg="white")
        lsearchby.grid(row=0,column=0,sticky=W)
        self.search_var=StringVar()
        comboSearch=ttk.Combobox(lbFrmR2,font=("arial",12,"bold"),width=23,state="readonly")
        comboSearch["value"]=("Room","Contact")
        comboSearch.current(0)
    
        comboSearch.grid(row=0,column=1,padx=2)
        self.txt_search=StringVar()
    
        txtSearch=ttk.Entry(lbFrmR2,font=("arial",12,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)
    
    #button
        #btSearch=Button(lbFrmR2,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="white",width=9)
        #btSearch.grid(row=0,column=3,padx=1)
    
        #btshow=Button(lbFrmR2,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="white",width=9)
        #btshow.grid(row=0,column=4,padx=1)
        #searchby table
        #............data table.......
        #............data table.......
    
    
        Tfram=Frame(lbFrmR2,bd=2,relief=RIDGE)
        Tfram.place(x=0,y=50,width=750,height=180)
        scbarx=ttk.Scrollbar(Tfram,orient=HORIZONTAL)
    
        scbary=ttk.Scrollbar(Tfram,orient=VERTICAL)
        self.room_table=ttk.Treeview(Tfram,columns=("contact","checkinDate","chekoutDate","roomtype","roomavailable","meal","noOFdays"),xscrollcommand=scbarx.set)
    
        self.room_table=ttk.Treeview(Tfram,columns=("contact","checkinDate","chekoutDate","roomtype","roomavailable","meal","noOFdays"),yscrollcommand=scbary.set)
    
        scbarx.pack(side=BOTTOM,fill=X)
        scbary.pack(side=RIGHT,fill=Y)
    
        scbarx.config(command=self.room_table.xview)
        scbary.config(command=self.room_table.yview)
    
        self.room_table.heading("contact",text="Contact No")
        self.room_table.heading("checkinDate",text="Check-in")
        self.room_table.heading("chekoutDate",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOFdays",text="NoOfDays")
        
        self.room_table["show"]="headings"
        
        self.room_table.column("contact",width=100)
        self.room_table.column("checkinDate",width=100)
        self.room_table.column("chekoutDate",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOFdays",width=100)

        
        self.room_table.pack(fill=BOTH,expand=1)
        
        self.room_table.bind ( "<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        
        #=======add button data
    def add_data ( self ) :
        if self.var_contact.get ( ) == " " or self.var_checkin.get ( ) == " " :
            messagebox.showerror ( " Error " , " All fields are requaired " , parent = self.root )
        else :
         try :
                      
                     con = sqlite3.connect('mcsdb1.db')
                     c=con.cursor()  
                     c.execute("insert into room (Contact,checkindate,checkoutdate,roomtype,roomavailable,meal,noOfdays) values(?,?,?,?,?,?,? ) " , (
                         
                                                                    self.var_contact.get(),
                                                                    self.var_checkin.get(),
                                                                    self.var_checkout.get(),
                                                                    self.var_roomtype.get(),
                                                                    self.var_roomavailable.get(),
                                                                    self.var_meal.get(),
                                                                    self.var_noofdays.get(),
                                                                    
                         
                     ))
                    
                     con.commit()
                     self.fetch_data()
                     c=con.close()
                                                                           
                     messagebox.showinfo ( " Success " , " Room datails have been added ", parent = self.root )
         except Exception as es:
          messagebox.showwarning("warning",f"SOmething went wrong:{str(es)}",parent=self.root)  
                  
                     
    #========fetch data=====\
    def fetch_data(self):
             


            conn = sqlite3.connect('mcsdb1.db')
            c=conn.cursor()  
            c.execute("select * from room")   
            rows=c.fetchall()
            if len(rows)!=0:
              self.room_table.delete(*self.room_table.get_children())
              for i in rows:
                  self.room_table.insert("",END,values=i)
              conn.commit()
              conn.close() 
              #======get cursor===========
    def get_cursor(self,event=""):
         cursor_row=self.room_table.focus()
         cont=self.room_table.item(cursor_row)
         row=cont["values"]
     
         self.var_contact.set(row[0]),
         self.var_checkin.set(row[1]),
         self.var_checkout.set(row[2]),
         self.var_roomtype.set(row[3]),
         self.var_roomavailable.set(row[4]),
         self.var_meal.set(row[5]),
         self.var_noofdays.set(row[6])  
    #======update======
    def update(self):
            if self.var_contact.get()=="":
                messagebox.showerror("Error","Please enter mobile number",parent=self.root)
            else:
                    
                
                 
                conn = sqlite3.connect('mcsdb1.db')
                c=conn.cursor()  
                c.execute("update room set checkindate=?,checkoutdate=?,roomtype=?,roomavailable=?,meal=?,noOfdays=? where Contact=?",(
                                                                    
                                                                    
                                                                    self.var_checkin.get(),
                                                                    self.var_checkout.get(),
                                                                    self.var_roomtype.get(),
                                                                    self.var_roomavailable.get(),
                                                                    self.var_meal.get(),
                                                                    self.var_noofdays.get(),
                                                                    self.var_contact.get()

                    
                                                                    ))
                          
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update","Room details Updated Successfully",parent=self.root)
 
    def delete(self):
     delete=messagebox.askyesno("Hotel Management System", "Do YOU want to delte customer",parent=self.root)
     if delete>0:
             


            conn = sqlite3.connect('mcsdb1.db')
            c=conn.cursor()   
            query="delete from room where Contact=?" 
            value=(self.var_contact.get(),)
            c.execute(query,value)
     else:
         if not delete:
             return
     conn.commit()
     self.fetch_data()
     conn.close()
    def  reset(self):
         self.var_contact.set(""),
         self.var_checkin.set("")
         self.var_checkout.set(""),
         self.var_roomtype.set(""),
         self.var_roomavailable.set(""),
         self.var_meal.set(""),
         self.var_noofdays.set("")  
         self.var_noofdays.set("")
         self.var_paidtax.set("")
         self.var_actualtotal.set("")
         self.var_total.set("")
         
                         
#============fetch all===========                 
    def fetch_contact(self):
          

         conn = sqlite3.connect('mcsdb1.db')
         c=conn.cursor() 
        
         if self.var_contact.get()=="":
            messagebox.showerror ( " Error " , " Plaese enter Contact Number " ,parent=self.root)
         else:
                 
                
                query = ( "select Name from customer where Mobile=?" )
                value = ( self.var_contact.get(), )
                c.execute ( query , value )
                row =c.fetchone ( )
                if row==None :
                    messagebox.showerror ( " Error " , " THis number Not Found " , parent = self.root)
                else :
                     c=conn.commit ()
                     c=conn.close()
                     showDataframe =Frame ( self.root , bd = 4 , relief = RIDGE , padx =2 )
                     showDataframe.place ( x = 440 , y = 70 , width = 300 , height = 180 )
                     lblName2 = Label (showDataframe,text="Name",font = ( " arial " , 12 , " bold " ) )
                     lblName2.place ( x=0 , y=0)
                     lblName3 = Label ( showDataframe , text= row, font = ("arial",12,"bold"))
                     lblName3.place (x=90,y=0)
                     #gender
                      
                     conn = sqlite3.connect('mcsdb1.db')
                     c=conn.cursor()  
                     c.execute( " select Gender from customer where Mobile ='?' " )
                     value= ( self.var_contact.get(), )
                     c.execute ( query , value )
                     row =c.fetchone ( )
                                                   
                     lblGender =Label ( showDataframe , text="Gender:" , font =( " arial " , 12 , " bold " ))
                     lblGender.place ( x = 0 , y= 30 )
                     lbl2= Label ( showDataframe , text = row , font = ( " arial " , 12 , " bold " ) )
                     lbl2.place ( x = 90 ,y=30 )
                     #email
                     
                      
                     conn = sqlite3.connect('mcsdb1.db')
                     c=conn.cursor()  
                     c.execute("select Email from customer where Mobile='?'")
                     value= ( self.var_contact.get ( ) , )
                     c.execute ( query , value )
                     row = c.fetchone ( )
                     lblemail = Label ( showDataframe , text= " Email :" , font = ( " arial " , 12 , " bold " ) )
                     lblemail.place ( x=0 , y =60 )
                     lb13 = Label ( showDataframe , text = row , font = ( " arial " , 12 , " bold " ) )
                     lb13.place ( x = 90 , y = 60 )
           #Nationality ----
                      
                     conn = sqlite3.connect('mcsdb1.db')
                     c=conn.cursor()  
                     c.execute( " select Nationality from customer where Mobile='?' " )
                     value= ( self.var_contact.get() , )
                     c.execute ( query , value )
                     row =c.fetchone ( )
                     lblNationality = Label ( showDataframe , text= " Nationality : " , font= ( " arial " , 12 , " bold " ) )
                     lblNationality.place ( x = 0,y = 90 )
                     lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
                     lbl4.place(x=90,y=90)                     
                     
                     #======== Address
                      
                     conn = sqlite3.connect('mcsdb1.db')
                     c=conn.cursor()  
                     c.execute( " select Address from customer where Mobile='?' " )
                     value = ( self.var_contact.get ( ) , )
                     c.execute ( query , value )
                     row =c.fetchone
                     lbladdress =Label ( showDataframe, text=" Address : " , font = ( " arial " , 12 , " bold " ) )
                     lbladdress.place ( x = 0 , y = 120 )
                     lb11 = Label ( showDataframe , text= row , font =( " arial " , 12 , " bold " ) )
                     lb11.place ( x = 90 , y = 120 )
                     
                       
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)
        
        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxury"):
            q1=float(800)
            q2=float(900)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxury"):
            q6=float(700)
            q7=float(800)
            q8=float(self.var_noofdays.get())
            q9=float(q6+q7)
            q10=float(q8+q9)
            Tax="Rs."+str("%.2f"%((q10)*0.09))
            ST="Rs."+str("%.2f"%((q10)))
            TT="Rs."+str("%.2f"%(q10+((q10)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxury"):
            q1=float(600)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            #single
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
            q1=float(600)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(500)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT) 
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(500)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)  
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
            q1=float(400)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(400)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)  
        else:
             messagebox.showerror("Error","Wrong Input",parent=self.root)
            
           
    def search(self):
             


            conn = sqlite3.connect('mcsdb1.db')
            c=conn.cursor()
            c.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
            row=c.fetchall()
            if len(row)!=0:
                self.room_table.delete(self.room_table.get_children())
                for i in row:
                    self.room_table.insert("",END,values=i)  
            conn.commit()
            conn.close()                      
                     
                     
                  
         
        
    
        
    

    
if __name__ == "__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()        
        
        
        