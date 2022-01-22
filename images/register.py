from atexit import register
from cgitb import text
from ssl import _create_unverified_context
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        self.fname=StringVar()
        self.lname=StringVar()
        self.cont=StringVar()
        self.email=StringVar()
        self.chec_v=IntVar()
        self.seqQ=StringVar()
        self.seqA=StringVar()
        

        self.bg=ImageTk.PhotoImage(file=r"images\register.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relheight=1,relwidth=1)

        frame=Frame(self.root,bg='white')
        frame.place(x=450,y=100,width=800,height=550)

        register_lbl=Label(frame,text="Register Here",font=("times new roman",25,"bold"),fg="blue")
        register_lbl.place(x=20,y=20)

        fname=Label(frame,text="First Name",font=("times new roman",20,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=135,width=250)

        Lname=Label(frame,text="Last Name",font=("times new roman",20,"bold"),bg="white")
        Lname.place(x=370,y=100)

        Lname_entry=ttk.Entry(frame,textvariable=self.lname,font=("times new roman",15,"bold"))
        Lname_entry.place(x=370,y=135,width=250)

        email=Label(frame,text="Email",font=("times new roman",20,"bold"),bg="white")
        email.place(x=50,y=180)

        email_entry=ttk.Entry(frame,textvariable=self.email,font=("times new roman",15,"bold"))
        email_entry.place(x=50,y=220,width=250)

        cnt=Label(frame,text="Contact Number",font=("times new roman",20,"bold"),bg="white")
        cnt.place(x=370,y=180)

        cnt_entry=ttk.Entry(frame,textvariable=self.cont,font=("times new roman",15,"bold"))
        cnt_entry.place(x=370,y=220,width=250)

        SQ_que=Label(frame,text="Security Quetions",font=("times new roman",20,"bold"),bg="white")
        SQ_que.place(x=50,y=270)

        self.combo_sec=ttk.Combobox(frame,textvariable=self.seqQ,font=("times new roman",15,"bold"),state="read only")
        self.combo_sec["values"]=("Select","Your Birth Place","Your Pet Name")
        self.combo_sec.place(x=50,y=310,width=250)
        self.combo_sec.current(0)

        

        SQ_ans=Label(frame,text="Security Answer",font=("times new roman",20,"bold"),bg="white")
        SQ_ans.place(x=370,y=270)

        SQ_ans_entry=ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=self.seqA)
        SQ_ans_entry.place(x=370,y=310,width=250)

        

        pwd=Label(frame,text="PassWord",font=("times new roman",20,"bold"),bg="white")
        pwd.place(x=50,y=360)

        self.text_pwd=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.text_pwd.place(x=50,y=400,width=250)

        confirm_pwd=Label(frame,text="Confirm PassWord",font=("times new roman",20,"bold"),bg="white")
        confirm_pwd.place(x=390,y=360)

        self.textconfirm=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.textconfirm.place(x=390,y=400,width=250)

        checkbtn=Checkbutton(frame,text="I Agree The Terms & Conditions",variable=self.chec_v,font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=430)


        b1=Button(frame,text="Register",font=("times new roman",15,"bold"),command=self.register_data,cursor="hand2",bg="red",fg="White")
        b1.place(x=50,y=470,width=300)

        b2=Button(frame,text="Login",font=("times new roman",15,"bold"),cursor="hand2",bg="red",fg="White")
        b2.place(x=390,y=470,width=300)

    def register_data(self):
        if self.fname.get()=="" or self.email.get()=="" or self.seqQ.get()=="Select":
            messagebox.showerror("Error","All field Required")
        elif self.text_pwd.get()!=self.textconfirm.get():
            messagebox.showerror("Error","Password and Confirm Password Must Be Same")
        elif self.chec_v.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms & Conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
            my_cur=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.email.get(),)
            my_cur.execute(query,value)
            row=my_cur.fetchone()
            if row !=None:
                messagebox.showerror("Error","User Already Exists")
            else:
                my_cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(self.fname.get(),self.lname.get(),self.cont.get(),self.email.get(),self.seqQ.get(),self.seqA.get(),self.text_pwd.get()))
            
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successful")


if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()