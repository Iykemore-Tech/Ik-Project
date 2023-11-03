import os, tempfile, smtplib
from tkinter import *
from tkinter import ttk
import random
import controller as controller
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql

billnumber = random.randint(500, 1000)

class Firstpage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="Tomato")

        self.label1 = Label(self, text="Emporium Supermarket Management System",fg='white', font=("Arial Bold",25),bg="Tomato", bd=4)
        self.label1.place(x=150, y=60)

        self.border = LabelFrame(self, text="Login", bg='deep sky blue', bd=8, font=("Arial, Bold", 18))
        self.border.pack(fill=BOTH, expand=True, pady=150, padx=100)

        self.lbl1 = Label(self.border, text="Username", font=("Arial Bold", 15), bg='deep sky blue')
        self.lbl1.place(x=50, y=20)
        self.Ent1 = Entry(self.border, width=30, bd=5)
        self.Ent1.place(x=180, y=20)

        self.lbl2 = Label(self.border, text="Password", font=("Arial Bold", 15), bg='deep sky blue')
        self.lbl2.place(x=50, y=80)
        self.Ent2 = Entry(self.border, show="*", width=30, bd=5)
        self.Ent2.place(x=180, y=80)

        self.button = Button(self.border, text="Login", font=("Arial Bold", 15),command=self.verify)
        self.button.place(x=300, y=140)

    def verify(self):
        if self.Ent1.get() == '' and self.Ent2.get() == '':
            messagebox.showerror("Error", "Please, All Fields Are Required")

        elif self.Ent1.get() == "" and self.Ent2.get() != "":
            messagebox.showerror("Error", "Please, username cannot be empty")

        elif self.Ent1.get() != "" and self.Ent2.get() == "":
            messagebox.showerror("Error", "Please, password cannot be empty")

        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="myProject1")
                cur = con.cursor()
                cur.execute("select * from Users where username=%s AND password=%s",(self.Ent1.get(),self.Ent2.get()))
                rows = cur.fetchall()
                if len(rows) != 0:
                    messagebox.showinfo("Success", "Login Successful")
                    self.controller.showFrame(Secondpage)
                else:
                    messagebox.showerror('Error', 'Invalid username and password, Please Try Again')
                con.commit()
                self.clear()
                con.close()
            except:
                messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')

    def clear(self):
        self.Ent1.delete(0, END)
        self.Ent2.delete(0, END)

class Secondpage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)



        manageFrame = Frame( self, border=4, relief=RIDGE, bg="crimson")
        manageFrame.place(x=0, y=40, width=300, height=500)

        self.label = Label(self, text="SUPERMARKET DASHBOARD", font=("Arial Bold", 15), bd=4, bg="yellow", relief=RIDGE)
        self.label.pack(fill=X, side=TOP)

        self.button = Button(manageFrame, text="Users", font=("Arial Bold", 15),width=15,
                             command=lambda: controller.showFrame(Thirdpage))
        self.button.place(x=50, y=50)

        self.button = Button(self, text="Products", font=("Arial Bold", 15),width=15,
                             command=lambda: controller.showFrame(Fourthpage))
        self.button.place(x=50, y=170)

        self.button = Button(self, text="Sales", font=("Arial Bold", 15),width=15,
                             command=lambda: controller.showFrame(Fifthpage))
        self.button.place(x=50, y=250)

        self.button = Button(manageFrame, text="Logout", font=("Arial Bold", 15),width=15,
                             command=lambda: controller.showFrame(Firstpage))
        self.button.place(x=50, y=290)

        imageFrame = Frame(self, border=4, relief=RIDGE)

        self.img = Image.open("C:/Users/user/Pictures/sup.png")

        Ik = ImageTk.PhotoImage(self.img)
        label = Label(imageFrame, image=Ik)

        # reference must be stored
        label.image = Ik
        label.place(x=0, y=0)
        #label.pack(expand=1)
        imageFrame.place(x=310, y=40, width=700, height=500)

