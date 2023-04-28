from ast import Pass
from email.mime import message
from ipaddress import collapse_addresses
from msilib import text
from pickletools import TAKEN_FROM_ARGUMENT1
from tkinter import *
import mysql.connector
import tkinter
import random
from tkinter.tix import COLUMN
from PIL import Image 
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class customers():
   
        
        
 def __init__(self,root):
    self.root=root
    self.root.title("Hotel Management system")
    self.root.geometry("1190x550+0+100")
    #............variables......
    self.var_ref=StringVar()
    x=random.randint(1000,9999)
    self.var_ref.set(str(x))
    
    self.var_cust_name=StringVar()
    self.var_mother=StringVar()
    self.var_gender=StringVar()
    self.var_post=StringVar()
    self.var_mobile=StringVar()
    self.var_email=StringVar()
    self.var_nationality=StringVar()
    self.var_id_proof=StringVar()
    self.var_id_number=StringVar()
    self.var_address=StringVar()
    
    
    
    
    lab_tit=Label(self.root,text="Add Customer Details",font=("times new roman",18,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
    lab_tit.place(x=0,y=0,width=1190,height=50)
    
#..........label...........

    lbFrm=LabelFrame(self.root,bd=2,relief=RIDGE,text="cusotmer details",padx=2,font=("times new roman",12,"bold"))
    lbFrm.place(x=5,y=50,width=425,height=490)
    
    lb1cust=Label(lbFrm,text="Customer Ref", font=( "times new roman",12,"bold") , padx = 2 , pady = 6 )
    lb1cust.grid(row=0,column=0,sticky=W)
    
    entry=Entry(lbFrm,textvariable=self.var_ref,width=22,font=( "times new roman",12,"bold") ,state="readonly")
    entry.grid(row=0,column=1)
    
    #cutname
    cname=Label(lbFrm,font=("arial",12,"bold"),text="Customer Name:",padx=2,pady=6)
    cname.grid(row=1,column=0,sticky=W)
    tcname=ttk.Entry(lbFrm,textvariable=self.var_cust_name,font=("arial",12,"bold"),width=29)
    tcname.grid(row=1,column=1)
    #mother name
    cmname=Label(lbFrm,font=("arial",12,"bold"),text="Father Name:",padx=2,pady=6)
    cmname.grid(row=2,column=0,sticky=W)
    tmcname=ttk.Entry(lbFrm,textvariable=self.var_mother,font=("arial",12,"bold"),width=29)
    tmcname.grid(row=2,column=1)
    #gender combox
    cgname=Label(lbFrm,font=("arial",12,"bold"),text="Gender:",padx=2,pady=6)
    cgname.grid(row=3,column=0,sticky=W)
    tcgname=ttk.Entry(lbFrm,font=("arial",12,"bold"),width=29)
    tcgname.grid(row=3,column=1)
    combog=ttk.Combobox(lbFrm,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
    combog["value"]=("Male","Female","Other")
    combog.current(0)
    
    combog.grid(row=3,column=1)
    
    #postcode
    pcode=Label(lbFrm,font=("arial",12,"bold"),text="Postal code:",padx=2,pady=6)
    pcode.grid(row=4,column=0,sticky=W)
    tpcode=ttk.Entry(lbFrm,textvariable=self.var_post,font=("arial",12,"bold"),width=29)
    tpcode.grid(row=4,column=1)
    #mobile num
    cnum=Label(lbFrm,font=("arial",12,"bold"),text="mobile num:",padx=2,pady=6)
    cnum.grid(row=5,column=0,sticky=W)
    tcnum=ttk.Entry(lbFrm,textvariable=self.var_mobile,font=("arial",12,"bold"),width=29)
    tcnum.grid(row=5,column=1)
    #email
    cemail=Label(lbFrm,font=("arial",12,"bold"),text="Email:",padx=2,pady=6)
    cemail.grid(row=6,column=0,sticky=W)
    tcemail=ttk.Entry(lbFrm,textvariable=self.var_email,font=("arial",12,"bold"),width=29)
    tcemail.grid(row=6,column=1)
    #nationality
    cnationality=Label(lbFrm,font=("arial",12,"bold"),text="nationality:",padx=2,pady=6)
    cnationality.grid(row=7,column=0,sticky=W)
    cnationality=ttk.Entry(lbFrm,textvariable=self.var_nationality,font=("arial",12,"bold"),width=29)
    
    
    nat=ttk.Combobox(lbFrm,font=("arial",12,"bold"),width=27,state="readonly")
    nat["value"]=("Pakistani","Indian","Bangali","British","American","Other")
    nat.current(0)
    nat.grid(row=7,column=1)
    
    #id 
    cid=Label(lbFrm,font=("arial",12,"bold"),text="Id proof type",padx=2,pady=6)
    cid.grid(row=8,column=0,sticky=W)
    tcid=ttk.Entry(lbFrm,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=29)
  
    
    idt=ttk.Combobox(lbFrm,font=("arial",12,"bold"),width=27,state="readonly")
    idt["value"]=("Id card","Driving License","Passport","Other")
    idt.current(0)
    idt.grid(row=8,column=1)
    #id num
    cinum=Label(lbFrm,font=("arial",12,"bold"),text="ID num:",padx=2,pady=6)
    cinum.grid(row=9,column=0,sticky=W)
    tinum=ttk.Entry(lbFrm,textvariable=self.var_id_number,font=("arial",12,"bold"),width=29)
    tinum.grid(row=9,column=1)
    #address
    cadd=Label(lbFrm,font=("arial",12,"bold"),text="address:",padx=2,pady=6)
    cadd.grid(row=10,column=0,sticky=W)
    tcadd=ttk.Entry(lbFrm,textvariable=self.var_address,font=("arial",12,"bold"),width=29)
    tcadd.grid(row=10,column=1)
    
    #...........buttons.............
    btFrm=Frame(lbFrm,bd=2,relief=RIDGE)
    btFrm.place(x=0,y=400,width=412,height=40)
    btadd=Button(btFrm,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="white",width=9)
    btadd.grid(row=0,column=0,padx=1)
    
    btup=Button(btFrm,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="white",width=9)
    btup.grid(row=0,column=1,padx=1)
    
    btdel=Button(btFrm,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="white",width=9)
    btdel.grid(row=0,column=2,padx=1)
    
    btreset=Button(btFrm,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="white",width=9)
    btreset.grid(row=0,column=3,padx=1)
    #..................table frame........
    lbFrmR=LabelFrame(self.root,bd=2,relief=RIDGE,text="View details and Search",padx=2,font=("times new roman",12,"bold"))
    lbFrmR.place(x=435,y=50,width=900,height=490)
    
    
    #searchby
    lsearchby=Label(lbFrmR,font=("arial",12,"bold"),text="Search by",bg="red",fg="white")
    lsearchby.grid(row=0,column=0,sticky=W)
    self.search_var=StringVar()
    comboSearch=ttk.Combobox(lbFrmR,textvariable=self.search_var,font=("arial",12,"bold"),width=23,state="readonly")
    comboSearch["value"]=("Mobile","Ref")
    comboSearch.current(0)
    
    comboSearch.grid(row=0,column=1,padx=2)
    self.txt_search=StringVar()
    
    txtSearch=ttk.Entry(lbFrmR,textvariable=self.txt_search,font=("arial",12,"bold"),width=24)
    txtSearch.grid(row=0,column=2,padx=2)
    
    #button
    btSearch=Button(lbFrmR,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="white",width=9)
    btSearch.grid(row=0,column=3,padx=1)
    
    btshow=Button(lbFrmR,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="white",width=9)
    btshow.grid(row=0,column=4,padx=1)
    
    
    #............data table.......
    
    
    Tfram=Frame(lbFrmR,bd=2,relief=RIDGE)
    Tfram.place(x=0,y=50,width=750,height=350)
    scbarx=ttk.Scrollbar(Tfram,orient=HORIZONTAL)
    
    scbary=ttk.Scrollbar(Tfram,orient=VERTICAL)
    self.customer_table=ttk.Treeview(Tfram,columns=("ref","name","mothername","gender","post","mobile","email","nationality","idproof","id number","address"),xscrollcommand=scbarx.set)
    
    self.customer_table=ttk.Treeview(Tfram,columns=("ref","name","mothername","gender","post","mobile","email","nationality","idproof","id number","address"),yscrollcommand=scbary.set)
    
    scbarx.pack(side=BOTTOM,fill=X)
    scbary.pack(side=RIGHT,fill=Y)
    
    scbarx.config(command=self.customer_table.xview)
    scbary.config(command=self.customer_table.yview)
    
    self.customer_table.heading("ref",text="Refer no")
    self.customer_table.heading("name",text="Name")
    self.customer_table.heading("mothername",text="Mother Name")
    self.customer_table.heading("gender",text="Gender")
    self.customer_table.heading("post",text="Post Code")
    self.customer_table.heading("mobile",text="Mobile")
    self.customer_table.heading("email",text="Email")
    self.customer_table.heading("nationality",text="Nationality")
    self.customer_table.heading("idproof",text="Id Proof")
    self.customer_table.heading("id number",text="Id number")
    self.customer_table.heading("address",text="Address")
    
    self.customer_table["show"]="headings"
    self.customer_table.column("ref",width=100)
    self.customer_table.column("name",width=100)
    self.customer_table.column("mothername",width=100)
    self.customer_table.column("gender",width=100)
    self.customer_table.column("post",width=100)
    self.customer_table.column("mobile",width=100)
    self.customer_table.column("email",width=100)
    self.customer_table.column("nationality",width=100)
    self.customer_table.column("idproof",width=100)
    self.customer_table.column("id number",width=100)
    self.customer_table.column("address",width=100)
    
    
    self.customer_table.pack(fill=BOTH,expand=1)
    self.customer_table.bind("<ButtonRelease-1>",self.get_cursor)
    self.fetch_data()
 
 
    
    
 def add_data(self):
    if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root) 
    else:
        try:


            conn = sqlite3.connect('mcsdb1.db')
            c=conn.cursor()

            c.execute("insert into customer (Ref,Name,Mother,Gender,PostCode,Mobile,Email,Nationality,Idproof,Idnumber,Address) values(?,?,?,?,?,?,?,?,?,?,? )",(
                                                                    self.var_ref.get(),
                                                                    self.var_cust_name.get(),
                                                                    self.var_mother.get(),
                                                                    self.var_gender.get(),
                                                                    self.var_post.get(),
                                                                    self.var_mobile.get(),
                                                                    self.var_email.get(),
                                                                    self.var_nationality.get(),
                                                                    self.var_id_proof.get(),
                                                                    self.var_id_number.get(),
                                                                    self.var_address.get()
                                                                    
                                                            
                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Customer had been added",parent=self.root)
        except Exception as es:
            messagebox.showwarning("warning",f"Something went wrong:{str(es)}",parent=self.root) 
 #==========reset=======
 
     
 #===========fetch============
 def fetch_data(self):
            


            conn = sqlite3.connect('mcsdb1.db')
            c=conn.cursor()  
            c.execute("select * from customer")   
            rows=c.fetchall()
            if len(rows)!=0:
              self.customer_table.delete(*self.customer_table.get_children())
              for i in rows:
                  self.customer_table.insert("",END,values=i)
              conn.commit()
              conn.close()
 def get_cursor(self,event=""):
     cursor_row=self.customer_table.focus()
     cont=self.customer_table.item(cursor_row)
     row=cont["values"]
     
     self.var_ref.set(row[0]),
     self.var_cust_name.set(row[1]),
     self.var_mother.set(row[2]),
     self.var_gender.set(row[3]),
     self.var_post.set(row[4]),
     self.var_mobile.set(row[5]),
     self.var_email.set(row[6]),
     self.var_nationality.set(row[7]),
     self.var_id_proof.set(row[8]),
     self.var_id_number.set(row[9]),
     self.var_address.set(row[10])
 def update(self):
            if self.var_mobile.get()=="":
                messagebox.showerror("Error","Please enter mobile number",parent=self.root)
            else:
                    
                
                 
                conn = sqlite3.connect('mcsdb1.db')
                c=conn.cursor()  
                c.execute("update customer set Name=?,Mother=?,Gender=?,PostCode=?,Mobile=?,Email=?,Nationality=?,Idproof=?,Idnumber=?,Address=? where Ref=?",(
                                                                    
                                                                    self.var_cust_name.get(),
                                                                    self.var_mother.get(),
                                                                    self.var_gender.get(),
                                                                    self.var_post.get(),
                                                                    self.var_mobile.get(),
                                                                    self.var_email.get(),
                                                                    self.var_nationality.get(),
                                                                    self.var_id_proof.get(),
                                                                    self.var_id_number.get(),
                                                                    self.var_address.get(),
                                                                    self.var_ref.get()

                    
                                                                    ))
                          
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Updated Successfully",parent=self.root)
          
 def delete(self):
     delete=messagebox.askyesno("Hotel Management System", "Do YOU want to delete customer",parent=self.root)
     if delete>0:
             


            conn = sqlite3.connect('mcsdb1.db')
            c=conn.cursor()   
            query="delete from customer where Ref=?" 
            value=(self.var_ref.get(),)
            c.execute(query,value)
     else:
         if not delete:
             return
     conn.commit()
     self.fetch_data()
     conn.close()
                    
 def reset(self):
     #self.var_ref.set(""),
     self.var_cust_name.set(""),
     self.var_mother.set(""),
     #self.var_gender.set(""),
     self.var_post.set(""),
     self.var_mobile.set(""),
     #self.var_email.set(""),
     #self.var_nationality.set(""),
     self.var_id_proof.set(""),
     self.var_id_number.set(""),
     self.var_address.set("" )  
     
     
     x=random.randint(1000,9999)
     self.var_ref.set(str(x))  
 def search(self):
             
        try:

            conn = sqlite3.connect('mcsdb1.db')
            c=conn.cursor()
            c.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
            row=c.fetchall()
            if len(row)!=0:
                self.customer_table.delete(*self.customer_table.get_children())
                for i in row:
                    self.customer_table.insert("",END,values=i)  
                conn.commit()
            conn.close()      
            
        except Exception as es:
            messagebox.showwarning("warning",f"Something went wrong:{str(es)}",parent=self.root) 
     
 


    
if __name__ == "__main__":
    root=Tk()
    
    obj=customers(root)
    root.mainloop()

