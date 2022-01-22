from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
from open import hotel_class


def main():
    win=Tk()
    app=Login_Win(win)
    win.mainloop()
class Login_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        

        self.bg=ImageTk.PhotoImage(file=r"images\login.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"images\img1.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbl_image1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lbl_image1.place(x=730,y=175,width=100,height=100)


        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=100,y=100)

        username=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.password=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.password.place(x=40,y=250,width=270)

        img2=Image.open(r"images\email.jps.jpg")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbl_image2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lbl_image2.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"images\pass.jpg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbl_image3=Label(image=self.photoimage3,bg="white",borderwidth=0)
        lbl_image3.place(x=650,y=393,width=25,height=25)

        loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),command=self.login,bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        regbtn=Button(frame,text="Register Now",font=("times new roman",10,"bold"),command=self.register_win,borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        regbtn.place(x=4,y=350,width=160)

        forgotbtn=Button(frame,text="Forgot Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotbtn.place(x=10,y=370,width=160)

    def register_win(self):
        self.new_win=Toplevel(self.root)
        self.app=Register(self.new_win)

    def login(self):
        if self.txtuser.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All Fields Required")
        elif self.txtuser.get()=="a" and self.password.get()=="a":
            messagebox.showinfo("success","Welcome")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
            my_cur=conn.cursor()
            my_cur.execute("select * from register where email=%s and password=%s",(self.txtuser.get(),self.password.get()))
            row=my_cur.fetchone()
            if row!=None:
                self.new_win=Toplevel(self.root)
                self.app=hotel_class(self.new_win)
            else:
                messagebox.showerror("Error","Invalid Email or Password")


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
    main()