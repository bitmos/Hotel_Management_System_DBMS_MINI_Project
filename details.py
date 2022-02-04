from tkinter import *
import tkinter
from typing import Pattern
from PIL import Image,ImageTk 
from tkinter import ttk
from time import strftime
from datetime import datetime
import mysql.connector 
import random
from tkinter import messagebox
class DetailsRoom:
    def __init__(self,root,var_hotel):
        self.var_hotel=var_hotel
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1300x550+234+100")

        lbl_title=Label(self.root,text="ROOM BOOKING",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1300,height=50)

        labelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",padx=2,font=("times new roman",15,"bold"))
        labelframe.place(x=5,y=50,width=540,height=350)

        lbl_floor=Label(labelframe,text="Floor",font=("arial",15,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframe,textvariable=self.var_floor,font=("arial",13,"bold"),width=20)
        entry_floor.grid(row=0,column=1,sticky=W)

        lbl_roomno=Label(labelframe,text="Room Number",font=("arial",15,"bold"),padx=2,pady=6)
        lbl_roomno.grid(row=1,column=0,sticky=W)
        self.var_roomno=StringVar()
        entry_roomno=ttk.Entry(labelframe,textvariable=self.var_roomno,font=("arial",13,"bold"),width=20)
        entry_roomno.grid(row=1,column=1,sticky=W)

        lbl_roomtype=Label(labelframe,text="Room Type",font=("arial",15,"bold"),padx=2,pady=6)
        lbl_roomtype.grid(row=2,column=0,sticky=W)
        self.var_roomtype=StringVar()
        entry_roomtype=ttk.Entry(labelframe,textvariable=self.var_roomtype,font=("arial",13,"bold"),width=20)
        entry_roomtype.grid(row=2,column=1,sticky=W)

        btn_frame=Frame(labelframe,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btn_add=Button(btn_frame,text="Add",font=("arial",13,"bold"),bg="black",fg="gold",width=9,command=self.add_data)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",font=("arial",13,"bold"),bg="black",fg="gold",width=9,command=self.update)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",font=("arial",13,"bold"),bg="black",fg="gold",width=9,command=self.delete)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",font=("arial",13,"bold"),bg="black",fg="gold",width=9,command=self.reset)
        btn_reset.grid(row=0,column=3,padx=1)

        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",padx=2,font=("times new roman",15,"bold"))
        tableframe.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tableframe,orient=VERTICAL)

        self.room_Details=ttk.Treeview(tableframe,columns=("Floor","Room Number","Room Type"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_Details.xview)
        scroll_y.config(command=self.room_Details.yview)

        self.room_Details.heading("Room Number",text="Room Number")
        self.room_Details.heading("Floor",text="Floor")
        self.room_Details.heading("Room Type",text="Room Type")

        self.room_Details["show"]="headings"
        self.room_Details.pack(fill=BOTH,expand=1)
        self.room_Details.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_data(self):
            if self.var_roomno.get() == "" or self.var_roomtype.get()=="":
                messagebox.showerror("Error","Please fill all the fields",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
                    my_cur=conn.cursor()
                    my_cur.execute("insert into details values(%s,%s,%s,%s,%s)",(self.var_floor.get(),self.var_roomno.get(),self.var_roomtype.get(),"False",self.var_hotel))
                    conn.commit()
                    conn.close()
                    self.fetch_data()
                    messagebox.showinfo("Success","New Room Added",parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"Something went wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
        my_cur=conn.cursor()
        my_cur.execute("Select * from details")
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.room_Details.delete(*self.room_Details.get_children())
            for i in rows:
                self.room_Details.insert("",END,values=i)
            conn.commit()
            conn.close()

    def get_cursor(self,events=""):
        cursor_row=self.room_Details.focus()
        content=self.room_Details.item(cursor_row)
        row=content["values"]
        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_roomtype.set(row[2])

    def update(self):
        if self.var_roomno.get()=="":
            messagebox.showerror("Error","Please enter the Room Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
            my_cur=conn.cursor()
            my_cur.execute("update details set floor=%s,RoomType=%s where RoomNumber=%s",(self.var_floor.get(),self.var_roomtype.get(),self.var_roomno.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Details Updated",parent=self.root)

    def delete(self):
        delete=messagebox.askyesno("Hotel","Are you sure you want to delete?",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
            my_cur=conn.cursor()
            query="delete from details where RoomNUmber=%s"
            values=(self.var_roomno.get(),)
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
        self.var_roomno.set("")
        self.var_floor.set("")
        self.var_roomtype.set("")


if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()