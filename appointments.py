from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

## create table schedule(id int,name varchar(100),purpose varchar(100),mobile int,gender varchar(100),email varchar(100),visited varchar(100));
class appointment:
    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1295x550+230+220")

          #variable
        self.var_id=StringVar()
        x=random.randint(100,200)
        self.var_id.set(str(x))

        self.var_name=StringVar()
        self.var_purpose=StringVar()
        self.var_mobile=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_visited=StringVar()



        #title
        lbl_title=Label(self.root,text="APPOINTMENTS",font=("times new roman",18,"bold"),bg="light sky blue",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #label left
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Appointment Details",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)


        #id
        patient_no=Label(labelframeleft,text="Patient ID",font=("times new roman",12,"bold"),padx=2,pady=6)
        patient_no.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_id,width=29,font=("times new roman",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)


         #name
        patient_name=Label(labelframeleft,font=("ariel",12,"bold"),text="Patient Name:",padx=2,pady=6)
        patient_name.grid(row=1,column=0,sticky=W)

        name=ttk.Entry(labelframeleft,textvariable=self.var_name,font=("times new roman",13,"bold"),width=29)
        name.grid(row=1,column=1)

         #purpose of appointment 
        purpose=Label(labelframeleft,font=("ariel",12,"bold"),text="Purpose:",padx=2,pady=6)
        purpose.grid(row=2,column=0,sticky=W)
        
        name=ttk.Entry(labelframeleft,textvariable=self.var_purpose,font=("times new roman",13,"bold"),width=29)
        name.grid(row=2,column=1)

        #mobile no
        patient_mobno=Label(labelframeleft,font=("ariel",12,"bold"),text="Mobile No:",padx=2,pady=6)
        patient_mobno.grid(row=3,column=0,sticky=W)
        
        name=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("times new roman",13,"bold"),width=29)
        name.grid(row=3,column=1)

        #gender
        la_gender=Label(labelframeleft,font=("ariel",12,"bold"),text="Gender",padx=2,pady=6)
        la_gender.grid(row=4,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("ariel",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=4,column=1)

        
        #email
        la_email=Label(labelframeleft,font=("ariel",12,"bold"),text="Email:",padx=2,pady=6)
        la_email.grid(row=5,column=0,sticky=W)
        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("times new roman",13,"bold"),width=29)
        txtemail.grid(row=5,column=1)

        #previously visited or not
        la_visited=Label(labelframeleft,font=("ariel",12,"bold"),text="Previously visited",padx=2,pady=6)
        la_visited.grid(row=6,column=0,sticky=W)
        combo_visit=ttk.Combobox(labelframeleft,textvariable=self.var_visited,font=("ariel",10,"bold"),width=27,state="readonly")
        combo_visit["value"]=("Yes", "No")
        combo_visit.current(0)
        combo_visit.grid(row=6,column=1)

        ##buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=370,width=412,height=40)

        btnadd=Button(btn_frame,text="Add",command=self.insert,font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=9)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.delete,font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=9)
        btnreset.grid(row=0,column=3,padx=1)


        ##searchh
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Data",padx=2,font=("times new roman",12,"bold"))
        table_frame.place(x=435,y=50,width=860,height=460)

        searchby=Label(table_frame,font=("ariel",12,"bold"),text="Search",bg="light skyblue",fg="white")
        searchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("ariel",10,"bold"),width=20,state="readonly")
        combo_search["value"]=("id", "name","mobile")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(table_frame,textvariable=self.txt_search,font=("times new roman",13,"bold"),width=24)
        txtsearch.grid(row=0,column=2,padx=2)

        btnsearch=Button(table_frame,text="Search",command=self.search,font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=12)
        btnsearch.grid(row=0,column=3,padx=1)

        btnshow=Button(table_frame,text="Show",command=self.fetch_data,font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=12)
        btnshow.grid(row=0,column=4,padx=1)

        
        ### right table
        data_frame=Frame(table_frame,bd=2,relief=RIDGE)
        data_frame.place(x=0,y=50,width=860,height=350)

        scrollx=ttk.Scrollbar(data_frame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(data_frame,orient=VERTICAL)

        self.patient_data=ttk.Treeview(data_frame,column=("id","name","purpose","mobile","gender","email","visited"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.patient_data.xview)
        scrolly.config(command=self.patient_data.yview)


        self.patient_data.heading("id",text="Patient ID")
        self.patient_data.heading("name",text="Patient name")
        self.patient_data.heading("purpose",text="Purpose")
        self.patient_data.heading("mobile",text="Mobile No")
        self.patient_data.heading("gender",text="Gender")
        self.patient_data.heading("email",text="Email")
        self.patient_data.heading("visited",text="Visited")

        self.patient_data["show"]="headings"

        self.patient_data.column("name",width=80)
        self.patient_data.column("purpose",width=80)
        self.patient_data.column("mobile",width=80)
        self.patient_data.column("gender",width=80)
        self.patient_data.column("email",width=80)
        self.patient_data.column("visited",width=80)

        self.patient_data.pack(fill=BOTH,expand=1)
        self.patient_data.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def insert(self):
        if self.var_mobile.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","All Fields Required")
        else:
            #try:
            con=mysql.connector.connect(host="localhost",username="root",password="password",database="management")
            cursor=con.cursor()
            cursor.execute("insert into schedule values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_id.get(),
                                                                                    self.var_name.get(),
                                                                                    self.var_purpose.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_visited.get()
                                                                                ))
            cursor.execute("commit")
            self.fetch_data()
            messagebox.showinfo("success","Data Added",parent=self.root)
            con.close()
            #except Exception as es:
            #   messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",username="root",password="password",database="management")
        cursor=con.cursor()
        cursor.execute("select * from schedule")
        rows=cursor.fetchall()
        if len(rows)!=0:
           self.patient_data.delete(*self.patient_data.get_children())
           for i in rows:
                self.patient_data.insert("",END,values=i)
        con.commit()
        con.close()

    def get_cursor(self,event=""):
        cursor_row=self.patient_data.focus()
        content=self.patient_data.item(cursor_row)
        row=content["values"]
        self.var_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_purpose.set(row[2]),
        self.var_mobile.set(row[3]),
        self.var_gender.set(row[4]),
        self.var_email.set(row[5]),
        self.var_visited.set(row[6])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Enter mobile no",parent=self.root)
        else:
            con=mysql.connector.connect(host="localhost",username="root",password="password",database="management")
            cursor=con.cursor()
            cursor.execute("update schedule set name=%s,purpose=%s,mobile=%s,gender=%s,Email=%s,Visited=%s where id=%s",(

                                                                                                                                        self.var_name.get(),
                                                                                                                                        self.var_purpose.get(),
                                                                                                                                        self.var_mobile.get(),
                                                                                                                                        self.var_gender.get(),
                                                                                                                                        self.var_email.get(),
                                                                                                                                        self.var_visited.get(),
                                                                                                                                        self.var_id.get()                                                                                
        ))
        con.commit()
        self.fetch_data()
        con.close()
        messagebox.showinfo("Update","Customer details has been updated",parent=self.root)

    def delete(self):
        delete=messagebox.askyesno("message","Confirm deletion",parent=self.root)
        if delete>0:
            con=mysql.connector.connect(host="localhost",username="root",password="password",database="management")
            cursor=con.cursor()
            query="delete from schedule where id=%s"
            value=(self.var_id.get(),)
            cursor.execute(query,value)
        else:
            if not delete:
                return
        con.commit()
        self.fetch_data()
        con.close()

    def reset(self):
        #self.var_id.set(""),
        self.var_name.set(""),
        #self.var_gender.set(""),
        self.var_mobile.set(""),
        #self.var_visited.set(""),
        self.var_email.set(""),
        self.var_visited.set("")

        x=random.randint(100,200)
        self.var_id.set(str(x))

    def search(self):
        con=mysql.connector.connect(host="localhost",username="root",password="password",database="management")
        cursor=con.cursor()
        cursor.execute("select * from schedule where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.patient_data.delete(*self.patient_data.get_children())
            for i in rows:
                self.patient_data.insert("",END,values=i)
            con.commit()
        con.close()
    

    

     







if __name__=="__main__":
    root=Tk()
    obj=appointment(root)
    root.mainloop()