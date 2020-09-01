from tkinter import *
import tkinter as tk
import sqlite3 as sql
from datetime import *
from tkinter import messagebox

con = sql.connect("Expense Manager.db")

root = tk.Tk()
root.title("Expense Manager")
root.geometry("1080x680")
root.resizable(0, 0)
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)
f6 = Frame(root)

for frame in (f1, f2, f3, f4,f5,f6):
    frame.grid(row=0, column=0, sticky='news')


def raise_frame(frame):
    frame.tkraise()

def back():
    raise_frame(f1)


def create():
    query = """
            CREATE  TABLE IF NOT EXISTS Savings(
            Type varchar(100) NOT NULL,
            OrganizationName varchar(100) NOT NULL,
            SavingsId varchar(100) NOT NULL PRIMARY KEY,
            Rate number(2,2) NOT NULL,
            Date date NOT NULL,
            Amount number(7,2) NOT NULL)
          """
    con.execute(query)
    query2 = """
                CREATE  TABLE IF NOT EXISTS Total(
                Totalbal number(9,2) DEFAULT 0 PRIMARY KEY,
                Sumrate number(9,2) DEFAULT 0 )
            """
    con.execute(query2)

    query3="""
              CREATE TABLE IF NOT EXISTS Goals(
              SlNo int DEFAULT 0 PRIMARY KEY, 
              SubjectsofGoal varchar(150) NOT NULL,
              GoalAmount number(9,2) NOT NULL,
              GoalDate date NOT NULL,
              GoalDescription varchar(300) NOT NULL)
            """
    con.execute(query3)
    query4="""
             CREATE TABLE IF NOT EXISTS RateList(
             Organization varchar(100) NOT NULL PRIMARY KEY,
             RATE number(5,3) NOT NULL)
           """
    con.execute(query4)

create()


# 0) ADD RATE FOR GOALS
def adminp():
    raise_frame(f6)

def addrate():
    orn=ba2.get()
    orr=float(r2.get())
    query="INSERT INTO RateList(Organization,RATE) VALUES (?,?)"
    con.execute(query,[orn,orr])
    messagebox.showinfo("Expense Manager", "Add Successfully")
    raise_frame(f1)
    con.commit()
    """except:
        messagebox.showinfo("Expense Manager", "Check Entered Details and Try again")
    ba2.delete(0,END)
    r2.delete(0,END)
"""
def updaterate():
    try:
        orn=ba2.get()
        orr=r2.get()
        query="UPDATE RateList SET RATE = ? WHERE Organization = ?"
        con.execute(query,[orr,orn])
        messagebox.showinfo("Expense Manager", "Update Successfully")
        raise_frame(f1)
        con.commit()
    except:
        messagebox.showinfo("Expense Manager", "Check Entered Details and Try again")
    ba2.delete(0, END)
    r2.delete(0, END)



#adminpage setup
Label(f6,text="Fill All Details Correctly",font=('Times',15,'bold','italic','underline'),background='blue').pack()
Label(f6,text="                                                                                                ").pack()
Label(f6,text="                                                                                                ").pack()
ba=Label(f6,text="Enter Organizer Name ")
ba2=Entry(f6)
r=Label(f6,text="Enter rate of the organization ")
r2=Entry(f6)
ba.pack()
Label(f6,text="                                                                                                ").pack()
ba2.pack()
Label(f6,text="                                                                                                ").pack()
r.pack()
Label(f6,text="                                                                                                ").pack()
r2.pack()
Label(f6,text="                                                                                                ").pack()
Button(f6, text="ADD",command=addrate).pack()
Label(f6,text="                                                                                                ").pack()
Button(f6, text="UPDATE",command=updaterate).pack()
Label(f6,text="                                                                                                ").pack()
Button(f6,text="BACK",command=back).pack()



# 1) SAVINGS

def add_saving():
    raise_frame(f2)


#add savings coding part

