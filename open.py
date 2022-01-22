from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk
from customer import Cust_win
from details import DetailsRoom
from room import RoomBooking
class hotel_class:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        self.var_hotel=StringVar()
        self.open()
    def open(self):
        
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1550,height=50)

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=60,width=1550,height=820)
        img2=Image.open(r"images\background.jpg")
        img2=img2.resize((1550,820),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)

        labelimg2=Label(main_frame,image=self.photoimage2,bd=4,relief=RIDGE)
        labelimg2.place(x=0,y=0,width=1550,height=820)

        btn_frame=Frame(main_frame,bg="white")
        btn_frame.place(x=610,y=170,width=250,height=250)

        # btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        # btn_frame.place(x=0,y=205,width=700,height=190)

        lbl_cust_gender=Label(btn_frame,text="Hotel",font=("arial",25,"bold"),padx=2,pady=6,bg="black",fg="gold")
        lbl_cust_gender.place(x=80,y=50)

        combo_gender=ttk.Combobox(btn_frame,font=("arial",15,"bold"),textvariable=self.var_hotel,width=10,state="read only")
        combo_gender["value"]=(1,2,3)
        combo_gender.current(0)
        combo_gender.place(x=60,y=110)
        submit_btn=Button(btn_frame,text="Open",width=18,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1",command=self.hotel)
        submit_btn.place(x=30,y=150)
        exit_btn=Button(btn_frame,text="Exit",width=18,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        exit_btn.place(x=30,y=200)

        
    def hotel(self):
        print(self.var_hotel.get())
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1550,height=50)

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=60,width=1550,height=820)



        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=150,width=230,height=50)



        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=205,width=228,height=190)

        cust_btn=Button(btn_frame,text="Customer",command=self.cust_datils,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="Room",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1",command=self.room)
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="Details",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1",command=self.deatils)
        details_btn.grid(row=2,column=0,pady=1)

        exit_btn=Button(btn_frame,text="Logout",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        exit_btn.grid(row=3,column=0,pady=1)

        img2=Image.open(r"images\background.jpg")
        img2=img2.resize((1310,590),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)

        labelimg2=Label(main_frame,image=self.photoimage2,bd=4,relief=RIDGE)
        labelimg2.place(x=225,y=0,width=1310,height=590)

    def cust_datils(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window,self.var_hotel.get())
    
    def room(self):
        self.new_window=Toplevel(self.root)
        self.app=RoomBooking(self.new_window,self.var_hotel.get())
    def deatils(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window,self.var_hotel.get())
        

   





if __name__=="__main__":
    root=Tk()
    obj=hotel_class(root)
    root.mainloop()