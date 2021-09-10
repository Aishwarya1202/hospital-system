from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from patient import patient_window
from appointments import appointment
from staff import doctor
from details import about

class hospitalmanagement:
    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1550x800+0+0")

        #banner
        img1=Image.open(r"C:\Users\Aishwarya\Desktop\hospital\images\17th.jpg")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        #logo
        img2=Image.open(r"C:\Users\Aishwarya\Desktop\hospital\images\logo2.jpg")
        img2=img2.resize((100,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=100)

        #title under banner
        lbl_title=Label(self.root,text="HOSPITAL SYSTEM",font=("times new roman",40,"bold"),bg="light sky blue",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        # window
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #left part
        left_part=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="light sky blue",fg="white",bd=4,relief=RIDGE)
        left_part.place(x=0,y=0,width=230)

        # left window !!!!!!! check height
        option_frame=Frame(main_frame,bd=4,relief=RIDGE)
        option_frame.place(x=0,y=35,width=230,height=300)

        adm_btn=Button(option_frame,text="PATIENTS",command=self.patient_details,width=22,height=2,font=("times new roman",14,"bold"),bg="light sky blue",fg="white",bd=0, cursor="arrow")
        adm_btn.grid(row=0,column=0,pady=1)

        appoin_btn=Button(option_frame,text="APPOINTMENTS",command=self.appoint_details,width=22,height=2,font=("times new roman",14,"bold"),bg="light sky blue",fg="white",bd=0, cursor="arrow")
        appoin_btn.grid(row=1,column=0,pady=1)

        doctors_btn=Button(option_frame,text="DOCTORS",command=self.details_staff,width=22,height=2,font=("times new roman",14,"bold"),bg="light sky blue",fg="white",bd=0, cursor="arrow")
        doctors_btn.grid(row=2,column=0,pady=1)

        info_btn=Button(option_frame,text="ABOUT",command=self.about_hospital,width=22,height=2,font=("times new roman",14,"bold"),bg="light sky blue",fg="white",bd=0, cursor="arrow")
        info_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(option_frame,text="LOGOUT",command=self.logout,width=22,height=2,font=("times new roman",14,"bold"),bg="light sky blue",fg="white",bd=0, cursor="arrow")
        logout_btn.grid(row=4,column=0)

        

        #right side @@ change image
        img3=Image.open(r"C:\Users\Aishwarya\Desktop\hospital\images\15th.jpg")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)

        ##left bottm
        img4=Image.open(r"C:\Users\Aishwarya\Desktop\hospital\images\third.jpg")
        img4=img4.resize((225,180),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=325,width=230,height=180)







    def patient_details(self):
        self.new_window=Toplevel(self.root)
        self.app=patient_window(self.new_window)

    def appoint_details(self):
        self.new_window=Toplevel(self.root)
        self.app=appointment(self.new_window)

    def details_staff(self):
        self.new_window=Toplevel(self.root)
        self.app=doctor(self.new_window)

    def about_hospital(self):
        self.new_window=Toplevel(self.root)
        self.app=about(self.new_window)

    def logout(self):
        self.root.destroy()






if __name__=="__main__":
    root=Tk()
    obj=hospitalmanagement(root)
    root.mainloop()

