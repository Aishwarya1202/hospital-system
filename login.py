from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from hosptal import hospitalmanagement
from staff import doctor
from details import about

#from hosptal import hospitalmanagement


def main():
    var=Tk()
    app=login_window(var)
    var.mainloop()


class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Aishwarya\Desktop\hospital\images\login_bg.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="gray")
        frame.place(x=500,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Aishwarya\Desktop\hospital\images\login_1.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="gray",borderwidth=0)
        lblimg1.place(x=620,y=175,width=100,height=100)

        get_str=Label(frame,text="LOGIN", font=("times new roman",20,"bold"),fg="black",bg="gray")
        get_str.place(x=120,y=100)

        username=lbl=Label(frame,text="USERNAME:",font=("times new roman",15,"bold"),fg="black",bg="gray")
        username.place(x=50,y=155)

        self.txtuser=Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="PASSWORD:",font=("times new roman",15,"bold"),fg="black",bg="gray")
        password.place(x=50,y=218)

        self.txtpassword=Entry(frame,font=("times new roman",15,"bold"))
        self.txtpassword.place(x=40,y=240,width=270)


        ##########login button here
        loginbtn=Button(frame,text="LOGIN",command=self.login,font=("times new roman",20,"bold"),bd=3,relief=RIDGE,fg="White",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        
        ###########
        regbtn=Button(frame,text="New Registration",command=self.r_window,font=("times new roman",12),borderwidth=0,relief=RIDGE,fg="black",bg="gray",activeforeground="white",activebackground="gray")
        regbtn.place(x=10,y=350,width=160)

        forgotpassword=Button(frame,text="Forgot Password",command=self.forgot_password,font=("times new roman",12),borderwidth=0,relief=RIDGE,fg="black",bg="gray",activeforeground="white",activebackground="gray")
        forgotpassword.place(x=10,y=370,width=160)


    def r_window(self):
        self.new_window=Toplevel(self.root)
        self.app=register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpassword.get()=="":
            messagebox.showerror("Error","All feilds are required")
        elif self.txtuser.get()=="user" and self.txtpassword.get()=="password":
            messagebox.showinfo("Success","Login successful")
        else:
            con=mysql.connector.connect(host="localhost",username="root",password="password",database="management")
            cursor=con.cursor()
            cursor.execute("select * from register where email=%s and pwd=%s",(
                self.txtuser.get(),
                self.txtpassword.get()

            ))
            row=cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid credentials")
            else:
                open_main=messagebox.askyesno("ask","Access to registerd user")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                    self.app=hospitalmanagement(self.new_window)
                else:
                    if not open_main:
                        return
            con.commit()
            con.close()


############reset pwd
def reset(self):
    if self.combo_securityq.get()=="Select":
        messagebox.showerror("error","Invalid credentials")
    else:
        open_main=messagebox.askyesno("ask","To registerd user only")
        if open_main>0:
                self.new_window=Toplevel(self.root)
                self.app=hospitalmanagement(self.new_window)
        else:
            if not open_main:
                return
        con.commit()
        con.close()

    def reset_pwd(self):
        if self.combo_sequrityq.get()=="select":
            messagebox.showerror("error","Select security question",parent=self.root1)
        elif self.seq_entry.get()=="":
            messagebox.showerror("error","please enter answer",parent=self.root1)
        elif self.newpwd.get()=="":
             messagebox.showerror("error","please enter password",parent=self.root1)
        else:
            con=mysql.connector.connect(host="localhost",username="root",password="password",database="management")
            cursor=con.cursor()
            query=("select * from register where email=%s and securityq=%s and securitya=%s")
            value=(self.txtuser.get(),self.combo_securityq.get(),self.seq_entry)
            cursor.execute(query,value)
            row=cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root1)
            else:
                query=("update register set pwd=%s where email=%s")
                value=(self.newpwd_entry.get(),self.txtuser.get())
                cursor.execute(query,value)
                con.commit()
                con.close()
                messagebox.showinfo("info","Password Updated!",parent=self.root1)
                self.root1.destroy()



