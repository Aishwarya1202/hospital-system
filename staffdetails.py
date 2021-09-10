from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk

class doctor:
    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1295x550+230+220")

        #title
        lbl_title=Label(self.root,text="STAFF DETAILS",font=("times new roman",18,"bold"),bg="light sky blue",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #label left
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="STAFF DETAILS",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=520,height=350)

        #doctor name
         #name
        staff_name=Label(labelframeleft,font=("ariel",12,"bold"),text="Staff Name:",padx=2,pady=6)
        staff_name.grid(row=0,column=0,sticky=W)

        name=ttk.Entry(labelframeleft,font=("times new roman",13,"bold"),width=29)
        name.grid(row=0,column=1)

        #designation
        designation=Label(labelframeleft,font=("ariel",12,"bold"),text="Designation",padx=2,pady=6)
        designation.grid(row=1,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,font=("ariel",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Senior Doctor", "Junior Doctor", "Nurse")
        combo_gender.current(0)
        combo_gender.grid(row=1,column=1)

        #specialisation
        spaciality=Label(labelframeleft,font=("ariel",12,"bold"),text="Specialisation:",padx=2,pady=6)
        spaciality.grid(row=2,column=0,sticky=W)
        
        name=ttk.Entry(labelframeleft,font=("times new roman",13),width=29)
        name.grid(row=2,column=1)

        #mobile no
        patient_mobno=Label(labelframeleft,font=("ariel",12,"bold"),text="Mobile No:",padx=2,pady=6)
        patient_mobno.grid(row=3,column=0,sticky=W)
        
        name=ttk.Entry(labelframeleft,font=("times new roman",13,"bold"),width=29)
        name.grid(row=3,column=1)

         ##buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=240,width=412,height=40)

        btnadd=Button(btn_frame,text="Add",font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=12)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=12)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=12)
        btndelete.grid(row=0,column=2,padx=1)

        
        ##searchh
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Staff Details",padx=2,font=("times new roman",12,"bold"))
        table_frame.place(x=550,y=55,width=600,height=350)

        scrollx=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.patient_data=ttk.Treeview(table_frame,column=("name","designation","specialisation","mobile"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.patient_data.xview)
        scrolly.config(command=self.patient_data.yview)

        self.patient_data.heading("name",text="Staff name")
        self.patient_data.heading("designation",text="Desigation")
        self.patient_data.heading("specialisation",text="Specialisation")
        self.patient_data.heading("mobile",text="Mobile no")
        
        self.patient_data["show"]="headings"

        self.patient_data.column("name",width=80)
        self.patient_data.column("designation",width=80)
        self.patient_data.column("specialisation",width=80)
        self.patient_data.column("mobile",width=80)
    
        self.patient_data.pack(fill=BOTH,expand=1)









if __name__=="__main__":
    root=Tk()
    obj=doctor(root)
    root.mainloop()