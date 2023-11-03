from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")

        title = Label(self.root, text="Student Management System", bd=10, bg="yellow",
                      fg="red", relief=GROOVE, font=("times new roman", 40, "bold") )
        title.pack(side=TOP, fill=X)

    #=======All Variables=====================
        self.rollnoVar = StringVar()
        self.nameVar = StringVar()
        self.emailVar = StringVar()
        self.genderVar = StringVar()
        self.contactVar = StringVar()
        self.dobVar = StringVar()

        self.searchBy = StringVar()
        self.searchTXT = StringVar()

        manageFrame = Frame(self.root, border=4, relief=RIDGE, bg="crimson")
        manageFrame.place(x=20, y=100, width=450, height=580)

    #============ Manage Frame ========================================
        detailFrame = Frame(self.root, border=4, relief=RIDGE, bg="crimson")
        detailFrame.place(x=500, y=100, width=800, height=580)

        m_title = Label(manageFrame, text="Manage Students", bg="crimson", fg="white", font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lblRoll = Label(manageFrame, text="Roll No.", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lblRoll.grid(row=1, column=0, pady=10, padx=20, sticky=W)

        txtRoll = Entry(manageFrame, textvariable=self.rollnoVar, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txtRoll.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        lblName = Label(manageFrame, text="Name.", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lblName.grid(row=2, column=0, pady=10, padx=20, sticky=W)

        txtName = Entry(manageFrame, textvariable=self.nameVar, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txtName.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        lblEmail = Label(manageFrame, text="Email.", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lblEmail.grid(row=3, column=0, pady=10, padx=20, sticky=W)

        txtEmail = Entry(manageFrame, textvariable=self.emailVar, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txtEmail.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        lblGen = Label(manageFrame, text="Gender", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lblGen.grid(row=4, column=0, pady=10, padx=20, sticky=W)

        cmbGen = ttk.Combobox(manageFrame, textvariable=self.genderVar, width=19, font=("times new roman", 15, "bold"))
        cmbGen["values"] = ("male", "female", "other")
        cmbGen.grid(row=4, column=1, pady=10, padx=10, sticky=W)

        lblCont = Label(manageFrame, text="Contact", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lblCont.grid(row=5, column=0, pady=10, padx=20, sticky=W)

        txtCont = Entry(manageFrame, textvariable=self.contactVar, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txtCont.grid(row=5, column=1, padx=10, pady=10, sticky=W)

        lblDoB = Label(manageFrame, text="D.O.B", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lblDoB.grid(row=6, column=0, pady=10, padx=20, sticky=W)

        txtDoB = Entry(manageFrame, textvariable=self.dobVar, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txtDoB.grid(row=6, column=1, padx=10, pady=10, sticky=W)

        lblAdd = Label(manageFrame, text="Address", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lblAdd.grid(row=7, column=0, pady=10, padx=10, sticky=W)

        self.txtAdd = Text(manageFrame, width=30, height=4, font=("", 10))
        self.txtAdd.grid(row=7, column=1, padx=10, pady=10, sticky=W)

    #=======Button Frame=
        btnFrame = Frame(manageFrame, bd=4, relief=RIDGE, bg="crimson")
        btnFrame.place(x=15, y=515, width=420)

        Addbtn = Button(btnFrame, text="Add", width=10, command=self.addStudents).grid(row=0, column=0, padx=10, pady=10)
        Updatebtn = Button(btnFrame, text="Update", width=10, command=self.updateData).grid(row=0, column=1, padx=10, pady=10)
        Deletebtn = Button(btnFrame, text="Delete", width=10, command=self.deleteData).grid(row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(btnFrame, text="Clear", width=10, command=self.clear).grid(row=0, column=3, padx=10, pady=10)

    # ============ Detail Frame ========================================
        detailFrame = Frame(self.root, border=4, relief=RIDGE, bg="crimson")
        detailFrame.place(x=500, y=100, width=800, height=580)

        lblSrch = Label(detailFrame, text="Search By", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lblSrch.grid(row=0, column=0, pady=10, padx=20, sticky=W)

        cmbSrch = ttk.Combobox(detailFrame, textvariable=self.searchBy, width=10, font=("times new roman", 13, "bold"))
        cmbSrch["values"] = ("RollNo", "Name", "Contact")
        cmbSrch.grid(row=0, column=1, pady=10, padx=10, sticky=W)

        txtSrch = Entry(detailFrame, textvariable=self.searchTXT, font=("times new roman", 13, "bold"), bd=5, relief=GROOVE)
        txtSrch.grid(row=0, column=2, pady=10, padx=20, sticky=W)

        searchBtn = Button(detailFrame, text="Search", width=10, pady=5, command=self.searchData).grid(row=0,column=3,padx=10,pady=10)
        showAllBtn = Button(detailFrame, text="Show All", width=10, pady=5, command=self.fetchData).grid(row=0,column=4,padx=10,pady=10)

    #========Table Frame===============================
        tableFrame = Frame(detailFrame, bd=4, relief=RIDGE, bg="crimson")
        tableFrame.place(x=10, y=70, width=760, height=500)

        X_scroba = Scrollbar(tableFrame, orient=HORIZONTAL)
        Y_scroba = Scrollbar(tableFrame, orient=VERTICAL)
        self.studentTable = ttk.Treeview(tableFrame, columns=("roll","name","email","gender","contact","dob","address"), xscrollcommand=X_scroba.set, yscrollcommand=Y_scroba.set)
        X_scroba.pack(side=BOTTOM, fill=X)
        Y_scroba.pack(side=RIGHT, fill=Y)
        X_scroba.config(command=self.studentTable.xview)
        Y_scroba.config(command=self.studentTable.yview)
        self.studentTable.heading("roll", text="Roll No")
        self.studentTable.heading("name", text="Name")
        self.studentTable.heading("email", text="Email")
        self.studentTable.heading("gender", text="Gender")
        self.studentTable.heading("contact", text="Contact")
        self.studentTable.heading("dob", text="D.O.B")
        self.studentTable.heading("address", text="Address")
        self.studentTable["show"]="headings"
        self.studentTable.column("roll", width=100)
        self.studentTable.column("name", width=100)
        self.studentTable.column("email", width=100)
        self.studentTable.column("gender", width=100)
        self.studentTable.column("contact", width=100)
        self.studentTable.column("dob", width=100)
        self.studentTable.column("address", width=150)
        self.studentTable.pack(fill=BOTH, expand=True)
        self.studentTable.bind("<ButtonRelease-1>", self.getCursor)

        self.fetchData()
    def addStudents(self):
        if self.rollnoVar.get() == "" or self.nameVar.get() == "":
            messagebox.showerror("Error", "All fields are required!!!")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="myProject1")
            cur = con.cursor()
            cur.execute("insert into Students values(%s,%s,%s,%s,%s,%s,%s)",
                        (self.rollnoVar.get(),
                        self.nameVar.get(),
                        self.emailVar.get(),
                        self.genderVar.get(),
                        self.contactVar.get(),
                        self.dobVar.get(),
                        self.txtAdd.get('1.0', END)
                        ))
            con.commit()
            self.fetchData()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been inserted")
    def fetchData(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="myProject1")
        cur = con.cursor()
        cur.execute("select * from Students")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.studentTable.delete(*self.studentTable.get_children())
            for row in rows:
                self.studentTable.insert("", END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.rollnoVar.set("")
        self.nameVar.set("")
        self.emailVar.set("")
        self.genderVar.set("")
        self.contactVar.set("")
        self.dobVar.set("")
        self.txtAdd.delete("1.0", END)

    def getCursor(self, e):
        cursorRow = self.studentTable.focus()
        contents = self.studentTable.item(cursorRow)
        row = contents["values"]
        self.rollnoVar.set(row[0])
        self.nameVar.set(row[1])
        self.emailVar.set(row[2])
        self.genderVar.set(row[3])
        self.contactVar.set(row[4])
        self.dobVar.set(row[5])
        self.txtAdd.delete("1.0", END)
        self.txtAdd.insert(END, row[6])

    def updateData(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="myProject1")
        cur = con.cursor()
        cur.execute("Update Students set name=%s, email=%s, gender=%s, contact=%s, dob=%s, address=%s where rollNo=%s",
                    (
                     self.nameVar.get(),
                     self.emailVar.get(),
                     self.genderVar.get(),
                     self.contactVar.get(),
                     self.dobVar.get(),
                     self.txtAdd.get('1.0', END),
                     self.rollnoVar.get()
                     ))
        con.commit()
        self.fetchData()
        self.clear()
        con.close()

    def deleteData(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="myProject1")
        cur = con.cursor()
        cur.execute("Delete from Students where rollNo=%s", self.rollnoVar.get())
        con.commit()
        self.fetchData()
        self.clear()
        con.close()

    def searchData(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="myProject1")
        cur = con.cursor()
        cur.execute("select * from Students where "+str(self.searchBy.get())+" LIKE '%"+str(self.searchTXT.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.studentTable.delete(*self.studentTable.get_children())
            for row in rows:
                self.studentTable.insert("", END, values=row)
            con.commit()
        con.close()

root = Tk()
ex = Student(root)
root.geometry("1350x750+0+0")
root.mainloop()

