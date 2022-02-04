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
class RoomBooking:
    def __init__(self,root,var_hotel):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1300x550+234+100")
        self.var_hotel=var_hotel
        self.booking_id=StringVar()
        x=random.randint(1000,9999)
        self.booking_id.set(str(x))

        self.book_date=StringVar()
        self.checkout=StringVar()
        self.total_room=StringVar()
        self.payment=StringVar()
        self.room_number=StringVar()
        self.services=StringVar()
        self.var_id=StringVar()
        self.days=StringVar()
        self.room_type=StringVar()


        lbl_title=Label(self.root,text="ROOM BOOKING",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1300,height=50)

        labelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="BOOKING DETAILS",padx=2,font=("times new roman",15,"bold"))
        labelframe.place(x=5,y=50,width=455,height=590)

        lbl_cust_id=Label(labelframe,text="Customer ID",font=("arial",15,"bold"),padx=2,pady=6)
        lbl_cust_id.grid(row=0,column=0,sticky=W)

        entry_id=ttk.Entry(labelframe,textvariable=self.var_id,font=("arial",13,"bold"),width=20)
        entry_id.grid(row=0,column=1,sticky=W)

        btn_fetch=Button(labelframe,text="Fetch Data",font=("arial",11,"bold"),bg="black",fg="gold",width=8,command=self.fetch_cust_id)
        btn_fetch.place(x=350,y=4)

        lbl_booking_id=Label(labelframe,text="Booking ID",font=("arial",15,"bold"),padx=2,pady=6)
        lbl_booking_id.grid(row=1,column=0,sticky=W)

        entry_id=ttk.Entry(labelframe,textvariable=self.booking_id,width=29,font=("arial",13,"bold"),state="readonly")
        entry_id.grid(row=1,column=1)

        lbl_book_date=Label(labelframe,text="Check In Date",font=("arial",15,"bold"),padx=2,pady=6)
        lbl_book_date.grid(row=2,column=0,sticky=W)

        entry_book_date=ttk.Entry(labelframe,textvariable=self.book_date,width=29,font=("arial",13,"bold"))
        entry_book_date.grid(row=2,column=1)

        lbl_checkout=Label(labelframe,text="Check Out Date",font=("arial",15,"bold"),padx=2,pady=6)
        lbl_checkout.grid(row=3,column=0,sticky=W)

        entry_checkout=ttk.Entry(labelframe,textvariable=self.checkout,width=29,font=("arial",13,"bold"))
        entry_checkout.grid(row=3,column=1)

        lbl_total_rooms=Label(labelframe,text="Total Rooms",font=("arial",15,"bold"),padx=2,pady=6)
        lbl_total_rooms.grid(row=4,column=0,sticky=W)

        entry_total_rooms=ttk.Entry(labelframe,textvariable=self.total_room,width=29,font=("arial",13,"bold"))
        entry_total_rooms.grid(row=4,column=1)

        lbl_payment=Label(labelframe,text="Payment",font=("arial",15,"bold"),padx=2,pady=6)
        lbl_payment.grid(row=5,column=0,sticky=W)

        entry_payment=ttk.Entry(labelframe,textvariable=self.payment,width=29,font=("arial",13,"bold"))
        entry_payment.grid(row=5,column=1)

        lbl_days=Label(labelframe,text="No of days",font=("arial",15,"bold"),padx=2,pady=6)
        lbl_days.grid(row=6,column=0,sticky=W)

        entry_days=ttk.Entry(labelframe,textvariable=self.days,width=29,font=("arial",13,"bold"))
        entry_days.grid(row=6,column=1)
        
        lbl_room_number=Label(labelframe,text="Room Number",font=("arial",15,"bold"),padx=2,pady=6)
        lbl_room_number.grid(row=7,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
        my_cur=conn.cursor()
        my_cur.execute("select RoomNumber from details where Booked=%s AND hotel_id=%s",("False",self.var_hotel))
        rows=my_cur.fetchall()
        conn.commit()
        conn.close()
        combo_roomnumber=ttk.Combobox(labelframe,font=("arial",15,"bold"),textvariable=self.room_number,width=22,state="read only")
        combo_roomnumber["value"]=rows
        combo_roomnumber.current(0)
        combo_roomnumber.grid(row=7,column=1)

        lbl_services=Label(labelframe,text="Services",font=("arial",15,"bold"),padx=2,pady=6)
        lbl_services.grid(row=8,column=0,sticky=W)

        combo_services=ttk.Combobox(labelframe,font=("arial",15,"bold"),textvariable=self.services,width=22,state="read only")
        combo_services["value"]=("Breakfast","Dinner","Meals")
        combo_services.current(0)
        combo_services.grid(row=8,column=1)

        lbl_roomtype=Label(labelframe,text="Room Type",font=("arial",15,"bold"),padx=2,pady=6)
        lbl_roomtype.grid(row=9,column=0,sticky=W)
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
        my_cur=conn.cursor()
        my_cur.execute("select RoomType from details")
        type=my_cur.fetchall()
        conn.commit()
        conn.close()
        combo_roomtype=ttk.Combobox(labelframe,font=("arial",15,"bold"),textvariable=self.room_type,width=22,state="read only")
        combo_roomtype["value"]=type
        combo_roomtype.current(0)
        combo_roomtype.grid(row=9,column=1)

        btn_bill=Button(labelframe,text="Bill",font=("arial",13,"bold"),bg="black",fg="gold",width=9,command=self.total)
        btn_bill.grid(row=10,column=0,padx=1,sticky=W)

        btn_frame=Frame(labelframe,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=435,width=412,height=40)

        btn_add=Button(btn_frame,text="Add",font=("arial",13,"bold"),bg="black",fg="gold",width=9,command=self.add_data)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",font=("arial",13,"bold"),bg="black",fg="gold",width=9,command=self.update)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",font=("arial",13,"bold"),bg="black",fg="gold",width=9,command=self.delete)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",font=("arial",13,"bold"),bg="black",fg="gold",width=9,command=self.reset)
        btn_reset.grid(row=0,column=3,padx=1)

        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("times new roman",15,"bold"))
        tableframe.place(x=460,y=280,width=860,height=260)


        lblsearch=Label(tableframe,text="Search By : ",font=("arial",13,"bold"),bg='red',fg='white')
        lblsearch.grid(row=0,column=0,sticky=W,padx=1)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(tableframe,textvariable=self.search_var,font=("arial",13,"bold"),width=24,state="read only")
        combo_search["value"]=("Booking ID","Room ID")
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
        deatilsframe.place(x=0,y=50,width=820,height=180)

        scroll_x=ttk.Scrollbar(deatilsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(deatilsframe,orient=VERTICAL)

        self.room_Details=ttk.Treeview(deatilsframe,columns=("Booking ID","Customer ID","Check In Date","Check Out Date","Total Room","Payment","Room Number","Service Name","No of days"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_Details.xview)
        scroll_y.config(command=self.room_Details.yview)

        self.room_Details.heading("Booking ID",text="Booking ID")
        self.room_Details.heading("Customer ID",text="Customer ID")

        self.room_Details.heading("Check In Date",text="Check In Date")
        self.room_Details.heading("Check Out Date",text="Check Out Date")
        self.room_Details.heading("Total Room",text="Total Room")
        self.room_Details.heading("Payment",text="Payment")
        self.room_Details.heading("Room Number",text="Room Number")
        self.room_Details.heading("Service Name",text="Service Name")
        self.room_Details.heading("No of days",text="Number Of Days")

        self.room_Details["show"]="headings"
        self.room_Details.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.room_Details.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
            if self.room_number.get() == "" or self.var_id.get()=="":
                messagebox.showerror("Error","Please fill all the fields",parent=self.root)
            else:
                try :
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
                    my_cur=conn.cursor()
                    my_cur.execute("insert into booking values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.booking_id.get(),self.var_id.get(),self.var_hotel,self.book_date.get(),self.checkout.get(),self.total_room.get(),self.payment.get(),self.room_number.get(),self.days.get()))
                    my_cur.execute("insert into services values(%s,%s)",(self.booking_id.get(),self.services.get()))
                    my_cur.execute("update details set Booked=%s where RoomNumber=%s",("True",self.room_number.get()))
                    conn.commit()
                    conn.close()
                    self.fetch_data()
                    messagebox.showinfo("Success","Room Booked",parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"Something went wrong:{str(es)}",parent=self.root)



    def get_cursor(self,events=""):
        cursor_row=self.room_Details.focus()
        content=self.room_Details.item(cursor_row)
        row=content["values"]
        self.booking_id.set(row[0])
        self.var_id.set(row[1])
        self.book_date.set(row[2])
        self.checkout.set(row[3])
        self.total_room.set(row[4])
        self.payment.set(row[5])
        self.room_number.set(row[6])
        self.services.set(row[7])
        self.days.set(row[8])
    
    def update(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Please enter the name",parent=self.root)
        else:
            print(self.days.get())
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
            my_cur=conn.cursor()
            my_cur.execute("update booking set Check_in_date=%s,Check_out_date=%s,Total_Rooms=%s,Payment=%s,Room_Number=%s,No_of_Days=%s where Booking_ID=%s",(self.book_date.get(),self.checkout.get(),self.total_room.get(),self.payment.get(),self.room_number.get(),self.days.get(),self.booking_id.get()))
            my_cur.execute("update services set Name=%s where Booking_ID=%s",(self.services.get(),self.booking_id.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer Details Updated",parent=self.root)

    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
        my_cur=conn.cursor()
        my_cur.execute("Select booking.Booking_ID, Customer_ID,Check_in_date,Check_out_date,Total_Rooms,Payment,Room_Number,Name,No_of_Days from booking JOIN services ON booking.Booking_ID= services.Booking_ID  where booking.hotel_id=%s",(self.var_hotel,))
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.room_Details.delete(*self.room_Details.get_children())
            for i in rows:
                self.room_Details.insert("",END,values=i)
            conn.commit()
            conn.close()


    def delete(self):
        delete=messagebox.askyesno("Hotel","Are you sure you want to delete?",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
            my_cur=conn.cursor()
            query="delete from booking where Booking_ID=%s"
            values=(self.booking_id.get(),)
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
        self.var_id.set("")
        y=random.randint(1000,9999)
        self.booking_id.set(str(y))
        self.book_date.set("")
        self.checkout.set("")
        self.total_room.set("")
        self.payment.set("")
        self.room_number.set("")
        self.days.set("")
        self.services.set("")
        self.room_type.set("")




    def fetch_cust_id(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Please Enter The ID",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
            my_cur=conn.cursor()
            query="select Name from customer where ID=%s"
            values=(self.var_id.get(),)
            my_cur.execute(query,values)
            row=my_cur.fetchone()

            if row==None:
                messagebox.showerror("Error","This Number Not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=460,y=100,width=820,height=160)

                lblName=Label(showDataframe,text="Name: ",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=150,y=0)

                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
                my_cur=conn.cursor()
                query="select `Card Number` from customer where ID=%s"
                values=(self.var_id.get(),)
                my_cur.execute(query,values)
                row=my_cur.fetchone()

                lblCard=Label(showDataframe,text="Card Number: ",font=("arial",12,"bold"))
                lblCard.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=150,y=30)

                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
                my_cur=conn.cursor()
                query="select Gender from customer where ID=%s"
                values=(self.var_id.get(),)
                my_cur.execute(query,values)
                row=my_cur.fetchone()

                lblgender=Label(showDataframe,text="Gender: ",font=("arial",12,"bold"))
                lblgender.place(x=0,y=60)

                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=150,y=60)
    
    def total(self):
        inDate= self.book_date.get()
        outDate= self.checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.days.set(abs(outDate-inDate).days)

        if(self.services.get()=="Breakfast" ):
            q1=float(2000)
            q2=float(self.days.get())
            q4=float(q1*q2)
            Tax="Rs."+ str("%.2f"%((q4)*0.1))
            total="Rs."+str("%.2f"%(q4+((q4)*0.1)))
            self.payment.set(total)

        elif(self.services.get()=="Dinner" ):
            q1=float(2500)
            q2=float(self.days.get())
            q4=float(q1*q2)
            Tax="Rs."+ str("%.2f"%((q4)*0.1))
            total="Rs."+str("%.2f"%(q4+((q4)*0.1)))
            self.payment.set(total)

        elif(self.services.get()=="Meals" ):
            q1=float(1500)
            q2=float(self.days.get())
            q4=float(q1*q2)
            Tax="Rs."+ str("%.2f"%((q4)*0.1))
            total="Rs."+str("%.2f"%(q4+((q4)*0.1)))
            self.payment.set(total)

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
        my_cur=conn.cursor()
        # print("select * from customer where"+ str(self.search_var.get())+"= '%s'",(str(self.txt_search.get())))
        print(self.txt_search.get())
        if self.search_var.get() == "Booking ID":
            my_cur.execute("select Booking_ID,Customer_ID,Check_in_date,Check_out_date,Total_Rooms,Payment,Room_Number,No_of_Days from booking where  Booking_ID LIKE '%"+str(self.txt_search.get())+"%' AND booking.hotel_id=%s",(self.var_hotel,))
            rows=my_cur.fetchall()
            my_cur.execute("select * from services where Booking_ID LIKE '%"+str(self.txt_search.get())+"%'")
            rows2=my_cur.fetchall()
            if len(rows) !=0 and len(rows2) !=0 :
                self.room_Details.delete(*self.room_Details.get_children())
                for i,j in zip(rows,rows2):
                    i=i[:7]+(j[1],i[-1])
                    self.room_Details.insert("",END,values=i)
        else:
            my_cur.execute("select Booking_ID,Customer_ID,Check_in_date,Check_out_date,Total_Rooms,Payment,Room_Number,No_of_Days from booking where  Room_Number LIKE '%"+str(self.txt_search.get())+"%'")
            rows=my_cur.fetchall()
            id=rows[0][0]
            my_cur.execute("select * from services where Booking_ID LIKE '%"+str(id)+"%'")
            rows2=my_cur.fetchall()
            if len(rows) !=0 and len(rows2) !=0 :
                self.room_Details.delete(*self.room_Details.get_children())
                for i,j in zip(rows,rows2):
                    i=i[:7]+(j[1],i[-1])
                    self.room_Details.insert("",END,values=i)
        




if __name__=="__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()