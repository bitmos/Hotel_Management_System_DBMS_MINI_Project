from tkinter import *
from PIL import Image,ImageTk 
from customer import Cust_win
from room import RoomBooking
class HotelManagementSystem(send):
    def __init__(self,root):
        print(self.var_hotel)
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #header image
        # img1=Image.open(r"images\Hotel-Booking.jpg")
        # img1=img1.resize((1530,140),Image.ANTIALIAS)
        # self.photoimage1=ImageTk.PhotoImage(img1)

        # labelimg1=Label(self.root,image=self.photoimage1,bd=4,relief=RIDGE)
        # labelimg1.place(x=0,y=0,width=1550,height=200)

        #title
        

   





if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()