###############

    def forgot_password(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Enter Email to reset password")
        else:
            con=mysql.connector.connect(host="localhost",username="root",password="password",database="management")
            cursor=con.cursor()
            query=("info","select * from register where email=%s")
            value=(self.txtuser.get(),)
            cursor.execute(query,value)
            row=cursor.fetchone()
            print(row)

            if row==None:
                messagebox.showerror("error","Plese enter valid username")
            else:
                conn.close()
                self.root1=Toplevel()
                self.root1.title=("Forgot password")
                self.root1.geometry("340x450+610+170")
                

                l=Label(self.root1,text="Forgot Password",font=("times new roman",15,"bold"),fg="black",bg="gray")
                l.Place(x=0,y=10,relwidth=1)

                securityq=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="gray")
                securityq.place(x=50,y=80)
                self.combo_sq=ttk.Combobox(frame,font=("ariel",12,"bold"),width=27,state="readonly")
                self.combo_sq["value"]=("select", "Your nickname", "Your childhood friend name","Your School name")
                self.combo_sq.place(x=50,y=110,width=250)
                self.combo_sq.current(0)
                
                securitya=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="gray")
                securitya.place(x=50,y=150)

                seq_entry=Entry(self.root2,font=("times new roman",15,"bold"))
                seq_entry.place(x=50,y=180,width=250)

                nwpwd=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="gray")
                nwpwd.place(x=50,y=220)

                newpwd_entry=Entry(self.root2,font=("times new roman",15,"bold"))
                newpwd_entry.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",font=("times new roman",15,"bold"),fg="black",bg="gray")
                btn.place(x=100,y=290)


                




class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")


        ##variable
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_securityq=StringVar()
        self.var_securitya=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Aishwarya\Desktop\hospital\images\login_bg.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        ##frame
        frame=Frame(self.root,bg="gray")
        frame.place(x=350,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",15,"bold"),fg="gray",bg="black")
        register_lbl.place(x=20,y=20)


        ##name and other entries
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="gray")
        fname.place(x=50,y=100)

        fname_entry=Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="gray")
        lname.place(x=50,y=160)

        lname_entry=Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        lname_entry.place(x=50,y=190,width=250)

        contact=Label(frame,text="Mobile No:",font=("times new roman",15,"bold"),bg="gray")
        contact.place(x=50,y=220)

        contact_entry=Entry(frame,textvariable=self.var_mobile,font=("times new roman",15,"bold"))
        contact_entry.place(x=50,y=250,width=250)

        Email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="gray")
        Email.place(x=50,y=280)

        email_entry=Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        email_entry.place(x=50,y=310,width=250)

        securityq=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="gray")
        securityq.place(x=50,y=340)
        self.combo_sq=ttk.Combobox(frame,textvariable=self.var_securityq,font=("ariel",12,"bold"),width=27,state="readonly")
        self.combo_sq["value"]=("select", "Your nickname", "Your childhood friend name","Your School name")
        self.combo_sq.place(x=50,y=370,width=250)
        self.combo_sq.current(0)
        
        securitya=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="gray")
        securitya.place(x=50,y=400)

        seq_entry=Entry(frame,textvariable=self.var_securitya,font=("times new roman",15,"bold"))
        seq_entry.place(x=50,y=430,width=250)
        
        pwd1=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="gray")
        pwd1.place(x=500,y=340)

        pwd1_entry=Entry(frame,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
        pwd1_entry.place(x=500,y=370,width=250)

        cpwd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="gray")
        cpwd.place(x=500,y=400)

        cpwd_entry=Entry(frame,textvariable=self.var_cpwd,font=("times new roman",15,"bold"))
        cpwd_entry.place(x=500,y=430,width=250)


        btnregister=Button(frame,text="Register",command=self.register_data,font=("times new roman",20,"bold"),bg="black",fg="gray",width=9)
        btnregister.place(x=50,y=490,width=200,height=45)

        btnlogin=Button(frame,text="Login",command=self.return_login,font=("times new roman",20,"bold"),bg="black",fg="gray",width=9)
        btnlogin.place(x=500,y=490,width=200,height=45)


    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        elif self.var_pwd.get()!=self.var_cpwd.get():
            messagebox.showerror("Error","Password dosent match")
        else:
            con=mysql.connector.connect(host="localhost",username="root",password="password",database="login")
            cursor=con.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            cursor.execute(query,value)
            row=cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","This email is already registered. Try Login!")
            else:
                cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_mobile.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityq.get(),
                                                                                        self.var_securitya.get(),
                                                                                        self.var_pwd.get(),
                                                                                        self.var_cpwd.get()
                                                                                    ))
            con.commit()
            con.close()
            messagebox.showinfo("Success","Registerd!")

    def return_login(self):
        self.root.destroy()


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
    main()