def Savings():
    try:
        typ = tsa2.get()
        org = ora2.get()
        sid = oid2.get()
        rate = float(ro2.get())
        amt = float(am2.get())
        today = str(date.today())
        query = "INSERT INTO Savings(Type,OrganizationName,SavingsId,Rate,Date,Amount) VALUES(?,?,?,?,?,?)"
        con.execute(query, [typ, org, sid, rate, today, amt])
        query="SELECT Totalbal FROM Total"
        data=(con.execute(query)).fetchone()
        if data==None:
            total =0
            total+=amt
            query = "INSERT INTO Total(Totalbal) VALUES(?)"
            con.execute(query, [total])
        else:
            total = data[0]+amt
            query2 = "UPDATE  Total SET Totalbal=?"
            con.execute(query2, [total])
        con.commit()
        messagebox.showinfo("Expense Manager", "Add Successfully")
        raise_frame(f1)
        tsa2.delete(0, END)
        ora2.delete(0, END)
        oid2.delete(0, END)
        ro2.delete(0, END)
        am2.delete(0, END)
        if data == None:
            total = amt
            Label(f1, text="Total Balence  :  " + str(total), font=('Times', 15, 'bold', 'italic', 'underline'),
                  background='yellow', width=25, height=1).grid(row=0, column=4, padx=(0, 0), pady=(0, 0))
        else:
            total = data[0]+amt
            Label(f1, text="Total Balence  :  " + str(total), font=('Times', 15, 'bold', 'italic', 'underline'),
                  background='yellow', width=25, height=1).grid(row=0, column=4, padx=(0, 0), pady=(0, 0))
    except:
        messagebox.showinfo("Expense Manager", "Check Entered Details and Try again")
        raise_frame(f1)
        tsa2.delete(0, END)
        ora2.delete(0, END)
        oid2.delete(0, END)
        ro2.delete(0, END)
        am2.delete(0, END)

#savings page structure

Label(f2,text="Fill Your Savings Details Correctly",font=('Times',15,'bold','italic','underline'),background='blue').pack()
Label(f2,text="                                 ").pack()
Label(f2,text="                                 ").pack()
tsa = Label(f2, text="Enter the Type of the Savings")
tsa2 = Entry(f2)
ora = Label(f2, text="Enter the Name of the Organization")
ora2 = Entry(f2)
oid = Label(f2, text="Enter the Id of the Savings")
oid2 = Entry(f2)
ro = Label(f2, text="Enter the Rate of the Savings")
ro2 = Entry(f2)
am = Label(f2, text="Enter the Amount of the Savings")
am2 = Entry(f2)
add = Button(f2, text="ADD", command=Savings)
tsa.pack(fill="none", expand=True)
tsa2.pack()
Label(f2,text="                                 ").pack()
ora.pack()
Label(f2,text="                                 ").pack()
ora2.pack()
Label(f2,text="                                 ").pack()
oid.pack()
Label(f2,text="                                 ").pack()
oid2.pack()
Label(f2,text="                                 ").pack()
ro.pack()
Label(f2,text="                                 ").pack()
ro2.pack()
Label(f2,text="                                 ").pack()
am.pack()
Label(f2,text="                                 ").pack()
am2.pack()
Label(f2,text="                                 ").pack()
add.pack()
Label(f2,text="                                 ").pack()
Button(f2,text="BACK",command=back).pack()








# 2) VIEW SAVINGS

def viewsav():
    try:
        raise_frame(f3)
        Label(f3, text="  -: Your Savings Details :- ", font=('Times', 15, 'bold', 'italic', 'underline'),
              background='blue').grid(row=0,column=3)
        Button(f3, text="BACK", command=back).grid(row=1,column=3)

        query="SELECT * FROM Savings"
        data=(con.execute(query))
        xz=["Type-Of-Savings ","  Organization-Name ","Savings-id","Savings-Rate","   Date  ","   Amount  ","    Comulatve-Rate"]
        for i in range(len(xz)):
            Label(f3, text=xz[i],font=('Times', 10, 'bold', 'italic', 'underline')).grid(row=2, column=i)
        p = 3
        rx=[]
        for row in data.fetchall():
            q=0
            for i in range(len(row)):
                txt=str(row[i])
                txt=txt+"    "
                Label(f3, text=txt).grid(row=p,column=q)
                q+=1
            ra=row[3]
            po=row[5]
            da=row[4]
            val=da.split("-")
            da = date(int(val[0]), int(val[1]), int(val[2]))
            td=date.today()
            x=(td-da).days
            rt=(po*((1+ra)**((x+1)/365)))-po
            rt="{:.2f}".format(rt)
            rx.append(float(rt))
            Label(f3, text=str(rt)).grid(row=p, column=q)
            m=p
            p+=1
        query = "SELECT TotalBal FROM Total"
        data = (con.execute(query)).fetchone()
        query2 = "SELECT Sumrate FROM Total"
        data2 = (con.execute(query2)).fetchone()
        sr=sum(rx)
        if sr!=data2[0]:
            tt=sr+data[0]
            tt= "{:.2f}".format(tt)
            query = "UPDATE  Total SET Totalbal=? "
            con.execute(query, [tt])
            query = "UPDATE  Total SET Sumrate = ? "
            con.execute(query, [sr])
            con.commit()
        query = "SELECT TotalBal FROM Total"
        data = (con.execute(query)).fetchone()
        to=data[0]
        tr="Total Balence : "+str(to)
        Label(f3, text="                                                    ").grid(row=p + 1, column=6)
        Label(f3, text=tr).grid(row=p+2, column=6)
        query = "SELECT Totalbal FROM Total"
        data = (con.execute(query)).fetchone()
        if data == None:
            total = 0
            Label(f1, text="Total Balence  :  " + str(total), font=('Times', 15, 'bold', 'italic', 'underline'),
                  background='yellow', width=25, height=1).grid(row=0, column=4, padx=(0, 0), pady=(0, 0))
        else:
            total = data[0]
            Label(f1, text="Total Balence  :  " + str(total), font=('Times', 15, 'bold', 'italic', 'underline'),
                  background='yellow', width=25, height=1).grid(row=0, column=4, padx=(0, 0), pady=(0, 0))
    except:
        messagebox.showinfo("Expense Manager", "No Details to Show....")
        raise_frame(f1)






