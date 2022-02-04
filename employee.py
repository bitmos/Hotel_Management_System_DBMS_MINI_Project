from tkinter import *
import tkinter
from typing import Pattern
from PIL import Image,ImageTk 
from tkinter import ttk
import mysql.connector 
import random

from tkinter import messagebox
class Employee():
    def __init__(self,root,var_hotel):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1300x550+234+100")
        self.var_hotel=var_hotel
        self.var_id=StringVar()
        x=random.randint(1000,9999)
        self.var_id.set(str(x))

        self.var_name=StringVar()
        self.var_country=StringVar()
        self.var_city=StringVar()
        self.var_zipcode=StringVar()
        self.var_cardnumber=StringVar()
        self.var_gender=StringVar()


        lbl_title=Label(self.root,text="ADD Employee DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1300,height=50)


        labelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",15,"bold"))
        labelframe.place(x=5,y=50,width=455,height=490)



        lbl_cust_id=Label(labelframe,text="Employee ID",font=("arial",15,"bold"),padx=2,pady=6)
        lbl_cust_id.grid(row=0,column=0,sticky=W)

        entry_id=ttk.Entry(labelframe,textvariable=self.var_id,width=29,font=("arial",13,"bold"),state="readonly")
        entry_id.grid(row=0,column=1)

        lbl_cust_name=Label(labelframe,text="Name *",font=("arial",15,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0,sticky=W)

        entry_name=ttk.Entry(labelframe,textvariable=self.var_name,width=29,font=("arial",13,"bold"))
        entry_name.grid(row=1,column=1)

        lbl_cust_gender=Label(labelframe,text="Gender",font=("arial",15,"bold"),padx=2,pady=6)
        lbl_cust_gender.grid(row=2,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframe,font=("arial",15,"bold"),textvariable=self.var_gender,width=22,state="read only")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1)


        lbl_cust_cardno=Label(labelframe,text="Phone Number",font=("arial",15,"bold"),padx=2,pady=6)
        lbl_cust_cardno.grid(row=6,column=0,sticky=W)

        entry_cardno=ttk.Entry(labelframe,textvariable=self.var_cardnumber,width=29,font=("arial",13,"bold"))
        entry_cardno.grid(row=6,column=1)

        btn_frame=Frame(labelframe,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=300,width=412,height=40)

        btn_add=Button(btn_frame,text="Add",font=("arial",13,"bold"),bg="black",fg="gold",width=9,command=self.add_data)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",font=("arial",13,"bold"),bg="black",fg="gold",width=9,command=self.update)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",font=("arial",13,"bold"),bg="black",fg="gold",width=9,command=self.delete)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",font=("arial",13,"bold"),bg="black",fg="gold",width=9,command=self.reset)
        btn_reset.grid(row=0,column=3,padx=1)

        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("times new roman",15,"bold"))
        tableframe.place(x=435,y=50,width=860,height=490)


        lblsearch=Label(tableframe,text="Search By : ",font=("arial",13,"bold"),bg='red',fg='white')
        lblsearch.grid(row=0,column=0,sticky=W,padx=1)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(tableframe,textvariable=self.search_var,font=("arial",13,"bold"),width=24,state="read only")
        combo_search["value"]=("Employee_ID","Name")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=1)

        self.txt_search=StringVar()
        entry_search=ttk.Entry(tableframe,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        entry_search.grid(row=0,column=2,padx=1)

        btn_search=Button(tableframe,text="Search",font=("arial",13,"bold"),bg="black",fg="gold",width=8,command=self.search)
        btn_search.grid(row=0,column=3,padx=1)

        btn_showall=Button(tableframe,text="Show All",font=("arial",13,"bold"),bg="black",fg="gold",width=8,command=self.fetch_data)
        btn_showall.grid(row=0,column=4,padx=1)


        deatilsframe=Frame(tableframe,bd=2,relief=RIDGE)
        deatilsframe.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(deatilsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(deatilsframe,orient=VERTICAL)

        self.Cust_Details=ttk.Treeview(deatilsframe,columns=("ID","Name","Phone Number","Gender"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details.xview)
        scroll_y.config(command=self.Cust_Details.yview)

        self.Cust_Details.heading("ID",text="Employee ID")
        self.Cust_Details.heading("Name",text="Employee Name")
        
        self.Cust_Details.heading("Phone Number",text="Phone Number")
        self.Cust_Details.heading("Gender",text="Gender")

        self.Cust_Details["show"]="headings"
        self.Cust_Details.pack(fill=BOTH,expand=1)
        self.Cust_Details.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if  self.var_name.get()=="":
            messagebox.showerror("Error","Please fill all the fields",parent=self.root)
        else:
            try :
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
                my_cur=conn.cursor()
                my_cur.execute("insert into employee values(%s,%s,%s,%s,%s)",(self.var_id.get(),self.var_name.get(),self.var_cardnumber.get(),self.var_gender.get(),self.var_hotel))
                # my_cur.execute("insert into address values(%s,%s,%s,%s,%s,%s)",("",self.var_country.get(),self.var_city.get(),self.var_zipcode.get(),self.var_hotel,self.var_id.get()))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success","Employee has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
        my_cur=conn.cursor()
        print(type(self.var_hotel))
        my_cur.execute("Select * from employee where hotel_id=%s",(self.var_hotel,))
        rows=my_cur.fetchall()
        print(rows)
        if len(rows)!=0:
            self.Cust_Details.delete(*self.Cust_Details.get_children())
            for i in rows:
                self.Cust_Details.insert("",END,values=i)
            conn.commit()
            conn.close()
    def get_cursor(self,events=""):
        cursor_row=self.Cust_Details.focus()
        content=self.Cust_Details.item(cursor_row)
        row=content["values"]
        self.var_id.set(row[0])
        self.var_name.set(row[1])
        self.var_cardnumber.set(row[2])
        self.var_gender.set(row[3])
        

    def update(self):
        if self.var_name.get()=="":
            messagebox.showerror("Error","Please enter the name",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
            my_cur=conn.cursor()
            my_cur.execute("update employee set Name=%s,Phone_Number=%s,Gender=%s where ID=%s",(self.var_name.get(),self.var_cardnumber.get(),self.var_gender.get(),self.var_id.get()))
            # my_cur.execute("update address set Country=%s,City=%s,ZipCode=%s where Employee_ID=%s",(self.var_country.get(),self.var_city.get(),self.var_zipcode.get(),self.var_id.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Employee Details Updated",parent=self.root)
            

    def delete(self):
        delete=messagebox.askyesno("Hotel","Are you sure you want to delete?",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
            my_cur=conn.cursor()
            query="delete from employee where ID=%s"
            values=(self.var_id.get(),)
            my_cur.execute(query,values)
            # query="delete from address where ID=%s"
            # values=(self.var_id.get(),)
            # my_cur.execute(query,values)
            
        else:
            return 
        conn.commit()
        conn.close()
        self.fetch_data()
    
    def reset(self):
        x=random.randint(1000,9999)
        self.var_id.set(str(x))
        self.var_name.set("")
        self.var_country.set("")
        self.var_city.set("")
        self.var_zipcode.set("")
        self.var_cardnumber.set("")

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
        my_cur=conn.cursor()
        # print("select * from customer where"+ str(self.search_var.get())+"= '%s'",(str(self.txt_search.get())))
        if self.search_var.get() == "ID":
            my_cur.execute("select * from employee where "+ str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
            rows=my_cur.fetchall()
            # my_cur.execute("select * from address where Employee_ID LIKE '%"+str(self.txt_search.get())+"%'")
            # rows2=my_cur.fetchall()
            if len(rows) !=0:
                self.Cust_Details.delete(*self.Cust_Details.get_children())
                for i in rows:
                    self.Cust_Details.insert("",END,values=i)
            
            conn.commit()
        else :
            my_cur.execute("select * from employee where "+ str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
            rows=my_cur.fetchall()
            if len(rows) !=0:
                self.Cust_Details.delete(*self.Cust_Details.get_children())
                for i in rows:
                    self.Cust_Details.insert("",END,values=i)
                    self.Cust_Details.insert("",END,values=i)

        
        conn.close()  



if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()