class Thirdpage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.label = Label(self, text="USERS", font=("Arial Bold", 15), bd=4, bg="yellow", relief=RIDGE)
        self.label.pack(fill=X, side=TOP)

    # =======All Variables=====================
        self.userIdvar = StringVar()
        self.nameVar = StringVar()
        self.emailVar = StringVar()
        self.usnameVar = StringVar()
        self.passwdVar = StringVar()
        self.contVar = StringVar()
        self.dobVar = StringVar()
        self.staVar = StringVar()
        self.genVar = StringVar()
        self.searchBy = StringVar()
        self.searchTxt = StringVar()

    # ============ Manage Frame ========================================
        manageFrame = Frame(self, border=4, relief=RIDGE, bg="crimson")
        manageFrame.place(x=0, y=40, width=300, height=500)

        lblUser = Label(manageFrame, text="User Id", bg="crimson", fg="white", font=("times new roman", 10, "bold"))
        lblUser.grid(row=1, column=0, pady=10, padx=10, sticky=W)

        txtUser = Entry(manageFrame, textvariable=self.userIdvar, font=("times new roman", 10, "bold"), bd=5,relief=GROOVE)
        txtUser.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        lblName = Label(manageFrame, text="Name", bg="crimson", fg="white", font=("times new roman", 10, "bold"))
        lblName.grid(row=2, column=0, pady=6, padx=10, sticky=W)

        txtName = Entry(manageFrame, textvariable=self.nameVar, font=("times new roman", 10, "bold"), bd=5,relief=GROOVE)
        txtName.grid(row=2, column=1, padx=10, pady=6, sticky=W)

        lblEmail = Label(manageFrame, text="Email", bg="crimson", fg="white", font=("times new roman", 10, "bold"))
        lblEmail.grid(row=3, column=0, pady=6, padx=10, sticky=W)

        txtEmail = Entry(manageFrame, textvariable=self.emailVar, font=("times new roman", 10, "bold"), bd=5,relief=GROOVE)
        txtEmail.grid(row=3, column=1, padx=10, pady=6, sticky=W)

        lblUsername = Label(manageFrame, text="Username", bg="crimson", fg="white", font=("times new roman", 10, "bold"))
        lblUsername.grid(row=4, column=0, pady=6, padx=10, sticky=W)

        txtUsername = Entry(manageFrame, textvariable=self.usnameVar, font=("times new roman", 10, "bold"), bd=5,
                        relief=GROOVE)
        txtUsername.grid(row=4, column=1, padx=10, pady=6, sticky=W)

        lblPassword = Label(manageFrame, text="Password", bg="crimson", fg="white", font=("times new roman", 10, "bold"))
        lblPassword.grid(row=5, column=0, pady=6, padx=10, sticky=W)

        txtPassword = Entry(manageFrame, textvariable=self.passwdVar, font=("times new roman", 10, "bold"), bd=5,
                        relief=GROOVE)
        txtPassword.grid(row=5, column=1, padx=10, pady=6, sticky=W)

        lblCont = Label(manageFrame, text="Contact", bg="crimson", fg="white", font=("times new roman", 10, "bold"))
        lblCont.grid(row=6, column=0, pady=6, padx=10, sticky=W)

        txtCont = Entry(manageFrame, textvariable=self.contVar, font=("times new roman", 10, "bold"), bd=5,
                        relief=GROOVE)
        txtCont.grid(row=6, column=1, padx=10, pady=6, sticky=W)

        lblDOB = Label(manageFrame, text="D.O.B", bg="crimson", fg="white", font=("times new roman", 10, "bold"))
        lblDOB.grid(row=7, column=0, pady=6, padx=10, sticky=W)

        txtDOB = Entry(manageFrame, textvariable=self.dobVar, font=("times new roman", 10, "bold"), bd=5,relief=GROOVE)
        txtDOB.grid(row=7, column=1, padx=10, pady=6, sticky=W)

        lblSta = Label(manageFrame, text="Status", bg="crimson", fg="white", font=("times new roman", 10, "bold"))
        lblSta.grid(row=8, column=0, pady=6, padx=10, sticky=W)

        cmbSta = ttk.Combobox(manageFrame, textvariable=self.staVar, width=18, font=("times new roman", 10, "bold"))
        cmbSta["values"] = ("Single", "Married", "Not Specify")
        cmbSta.grid(row=8, column=1, pady=10, padx=10, sticky=W)

        lblGender = Label(manageFrame, text="Gender", bg="crimson", fg="white", font=("times new roman", 10, "bold"))
        lblGender.grid(row=9, column=0, pady=6, padx=10, sticky=W)

        cmbGen = ttk.Combobox(manageFrame, textvariable=self.genVar, width=18, font=("times new roman", 10, "bold"))
        cmbGen["values"] = ("male", "female", "other")
        cmbGen.grid(row=9, column=1, pady=10, padx=10, sticky=W)

        lblAdd = Label(manageFrame, text="Address", bg="crimson", fg="white", font=("times new roman", 10, "bold"))
        lblAdd.grid(row=10, column=0, pady=6, padx=10, sticky=W)

        self.txtAdd = Text(manageFrame, width=21, height=4, font=("", 10))
        self.txtAdd.grid(row=10, column=1, padx=10, pady=10, sticky=W)

    # =======Button Frame=
        btnFrame = Frame(manageFrame, bd=4, relief=RIDGE, bg="crimson")
        btnFrame.place(x=0, y=445, width=290)

        Addbtn = Button(btnFrame, text="Add", width=7, command=self.addUser)
        Addbtn.grid(row=0, column=0, padx=6, pady=6)
        Updatebtn = Button(btnFrame, text="Update", width=7, command=self.updateData)
        Updatebtn.grid(row=0, column=1, padx=6,pady=6)
        Deletebtn = Button(btnFrame, text="Delete", width=7, command=self.deleteData)
        Deletebtn.grid(row=0, column=2, padx=6,pady=6)
        Clearbtn = Button(btnFrame, text="Clear", width=7, command=self.clear)
        Clearbtn.grid(row=0, column=3, padx=6, pady=6)

    # ============ Details Frame ========================================
        detailFrame = Frame(self, border=4, relief=RIDGE, bg="crimson")
        detailFrame.place(x=310, y=40, width=800, height=500)

        lblSrch = Label(detailFrame, text="Search By", bg="crimson", fg="white", font=("times new roman", 10, "bold"))
        lblSrch.grid(row=0, column=0, pady=6, padx=10, sticky=W)

        cmbSrch = ttk.Combobox(detailFrame, textvariable=self.searchBy, width=12, font=("times new roman", 10, "bold"))
        cmbSrch["values"] = ("userId", "Name", "Contact")
        cmbSrch.grid(row=0, column=1, pady=6, padx=10, sticky=W)

        txtSrch = Entry(detailFrame, textvariable=self.searchTxt, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        txtSrch.grid(row=0, column=2, pady=6, padx=10, sticky=W)

        searchBtn = Button(detailFrame, text="Search", width=8, pady=5, command=self.searchData)
        searchBtn.grid(row=0, column=3,padx=10, pady=6)
        showAllBtn = Button(detailFrame, text="Show All", width=8, pady=5, command=self.fetchData)
        showAllBtn.grid(row=0,column=4, padx=10,pady=6)
        backBtn = Button(detailFrame, text="Back", width=8, pady=5, command=lambda:controller.showFrame(Secondpage))
        backBtn.grid(row=0, column=5, padx=10,pady=6)

    # ========Table Frame===============================
        tableFrame = Frame(detailFrame, bd=4, relief=RIDGE, bg="crimson")
        tableFrame.place(x=10, y=50, width=620, height=440)

        X_scroba = Scrollbar(tableFrame, orient=HORIZONTAL)
        Y_scroba = Scrollbar(tableFrame, orient=VERTICAL)
        self.userTable = ttk.Treeview(tableFrame,columns=("Id", "name", "email","username","password",
        "contact","status", "dob", "gender", "address"), xscrollcommand=X_scroba.set, yscrollcommand=Y_scroba.set)
        X_scroba.pack(side=BOTTOM, fill=X)
        Y_scroba.pack(side=RIGHT, fill=Y)
        X_scroba.config(command=self.userTable.xview)
        Y_scroba.config(command=self.userTable.yview)
        self.userTable.heading("Id", text="User Id")
        self.userTable.heading("name", text="Name")
        self.userTable.heading("email", text="Email")
        self.userTable.heading("username", text="Username")
        self.userTable.heading("password", text="Password")
        self.userTable.heading("contact", text="Contact")
        self.userTable.heading("dob", text="D.O.B")
        self.userTable.heading("status", text="Status")
        self.userTable.heading("gender", text="Gender")
        self.userTable.heading("address", text="Address")
        self.userTable["show"] = "headings"
        self.userTable.column("Id", width=100)
        self.userTable.column("name", width=100)
        self.userTable.column("email", width=100)
        self.userTable.column("username", width=100)
        self.userTable.column("password", width=100)
        self.userTable.column("contact", width=100)
        self.userTable.column("dob", width=100)
        self.userTable.column("status", width=100)
        self.userTable.column("gender", width=100)
        self.userTable.column("address", width=150)
        self.userTable.pack(fill=BOTH, expand=True)
        self.userTable.bind("<ButtonRelease-1>", self.getCursor)

        self.fetchData()
    def addUser(self):
        if self.userIdvar.get() == "" or self.nameVar.get() == "":
            messagebox.showerror("Error", "All fields are required!!!")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="myProject1")
            cur = con.cursor()
            cur.execute("insert into Users values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (self.userIdvar.get(),
                         self.nameVar.get(),
                         self.emailVar.get(),
                         self.usnameVar.get(),
                         self.passwdVar.get(),
                         self.contVar.get(),
                         self.dobVar.get(),
                         self.staVar.get(),
                         self.genVar.get(),
                         self.txtAdd.get('1.0', END)
                             ))
            con.commit()
            self.fetchData()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been Inserted")
    def fetchData(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="myProject1")
        cur = con.cursor()
        cur.execute("select * from Users")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.userTable.delete(*self.userTable.get_children())
            for row in rows:
                self.userTable.insert("", END, values=row)
            con.commit()
        con.close()
    def getCursor(self, e):
        cursorRow = self.userTable.focus()
        contents = self.userTable.item(cursorRow)
        row = contents["values"]
        self.userIdvar.set(row[0])
        self.nameVar.set(row[1])
        self.emailVar.set(row[2])
        self.usnameVar.set(row[3])
        self.passwdVar.set(row[4])
        self.contVar.set(row[5])
        self.dobVar.set(row[6])
        self.staVar.set(row[7])
        self.genVar.set(row[8])
        self.txtAdd.delete("1.0", END)
        self.txtAdd.insert(END, row[9])

    def updateData(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="myProject1")
        cur = con.cursor()
        cur.execute("Update Users set name=%s, email=%s, username=%s, password=%s, contact=%s, dob=%s, "
                    "status=%s, gender=%s, address=%s where userId=%s",
                    (
                     self.nameVar.get(),
                     self.emailVar.get(),
                     self.usnameVar.get(),
                     self.passwdVar.get(),
                     self.contVar.get(),
                     self.dobVar.get(),
                     self.staVar.get(),
                     self.genVar.get(),
                     self.txtAdd.get('1.0', END),
                     self.userIdvar.get()
                     ))
        con.commit()
        self.fetchData()
        self.clear()
        con.close()
        messagebox.showinfo("Success", "Record has been Updated")
    def deleteData(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="myProject1")
        cur = con.cursor()
        cur.execute("Delete from Users where Id=%s", self.userIdvar.get())
        con.commit()
        self.fetchData()
        self.clear()
        con.close()
        messagebox.showinfo("Success", "Record has been Deleted")

    def clear(self):
        self.userIdvar.set("")
        self.nameVar.set("")
        self.emailVar.set("")
        self.usnameVar.set("")
        self.passwdVar.set("")
        self.contVar.set("")
        self.dobVar.set("")
        self.staVar.set("")
        self.genVar.set("")
        self.txtAdd.delete("1.0", END)

    def searchData(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="myProject1")
        cur = con.cursor()
        cur.execute("select * from Users where "+str(self.searchBy.get())+" LIKE '%"+str(self.searchTxt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.userTable.delete(*self.userTable.get_children())
            for row in rows:
                self.userTable.insert("", END, values=row)
            con.commit()
        con.close()

class Fourthpage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.proIdVar = StringVar()
        self.nameVar = StringVar()
        self.catVar = StringVar()
        self.rateVar = StringVar()
        self.searchBy = StringVar()
        self.searchTxt = StringVar()

        self.label = Label(self, text="PRODUCTS", font=("Arial Bold", 15), bd=4, bg="yellow", relief=RIDGE)
        self.label.pack(fill=X, side=TOP)

    # ============ Manage Frame ========================================
        manageFrame = Frame(self, border=4, relief=RIDGE, bg="#32a5b3")

        self.proId = Label(manageFrame, text='Product Id', bg="#32a5b3", fg="white",
                           font=("times new roman", 12, "bold"))
        self.proId.grid(row=0, column=0, padx=10, pady=20)
        self.entId = Entry(manageFrame, textvariable=self.proIdVar, width=16,
                           font=("times new roman", 12, "bold"), bd=5,relief=GROOVE)
        self.entId.grid(row=0, column=1, pady=20, padx=10)

        self.name = Label(manageFrame, text='Name', bg="#32a5b3", fg="white",
                          font=("times new roman", 12, "bold"))
        self.name.grid(row=1, column=0, padx=10, pady=20)
        self.entName = Entry(manageFrame, textvariable=self.nameVar, width=16,
                             font=("times new roman", 12, "bold"), bd=5, relief=GROOVE)
        self.entName.grid(row=1, column=1, pady=20, padx=10)

        self.cat = Label(manageFrame, text='Category', bg="#32a5b3", fg="white", font=("times new roman", 12, "bold"))
        self.cat.grid(row=2, column=0, padx=10, pady=20)
        cmbCat = ttk.Combobox(manageFrame, textvariable=self.catVar, width=15, font=("times new roman", 12, "bold"))
        cmbCat["values"] = ("Cosmetics", "Grocery", "Cold Drinks")
        cmbCat.grid(row=2, column=1, pady=20, padx=10, sticky=W)

        self.desc = Label(manageFrame, text='Description', bg="#32a5b3", fg="white", font=("times new roman", 12, "bold"))
        self.desc.grid(row=3, column=0, padx=10, pady=20)
        self.txtDesc = Text(manageFrame, width=15, height=4, font=("", 12))
        self.txtDesc.grid(row=3, column=1, pady=20, padx=10)

        self.rate = Label(manageFrame, text='Rate', bg="#32a5b3", fg="white", font=("times new roman", 12, "bold"))
        self.rate.grid(row=4, column=0, padx=10, pady=20)
        self.entRate = Entry(manageFrame, textvariable=self.rateVar, width=16,
                             font=("times new roman", 12, "bold"), bd=5, relief=GROOVE)
        self.entRate.grid(row=4, column=1, pady=20, padx=10)

        # =======Button Frame=
        btnFrame = Frame(manageFrame, bd=4, relief=RIDGE, bg="#32a5b3")
        btnFrame.place(x=0, y=430, width=290)

        Addbtn = Button(btnFrame, text="Add", width=7, command=self.addProduct)
        Addbtn.grid(row=0, column=0, padx=6, pady=6)
        Updatebtn = Button(btnFrame, text="Update", width=7, command=self.updateProduct)
        Updatebtn.grid(row=0, column=1, padx=6,pady=6)
        Deletebtn = Button(btnFrame, text="Delete", width=7, command=self.deleteProduct)
        Deletebtn.grid(row=0, column=2, padx=6,pady=6)
        Clearbtn = Button(btnFrame, text="Clear", width=7, command=self.clear)
        Clearbtn.grid(row=0, column=3, padx=6, pady=6)

        manageFrame.place(x=0, y=40, width=300, height=500)

    # ============ Details Frame ========================================
        detailFrame = Frame(self, border=4, relief=RIDGE, bg="#ef2ae2")

        lblSrch = Label(detailFrame, text="Search By", bg="#ef2ae2", fg="white", font=("times new roman", 12, "bold"))
        lblSrch.grid(row=0, column=0, pady=20, padx=10, sticky=W)

        cmbSrch = ttk.Combobox(detailFrame, textvariable=self.searchBy, width=12, font=("times new roman", 12, "bold"))
        cmbSrch["values"] = ("productId", "Name")
        cmbSrch.grid(row=0, column=1, pady=20, padx=10, sticky=W)

        txtSrch = Entry(detailFrame, textvariable=self.searchTxt, font=("times new roman", 12, "bold"), bd=5,relief=GROOVE)
        txtSrch.grid(row=0, column=2, pady=20, padx=10, sticky=W)

        searchBtn = Button(detailFrame, text="Search", width=8, pady=6, command=self.searchProduct)
        searchBtn.grid(row=0, column=3,padx=10, pady=6)
        showAllBtn = Button(detailFrame, text="Show All", width=8, pady=6, command=self.fetchProduct)
        showAllBtn.grid(row=0, column=4,padx=10, pady=6)
        backBtn = Button(detailFrame, text="Back", width=8, pady=6,command=lambda: controller.showFrame(Secondpage))
        backBtn.grid(row=0, column=5, padx=10, pady=6)

        detailFrame.place(x=310, y=40, width=700, height=500)

        # ========Table Frame===============================
        tableFrame = Frame(detailFrame, bd=4, relief=RIDGE, bg="#ef2ae2")
        tableFrame.place(x=10, y=60, width=660, height=430)

        X_scroba = Scrollbar(tableFrame, orient=HORIZONTAL)
        Y_scroba = Scrollbar(tableFrame, orient=VERTICAL)
        self.productTable = ttk.Treeview(tableFrame, columns=(
        "productId", "name", "category", "description", "rate"),xscrollcommand=X_scroba.set, yscrollcommand=Y_scroba.set)
        X_scroba.pack(side=BOTTOM, fill=X)
        Y_scroba.pack(side=RIGHT, fill=Y)
        X_scroba.config(command=self.productTable.xview)
        Y_scroba.config(command=self.productTable.yview)
        self.productTable.heading("productId", text="Product Id")
        self.productTable.heading("name", text="Name")
        self.productTable.heading("category", text="Category")
        self.productTable.heading("description", text="Description")
        self.productTable.heading("rate", text="Rate")
        self.productTable["show"] = "headings"
        self.productTable.column("productId", width=100)
        self.productTable.column("name", width=100)
        self.productTable.column("category", width=100)
        self.productTable.column("description", width=100)
        self.productTable.column("rate", width=100)
        self.productTable.pack(fill=BOTH, expand=True)
        self.productTable.bind("<ButtonRelease-1>", self.getCursor)
        self.fetchProduct()

    def addProduct(self):
        if self.proIdVar.get() == "" or self.nameVar.get() == "":
            messagebox.showerror("Error", "All fields are required!!!")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="myProject1")
            cur = con.cursor()
            cur.execute("insert into Product values (%s,%s,%s,%s,%s)",
                        (self.proIdVar.get(),
                         self.nameVar.get(),
                         self.catVar.get(),
                         self.txtDesc.get('1.0', END),
                         self.rateVar.get()
                             ))
            con.commit()
            self.fetchProduct()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been Inserted")
    def fetchProduct(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="myProject1")
        cur = con.cursor()
        cur.execute("select * from Product")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert("", END, values=row)
            con.commit()
        con.close()
    def getCursor(self, e):
        cursorRow = self.productTable.focus()
        contents = self.productTable.item(cursorRow)
        row = contents["values"]
        self.proIdVar.set(row[0])
        self.nameVar.set(row[1])
        self.catVar.set(row[2])
        self.txtDesc.delete("1.0", END)
        self.txtDesc.insert(END, row[3])
        self.rateVar.set(row[4])

    def updateProduct(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="myProject1")
        cur = con.cursor()
        cur.execute("Update Product set name=%s, category=%s, description=%s, rate=%s where productId=%s",
                    (
                     self.nameVar.get(),
                     self.catVar.get(),
                     self.txtDesc.get('1.0', END),
                     self.rateVar.get(),
                     self.proIdVar.get()
                     ))
        con.commit()
        self.fetchProduct()
        self.clear()
        con.close()
        messagebox.showinfo("Success", "Record has been Updated")
    def deleteProduct(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="myProject1")
        cur = con.cursor()
        cur.execute("Delete from Product where productId=%s", self.proIdVar.get())
        con.commit()
        self.fetchProduct()
        self.clear()
        con.close()
        messagebox.showinfo("Success", "Record has been Deleted")

    def clear(self):
        self.proIdVar.set("")
        self.nameVar.set("")
        self.catVar.set("")
        self.txtDesc.delete("1.0", END)
        self.rateVar.set("")

    def searchProduct(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="myProject1")
        cur = con.cursor()
        cur.execute("select * from Product where "+str(self.searchBy.get())+" LIKE '%"+str(self.searchTxt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert("", END, values=row)
            con.commit()
        con.close()

class Fifthpage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.nameVar = StringVar()
        self.contVar = StringVar()
        self.billNoVar = StringVar()
        self.bathsoapVar = StringVar()
        self.facecreamVar = StringVar()
        self.mouthwashVar = StringVar()
        self.hairsprayVar = StringVar()
        self.hairgelVar = StringVar()
        self.bodyloVar = StringVar()
        self.perfumeVar = StringVar()

        self.cerealVar = StringVar()
        self.vegeOilVar = StringVar()
        self.noodleVar = StringVar()
        self.wheatVar = StringVar()
        self.teaVar = StringVar()
        self.custardVar = StringVar()
        self.fishVar = StringVar()

        self.fivealiveVar = StringVar()
        self.fantaVar = StringVar()
        self.hollandiaVar = StringVar()
        self.cokeVar = StringVar()
        self.cwayVar = StringVar()
        self.pepsiVar = StringVar()
        self.monsterVar = StringVar()

        self.cosmePriceVar = StringVar()
        self.grocPriceVar = StringVar()
        self.drinkPriceVar = StringVar()
        self.cosmeTaxVar = StringVar()
        self.grocTaxVar = StringVar()
        self.drinkTaxVar = StringVar()

        self.label = Label(self, text="SALES", font=("Arial Bold", 15), bd=4, bg="yellow", relief=RIDGE)
        self.label.pack(fill=X, side=TOP, pady=1)

    #============= Customer Details =================================
        cusFrame = LabelFrame(self, text='Customer Details', bd=5, bg='green', font=('Arial Bold', 10))

        self.name = Label(cusFrame, text='Name', font=("Arial Bold", 10))
        self.name.grid(row=0, column=0, padx=22, pady=10, sticky=E)

        self.nameEnt = Entry(cusFrame, width=20, textvariable=self.nameVar)
        self.nameEnt.grid(row=0, column=1, padx=10)

        self.contact = Label(cusFrame, text='Contact', font=("Arial Bold", 10))
        self.contact.grid(row=0, column=2, pady=10, padx=22, sticky=E)

        self.contactEnt = Entry(cusFrame, width=20, textvariable=self.contVar)
        self.contactEnt.grid(row=0, column=4, padx=10)

        self.billNo = Label(cusFrame, text='Bill Number', font=("Arial Bold", 10))
        self.billNo.grid(row=0, column=5, pady=10, padx=23, sticky=E)

        self.billNoEnt = Entry(cusFrame, width=20, textvariable=self.billNoVar)
        self.billNoEnt.grid(row=0, column=6, padx=10)

        self.searchBtn = Button(cusFrame, text='Search', width=10, font=("Arial Bold", 10), command=self.searchBill)
        self.searchBtn.grid(row=0, column=7, pady=10, padx=22, sticky=E)

        self.backBtn = Button(cusFrame, text='Back', width=10, font=("Arial Bold", 10), command=lambda:controller.showFrame(Secondpage))
        self.backBtn.grid(row=0, column=8, pady=10, padx=22, sticky=E)

        cusFrame.pack(fill=BOTH)

    # ============ Manage Cosmetic ========================================
        costFrame = LabelFrame(self, text='Cosmetics', border=4, relief=RIDGE, bg="#aea5b7", font=("Arial Bold", 10))
        self.l1 = Label(costFrame, text='Bath Soap', font=("Arial Bold", 10), bg="#aea5b7")
        self.l1.grid(row=0, column=0, padx=10, pady=5)
        self.ent1 = Entry(costFrame, width=10, bd=4, textvariable=self.bathsoapVar)
        self.ent1.grid(row=0, column=1, pady=5, padx=6)
        self.ent1.insert(0, 0)

        self.l2 = Label(costFrame, text='Face Cream', font=("Arial Bold", 10), bg="#aea5b7")
        self.l2.grid(row=1, column=0, padx=10, pady=5)
        self.ent2 = Entry(costFrame, width=10, bd=4, textvariable=self.facecreamVar)
        self.ent2.grid(row=1, column=1, pady=5, padx=6)
        self.ent2.insert(0, 0)

        self.l3 = Label(costFrame, text='Mouth Wash', font=("Arial Bold", 10), bg="#aea5b7")
        self.l3.grid(row=2, column=0, padx=10, pady=5)
        self.ent3 = Entry(costFrame, width=10, bd=4, textvariable=self.mouthwashVar)
        self.ent3.grid(row=2, column=1, pady=5, padx=6)
        self.ent3.insert(0, 0)

        self.l4 = Label(costFrame, text='Hair Spray', font=("Arial Bold", 10), bg="#aea5b7")
        self.l4.grid(row=3, column=0, padx=10, pady=5)
        self.ent4 = Entry(costFrame, width=10, bd=4, textvariable=self.hairsprayVar)
        self.ent4.grid(row=3, column=1, pady=5, padx=6)
        self.ent4.insert(0, 0)

        self.l5 = Label(costFrame, text='Hair Gel', font=("Arial Bold", 10), bg="#aea5b7")
        self.l5.grid(row=4, column=0, padx=10, pady=5)
        self.ent5 = Entry(costFrame, width=10, bd=4, textvariable=self.hairgelVar)
        self.ent5.grid(row=4, column=1, pady=5, padx=6)
        self.ent5.insert(0, 0)

        self.l6 = Label(costFrame, text='Body Lotion', font=("Arial Bold", 10), bg="#aea5b7")
        self.l6.grid(row=5, column=0, padx=10, pady=5)
        self.ent6 = Entry(costFrame, width=10, bd=4, textvariable=self.bodyloVar)
        self.ent6.grid(row=5, column=1, pady=5, padx=6)
        self.ent6.insert(0, 0)

        self.l7 = Label(costFrame, text='Perfume', font=("Arial Bold", 10), bg="#aea5b7")
        self.l7.grid(row=6, column=0, padx=10, pady=5)
        self.ent7 = Entry(costFrame, width=10, bd=4, textvariable=self.perfumeVar)
        self.ent7.grid(row=6, column=1, pady=5, padx=6, sticky='w')
        self.ent7.insert(0, 0)

        costFrame.place(x=0, y=105, width=200, height=280)

    # ============ Manage Grocery ========================================
        grocFrame = LabelFrame(self, text='Grocery', border=4, relief=RIDGE, bg="#f2a5b7", font=("Arial Bold", 10))
        self.g1 = Label(grocFrame, text='Cereals',  font=("Arial Bold", 10), bg="#f2a5b7")
        self.g1.grid(row=0, column=0, pady=5, padx=10, sticky='w')
        self.entg1 = Entry(grocFrame, width=10, bd=4, textvariable=self.cerealVar)
        self.entg1.grid(row=0, column=1, padx=6, pady=5)
        self.entg1.insert(0, 0)

        self.g2 = Label(grocFrame, text='Vegetable Oil', font=("Arial Bold", 10), bg="#f2a5b7")
        self.g2.grid(row=1, column=0, pady=5, padx=10, sticky='w')
        self.entg2 = Entry(grocFrame, width=10, bd=4, textvariable=self.vegeOilVar)
        self.entg2.grid(row=1, column=1, padx=6, pady=5)
        self.entg2.insert(0, 0)

        self.g3 = Label(grocFrame, text='Noodles', font=("Arial Bold", 10), bg="#f2a5b7")
        self.g3.grid(row=2, column=0, pady=5, padx=10, sticky='w')
        self.entg3 = Entry(grocFrame, width=10, bd=4, textvariable=self.noodleVar)
        self.entg3.grid(row=2, column=1, padx=6, pady=5)
        self.entg3.insert(0, 0)

        self.g4 = Label(grocFrame, text='WheatMill', font=("Arial Bold", 10), bg="#f2a5b7")
        self.g4.grid(row=3, column=0, pady=5, padx=10, sticky='w')
        self.entg4 = Entry(grocFrame, width=10, bd=4, textvariable=self.wheatVar)
        self.entg4.grid(row=3, column=1, padx=6, pady=5)
        self.entg4.insert(0, 0)

        self.g5 = Label(grocFrame, text='Tea', font=("Arial Bold", 10), bg="#f2a5b7")
        self.g5.grid(row=4, column=0, pady=5, padx=10, sticky='w')
        self.entg5 = Entry(grocFrame, width=10, bd=4, textvariable=self.teaVar)
        self.entg5.grid(row=4, column=1, padx=6, pady=5)
        self.entg5.insert(0, 0)

        self.g6 = Label(grocFrame, text='Custard', font=("Arial Bold", 10), bg="#f2a5b7")
        self.g6.grid(row=5, column=0, pady=5, padx=10, sticky='w')
        self.entg6 = Entry(grocFrame, width=10, bd=4, textvariable=self.custardVar)
        self.entg6.grid(row=5, column=1, padx=6, pady=5)
        self.entg6.insert(0, 0)

        self.g7 = Label(grocFrame, text='Frozen Fish', font=("Arial Bold", 10), bg="#f2a5b7")
        self.g7.grid(row=6, column=0, pady=5, padx=10, sticky='w')
        self.entg7 = Entry(grocFrame, width=10, bd=4, textvariable=self.fishVar)
        self.entg7.grid(row=6, column=1, padx=6, pady=5)
        self.entg7.insert(0, 0)

        grocFrame.place(x=200, y=105, width=200, height=280)

    # ============ Manage Drinks ========================================
        drinkFrame = LabelFrame(self, text='Cold Drinks', border=4, relief=RIDGE, bg="light blue", font=("Arial Bold", 10))
        self.c1 = Label(drinkFrame, text='Five Alive', font=("Arial Bold", 10), bg="light blue")
        self.c1.grid(row=0, column=0, pady=5, padx=10, sticky='w')
        self.entc1 = Entry(drinkFrame, width=10, bd=4, textvariable=self.fivealiveVar)
        self.entc1.grid(row=0, column=1, padx=6, pady=5)
        self.entc1.insert(0, 0)

        self.c2 = Label(drinkFrame, text='Fanta', font=("Arial Bold", 10), bg="light blue")
        self.c2.grid(row=1, column=0, pady=5, padx=10, sticky='w')
        self.entc2 = Entry(drinkFrame, width=10, bd=4, textvariable=self.fantaVar)
        self.entc2.grid(row=1, column=1, padx=6, pady=5)
        self.entc2.insert(0, 0)

        self.c3 = Label(drinkFrame, text='Hollandia', font=("Arial Bold", 10), bg="light blue")
        self.c3.grid(row=2, column=0, pady=5, padx=10, sticky='w')
        self.entc3 = Entry(drinkFrame, width=10, bd=4, textvariable=self.hollandiaVar)
        self.entc3.grid(row=2, column=1, padx=6, pady=5)
        self.entc3.insert(0, 0)

        self.c4 = Label(drinkFrame, text='Coca Cola', font=("Arial Bold", 10), bg="light blue")
        self.c4.grid(row=3, column=0, pady=5, padx=10, sticky='w')
        self.entc4 = Entry(drinkFrame, width=10, bd=4, textvariable=self.cokeVar)
        self.entc4.grid(row=3, column=1, padx=6, pady=5)
        self.entc4.insert(0, 0)

        self.c5 = Label(drinkFrame, text='Cway Nutri', font=("Arial Bold", 10), bg="light blue")
        self.c5.grid(row=4, column=0, pady=5, padx=10, sticky='w')
        self.entc5 = Entry(drinkFrame, width=10, bd=4, textvariable=self.cwayVar)
        self.entc5.grid(row=4, column=1, padx=6, pady=5)
        self.entc5.insert(0, 0)

        self.c6 = Label(drinkFrame, text='pepsi', font=("Arial Bold", 10), bg="light blue")
        self.c6.grid(row=5, column=0, pady=5, padx=10, sticky='w')
        self.entc6 = Entry(drinkFrame, width=10, bd=4, textvariable=self.pepsiVar)
        self.entc6.grid(row=5, column=1, padx=6, pady=5)
        self.entc6.insert(0, 0)

        self.c7 = Label(drinkFrame, text='Monster', font=("Arial Bold", 10), bg="light blue")
        self.c7.grid(row=6, column=0, pady=5, padx=10, sticky='w')
        self.entc7 = Entry(drinkFrame, width=10, bd=4, textvariable=self.monsterVar)
        self.entc7.grid(row=6, column=1, padx=6, pady=5)
        self.entc7.insert(0, 0)

        drinkFrame.place(x=400, y=105, width=200, height=280)

    # ============ Display Bills ========================================
        dispFrame = Frame(self, border=4, relief=RIDGE, bg="#aea5b7")
        self.bilArea = Label(dispFrame, text='Bill Area', bd=4, font=("Arial Bold", 10), bg="blue")
        self.bilArea.pack(fill=X)
        scrollbar = Scrollbar(dispFrame, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.textarea = Text(dispFrame, height=18, yscrollcommand=scrollbar.set)
        self.textarea.pack()
        scrollbar.config(command=self.textarea.yview)

        dispFrame.place(x=600, y=105, width=420, height=280)

    # ============ Bill Menu ========================================
        billFrame = LabelFrame(self, text='Bill Menu', border=4, relief=RIDGE, bg="dark grey", font=("Arial Bold", 10))
        self.cp1 = Label(billFrame, text='Cosmetic Price', font=("Arial Bold", 10), bg="dark grey")
        self.cp1.grid(row=0, column=0, padx=10, pady=10)
        self.entcp1 = Entry(billFrame, width=12, bd=4, textvariable=self.cosmePriceVar)
        self.entcp1.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        self.cg1 = Label(billFrame, text='Grocery Price', font=("Arial Bold", 10), bg="dark grey")
        self.cg1.grid(row=1, column=0, padx=10, pady=10)
        self.entgp1 = Entry(billFrame, width=12, bd=4, textvariable=self.grocPriceVar)
        self.entgp1.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        self.cdp1 = Label(billFrame, text='Cold Drinks Price', font=("Arial Bold", 10), bg="dark grey")
        self.cdp1.grid(row=2, column=0, padx=10, pady=10)
        self.entcdp1 = Entry(billFrame, width=12, bd=4, textvariable=self.drinkPriceVar)
        self.entcdp1.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        self.cp2 = Label(billFrame, text='Cosmetic Tax', font=("Arial Bold", 10), bg="dark grey")
        self.cp2.grid(row=0, column=2, padx=10, pady=10)
        self.entcp2 = Entry(billFrame, width=12, bd=4, textvariable=self.cosmeTaxVar)
        self.entcp2.grid(row=0, column=3, padx=10, pady=10, sticky='w')

        self.gp2 = Label(billFrame, text='Grocery Tax', font=("Arial Bold", 10), bg="dark grey")
        self.gp2.grid(row=1, column=2, padx=10, pady=10)
        self.entgp2 = Entry(billFrame, width=12, bd=4, textvariable=self.grocTaxVar)
        self.entgp2.grid(row=1, column=3, padx=10, pady=10, sticky='w')

        self.cdp2 = Label(billFrame, text='Cold Drinks Tax', font=("Arial Bold", 10), bg="dark grey")
        self.cdp2.grid(row=2, column=2, padx=10, pady=10)
        self.entcdp2 = Entry(billFrame, width=12, bd=4, textvariable=self.drinkTaxVar)
        self.entcdp2.grid(row=2, column=3, padx=10, pady=10, sticky='w')

        btnFrame = Frame(self, border=4, relief=RIDGE, bg="white")
        self.totalBtn = Button(btnFrame, text='Total', width=8, bd=4, height=2, bg="dark grey",
                               font=("Arial Bold", 10), command=self.totalData)
        self.totalBtn.grid(row=0, column=0, pady=30, padx=12)

        self.billBtn = Button(btnFrame, text='Bill', width=8, bd=4, height=2, bg="dark grey",
                              font=("Arial Bold", 10), command=self.billArea)
        self.billBtn.grid(row=0, column=1, pady=30, padx=12)

        self.emailBtn = Button(btnFrame, text='Email', width=8, bd=4, height=2, bg="dark grey",
                               font=("Arial Bold", 10), command=self.sendEmail)
        self.emailBtn.grid(row=0, column=2, pady=30, padx=12)

        self.printBtn = Button(btnFrame, text='Print', width=8, bd=4, height=2, bg="dark grey",
                               font=("Arial Bold", 10), command=self.printBill)
        self.printBtn.grid(row=0, column=3, pady=30, padx=12)

        self.clearBtn = Button(btnFrame, text='Clear', width=8, bd=4, height=2, bg="dark grey",
                               font=("Arial Bold", 10), command=self.clearData)
        self.clearBtn.grid(row=0, column=4, pady=30, padx=12)

        btnFrame.place(x=470, y=415, width=540, height=110)

        billFrame.place(x=0, y=385, width=1020, height=160)


    #==== Functionality part==========================

    if not os.path.exists('bills'):
        os.mkdir('bills')

    def saveBill(self):
        global billnumber
        result = messagebox.askyesno('Confirm', 'Do you want to save the bill?')
        if result:
            billContent = self.textarea.get(1.0, END)
            file = open(f'bills/ {billnumber}.txt', 'w')
            file.write(billContent)
            file.close()
            messagebox.showinfo('Success', f'bill number {billnumber} is saved successfully')
            billnumber = random.randint(500, 1000)

    def totalData(self):
        global soapPrice, facecreamPrice, facewashPrice, hairsprayPrice, hairgelPrice, bodylotionPrice, perfumePrice
        global cerealPrice, oilPrice, noodlesPrice, wheatPrice, teaPrice, custardPrice, fishPrice
        global fiveAlivePrice, fantaPrice, hollandiaPrice, cokePrice, cwayPrice, pepsiPrice, monsterPrice
        global totalBill

        soapPrice = int(self.ent1.get()) * 450
        facecreamPrice = int(self.ent2.get()) * 800
        facewashPrice = int(self.ent3.get()) * 650
        hairsprayPrice = int(self.ent4.get()) * 600
        hairgelPrice = int(self.ent5.get()) * 500
        bodylotionPrice = int(self.ent6.get()) * 900
        perfumePrice = int(self.ent7.get()) * 1000

        totalcosmeticPrice = (soapPrice+facecreamPrice+facewashPrice+hairsprayPrice+hairgelPrice+bodylotionPrice+perfumePrice)
        self.entcp1.delete(0, END)
        self.entcp1.insert(0, f'#{totalcosmeticPrice}')
        cosmeticTax = totalcosmeticPrice * 0.075
        self.entcp2.delete(0, END)
        self.entcp2.insert(0, f'#{cosmeticTax}')

    #==== Grocery price ===========================
        cerealPrice = int(self.entg1.get()) * 1200
        oilPrice = int(self.entg2.get()) * 600
        noodlesPrice = int(self.entg3.get()) * 900
        wheatPrice = int(self.entg4.get()) * 700
        teaPrice = int(self.entg5.get()) * 300
        custardPrice = int(self.entg6.get()) * 500
        fishPrice = int(self.entg7.get()) * 400

        totalgroceryPrice = (cerealPrice+oilPrice+noodlesPrice+wheatPrice+teaPrice+custardPrice+fishPrice)
        self.entgp1.delete(0, END)
        self.entgp1.insert(0, f'#{totalgroceryPrice}')
        groceryTax = totalgroceryPrice * 0.075
        self.entgp2.delete(0, END)
        self.entgp2.insert(0, f'#{groceryTax}')

    # ==== ColdDrink price ===========================
        fiveAlivePrice = int(self.entc1.get()) * 480
        fantaPrice = int(self.entc2.get()) * 220
        hollandiaPrice = int(self.entc3.get()) * 600
        cokePrice = int(self.entc4.get()) * 220
        cwayPrice = int(self.entc5.get()) * 300
        pepsiPrice = int(self.entc6.get()) * 200
        monsterPrice = int(self.entc7.get()) * 450

        totalcoldDrinkPrice = (fiveAlivePrice+fantaPrice+hollandiaPrice+cokePrice+cwayPrice+pepsiPrice+monsterPrice)
        self.entcdp1.delete(0, END)
        self.entcdp1.insert(0, f'#{totalcoldDrinkPrice}')
        coldDrinkTax = totalcoldDrinkPrice * 0.075
        self.entcdp2.delete(0, END)
        self.entcdp2.insert(0, f'#{coldDrinkTax}')

        totalBill = totalcosmeticPrice+totalgroceryPrice+totalcoldDrinkPrice+cosmeticTax+groceryTax+coldDrinkTax

    def billArea(self):
        if self.nameEnt.get() == '' or self.contactEnt.get() == '':
            messagebox.showerror('Error', 'Customer Details Are Required')
        elif self.entcp1.get() == '' and self.entgp1.get() == '' and self.entcdp1.get() == '':
            messagebox.showerror('Error', 'No products are selected')
        elif self.entcp1.get() == '0' and self.entgp1.get() == '0' and self.entcdp1.get() == '0':
            messagebox.showerror('Error', 'No products are selected')
        else:
            self.textarea.delete(1.0, END)

            self.textarea.insert(END, '\t\t**Welcome Customers**\n')
            self.textarea.insert(END, f'\nBill Number: {billnumber}\n')
            self.textarea.insert(END, f'\nCustomer Name: {self.nameEnt.get()}\n')
            self.textarea.insert(END, f'\nContact Number: {self.contactEnt.get()}\n')
            self.textarea.insert(END, '\n================================================')
            self.textarea.insert(END, f'\nProducts\t\t Quantity \t\t\tPrice')
            self.textarea.insert(END, '\n================================================')
            if self.ent1.get() != '0':
                self.textarea.insert(END, f'\nBath Soap\t\t{self.ent1.get()}\t\t\t#{soapPrice}')
            if self.ent2.get() != '0':
                self.textarea.insert(END, f'\nFace Cream\t\t{self.ent2.get()}\t\t\t#{facecreamPrice}')
            if self.ent3.get() != '0':
                self.textarea.insert(END, f'\nFace Wash\t\t{self.ent3.get()}\t\t\t#{facewashPrice}')
            if self.ent4.get() != '0':
                self.textarea.insert(END, f'\nHair Spray\t\t{self.ent4.get()}\t\t\t#{hairsprayPrice}')
            if self.ent5.get() != '0':
                self.textarea.insert(END, f'\nHair Gel\t\t{self.ent5.get()}\t\t\t#{hairgelPrice}')
            if self.ent6.get() != '0':
                self.textarea.insert(END, f'\nBody Lotion\t\t{self.ent6.get()}\t\t\t#{bodylotionPrice}')
            if self.ent7.get() != '0':
                self.textarea.insert(END, f'\nPerfume \t\t{self.ent7.get()}\t\t\t#{perfumePrice}')

            #==== Groceries ========
            if self.entg1.get() != '0':
                self.textarea.insert(END, f'\nCereals\t\t{self.entg1.get()}\t\t\t#{cerealPrice}')
            if self.entg2.get() != '0':
                self.textarea.insert(END, f'\nVegetable Oil\t\t{self.entg2.get()}\t\t\t#{oilPrice}')
            if self.entg3.get() != '0':
                self.textarea.insert(END, f'\nNoodles\t\t{self.entg3.get()}\t\t\t#{noodlesPrice}')
            if self.entg4.get() != '0':
                self.textarea.insert(END, f'\nWheatmill\t\t{self.entg4.get()}\t\t\t#{wheatPrice}')
            if self.entg5.get() != '0':
                self.textarea.insert(END, f'\nTea\t\t{self.entg5.get()}\t\t\t#{teaPrice}')
            if self.entg6.get() != '0':
                self.textarea.insert(END, f'\nCustard\t\t{self.entg6.get()}\t\t\t#{custardPrice}')
            if self.entg7.get() != '0':
                self.textarea.insert(END, f'\nFrozen Fish\t\t{self.entg7.get()}\t\t\t#{fishPrice}')

            # ==== Cold Drinks ========
            if self.entc1.get() != '0':
                self.textarea.insert(END, f'\nFive Alive\t\t{self.entc1.get()}\t\t\t#{fiveAlivePrice}')
            if self.entc2.get() != '0':
                self.textarea.insert(END, f'\nFanta\t\t{self.entc2.get()}\t\t\t#{fantaPrice}')
            if self.entc3.get() != '0':
                self.textarea.insert(END, f'\nHollandia\t\t{self.entc3.get()}\t\t\t#{hollandiaPrice}')
            if self.entc4.get() != '0':
                self.textarea.insert(END, f'\nCoca Cola\t\t{self.entc4.get()}\t\t\t#{cokePrice}')
            if self.entc5.get() != '0':
                self.textarea.insert(END, f'\nCway Nutri\t\t{self.entc5.get()}\t\t\t#{cwayPrice}')
            if self.entc6.get() != '0':
                self.textarea.insert(END, f'\nPepsi\t\t{self.entc6.get()}\t\t\t#{pepsiPrice}')
            if self.entc7.get() != '0':
                self.textarea.insert(END, f'\nMonster\t\t{self.entc7.get()}\t\t\t#{monsterPrice}')
            self.textarea.insert(END, '\n================================================')

            if self.entcp2.get() != '0,0':
                self.textarea.insert(END, f'\nCosmetic Tax\t\t\t\t{self.entcp2.get()}')
            if self.entgp2.get() != '0,0':
                self.textarea.insert(END, f'\nGrocery Tax\t\t\t\t{self.entgp2.get()}')
            if self.entcdp2.get() != '0,0':
                self.textarea.insert(END, f'\nCold Drink Tax\t\t\t\t{self.entcdp2.get()}')
            self.textarea.insert(END, f'\n\nTotal Bill \t\t\t\t #{totalBill}')
            self.textarea.insert(END, '\n================================================')
            self.saveBill()


    def clearData(self):
        self.nameVar.set("")
        self.contVar.set("")
        self.billNoVar.set("")
        self.bathsoapVar.set("0")
        self.facecreamVar.set("0")
        self.mouthwashVar.set("0")
        self.hairsprayVar.set("0")
        self.hairgelVar.set("0")
        self.bodyloVar.set("0")
        self.perfumeVar.set("0")

        self.cerealVar.set("0")
        self.vegeOilVar.set("0")
        self.noodleVar.set("0")
        self.wheatVar.set("0")
        self.teaVar.set("0")
        self.custardVar.set("0")
        self.fishVar.set("0")

        self.fivealiveVar.set("0")
        self.fantaVar.set("0")
        self.hollandiaVar.set("0")
        self.cokeVar.set("0")
        self.cwayVar.set("0")
        self.pepsiVar.set("0")
        self.monsterVar.set("0")

        self.cosmePriceVar.set("0")
        self.grocPriceVar.set("0")
        self.drinkPriceVar.set("0")
        self.cosmeTaxVar.set("0")
        self.grocTaxVar.set("0")
        self.drinkTaxVar.set("0")

        self.textarea.delete(1.0, END)

    def searchBill(self):
        for i in os.listdir("bills/"):
            if i.split(",")[0] == self.billNoVar.get():
                f = open(f"bills/{i}", "r")
                self.textarea.delete(1.0, END)
                for data in f:
                    self.textarea.insert(END, data)
                f.close()
                break
        else:
            messagebox.showerror('Error', 'Invalid Bill Number')

    def printBill(self):
        if self.textarea.get(1.0, END) == '\n':
            messagebox.showerror('Error', 'Bill is Empty')
        else:
            file = tempfile.mktemp('.txt')
            open(file, 'w').write(self.textarea.get(1.0, END))
            os.startfile(file, 'print')

    def sendGmail(self):
        try:
            ob = smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(self.sendEnt.get(), self.passEnt.get())
            message = self.emailTextarea.get(1.0, END)
            ob.sendmail(self.sendEnt.get(), self.recieverEnt.get(), message)
            ob.quit()
            messagebox.showinfo('Success', 'Bill is successful sent', window=app1)
            app1.destroy()
        except:
            messagebox.showerror('Error', 'Something went wrong, please try again!', window=app1)

    def sendEmail(self):
        global app1

        if self.textarea.get(1.0, END) == '\n':
            messagebox.showerror('Error', 'Bill is Empty')
        else:
            app1 = Toplevel()
            app1.grab_set()
            app1.title('send gmail')
            app1.config(bg='sky blue')
            app1.resizable(0,0)

            senderFrame = LabelFrame(app1, text='SENDER', bg='sky blue',bd=4,fg='white', font=('Arial bold', 15))
            senderFrame.grid(row=0, column=0, padx=40, pady=20)

            self.senderlbl = Label(senderFrame, text="Sender's Email",bg='sky blue',bd=4,fg='white', font=('Arial bold', 15))
            self.senderlbl.grid(row=0, column=0, padx=10, pady=8)
            self.sendEnt = Entry(senderFrame, font=('Arial bold', 14), bd=2, width=20, relief=RIDGE)
            self.sendEnt.grid(row=0, column=1, padx=10, pady=8)

            self.passlbl = Label(senderFrame, text="Password", bg='sky blue', bd=4, fg='white', font=('Arial bold', 15))
            self.passlbl.grid(row=1, column=0, padx=10, pady=8)
            self.passEnt = Entry(senderFrame, font=('Arial bold', 14), show='*', bd=2, width=20, relief=RIDGE)
            self.passEnt.grid(row=1, column=1, padx=10, pady=8)

            recipientFrame = LabelFrame(app1, text='RECIPIENT', bg='sky blue', bd=4, fg='white', font=('Arial bold', 15))
            recipientFrame.grid(row=1, column=0, padx=40, pady=20)

            self.recieverlbl = Label(recipientFrame, text="Email Address", bg='sky blue', bd=4, fg='white', font=('Arial bold', 15))
            self.recieverlbl.grid(row=0, column=0, padx=10, pady=8)
            self.recieverEnt = Entry(recipientFrame, font=('Arial bold', 14), bd=2, width=20, relief=RIDGE)
            self.recieverEnt.grid(row=0, column=1, padx=10, pady=8)

            self.msglbl = Label(recipientFrame, text="Message", bg='sky blue', bd=4, fg='white', font=('Arial bold', 15))
            self.msglbl.grid(row=1, column=0, padx=10, pady=8)

            self.emailTextarea = Text(recipientFrame, bd=2, relief=SUNKEN, width=42, height=10, font=('Arial bold', 14))
            self.emailTextarea.grid(row=2, column=0, columnspan=2)
            self.emailTextarea.delete(1.0, END)
            self.emailTextarea.insert(END, self.textarea.get(1.0, END).replace('=', '').replace('\t\t\t', '\t\t'))



        sendBtn = Button(app1, text='SEND', font=('Arial bold', 16), width=14, command=self.sendGmail)
        sendBtn.grid(row=2, column=0, pady=15)


        app1.mainloop()

class Application(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # Creating a window
        window = Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=550)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (Firstpage, Secondpage, Thirdpage, Fourthpage, Fifthpage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.showFrame(Firstpage)

    def showFrame(self, page):
        frame = self.frames[page]
        frame.tkraise()

app = Application()
app.maxsize(1350, 750)
app.mainloop()