# 3) SET A GOAL

def goal():
    raise_frame(f4)


def goal2():
    gf=ts2.get()
    amt=float(or2.get())
    gd=oi2.get()
    gdes=r2.get()
    query = "SELECT SlNo FROM Goals"
    data = (con.execute(query)).fetchone()
    if data==None:
        sl=1
    else:
        sl=int(data[0])+1
    query = "INSERT INTO Goals(SlNo,SubjectsofGoal,GoalAmount,GoalDate,GoalDescription) VALUES(?,?,?,?,?)"
    con.execute(query, [sl,gf,amt,gd,gdes])
    con.commit()



#page structure
po=Label(f4,text="Fill Your Goals Details Correctly",font=('Times',15,'bold','italic','underline'),background='yellow').pack()
Label(f4,text="                                                                                 ").pack()
Label(f4,text="                                                                                 ").pack()
ts = Label(f4, text="Goals for")
ts2 = Entry(f4)
or1 = Label(f4, text="Enter total amount for goal ")
or2 = Entry(f4)
oi = Label(f4, text="Enter the end date for goal(dd-mm-yyyy) ")
oi2 = Entry(f4)
r = Label(f4, text="Description for goal ")
r2 = Entry(f4,width=50)
add = Button(f4, text="ADD",command=goal2)
ts.pack()
Label(f4,text="                                                                                 ").pack()
ts2.pack()
Label(f4,text="                                                                                 ").pack()
or1.pack()
Label(f4,text="                                                                                 ").pack()
or2.pack()
Label(f4,text="                                                                                 ").pack()
oi.pack()
Label(f4,text="                                                                                 ").pack()
oi2.pack()
Label(f4,text="                                                                                 ").pack()
r.pack()
Label(f4,text="                                                                                 ").pack()
r2.pack()
Label(f4,text="                                                                                 ").pack()
add.pack()
Label(f4,text="                                                                                 ").pack()
Button(f4,text="BACK",command=back).pack()






#starting page
addsav = Button(f1, text="Add Savings", width=50,height=5,command=add_saving)
addsav.grid(row=0, column=1,padx=(10,20),pady=(30,10))
viewsav = Button(f1, text="view Savings", width=50,height=5,command=viewsav)
viewsav.grid(row=0, column=2,padx=(10,20),pady=(30,10))
makegoal = Button(f1, text="Make a Goal", width=50,height=5,command=goal)
makegoal.grid(row=1, column=1,padx=(10,20),pady=(30,10))
viewgoal = Button(f1, text="View Your Goals", width=50,height=5)
viewgoal.grid(row=1, column=2,padx=(10,20),pady=(30,10))
admin=Button(f1, text="ADMIN", width=10,height=5,command=adminp)
admin.grid(row=2, column=2,padx=(10,20),pady=(30,10))
raise_frame(f1)

query="SELECT Totalbal FROM Total"
data=(con.execute(query)).fetchone()
print(data)
if data==None:
    total =0
    Label(f1,text="Total Balence  :  "+str(total),font=('Times',15,'bold','italic','underline'),background='yellow',width=25,height=1).grid(row=0,column=4,padx=(0,0),pady=(0,0))
else:
    total = data[0]
    Label(f1, text="Total Balence  :  " + str(total),font=('Times',15,'bold','italic','underline'),background='yellow',width=25,height=1).grid(row=0, column=4,padx=(0,0),pady=(0,0))


root.mainloop()