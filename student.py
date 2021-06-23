import tkinter
import pymysql as mysql
from tkinter import messagebox
app = tkinter.Tk(className='Student Details')
app.geometry('800x400')

mysql_conn = mysql.connect(
    host="localhost", user="root", password="root", database="project", port=3325)
mysql_cursor = mysql_conn.cursor()

Name = tkinter.StringVar()
Place = tkinter.StringVar()
Class=tkinter.StringVar()
Phone_Number=tkinter.StringVar()
E_Mail=tkinter.StringVar()
delete=tkinter.StringVar()

label1 = tkinter.Label(app, text="Name")
label1.grid(row='1')

textEntry1 = tkinter.Entry(app, textvariable=Name, width=15)
textEntry1.grid(row='1', column='1')

label2 = tkinter.Label(app, text="Place")
label2.grid(row='2')

textEntry2 = tkinter.Entry(app, textvariable=Place, width=15)
textEntry2.grid(row='2', column='1')

label3 = tkinter.Label(app, text="Class")
label3.grid(row='3')

textEntry3 = tkinter.Entry(app, textvariable=Class, width=15)
textEntry3.grid(row='3', column='1')

label4 = tkinter.Label(app, text="Phone Number")
label4.grid(row='4')

textEntry4 = tkinter.Entry(app, textvariable=Phone_Number, width=15)
textEntry4.grid(row='4', column='1')

label5 = tkinter.Label(app, text="E-Mail")
label5.grid(row='5')

textEntry5 = tkinter.Entry(app, textvariable=E_Mail, width=15)
textEntry5.grid(row='5', column='1')

def insertion():
    m = Name.get()
    n = Place.get()
    o= Class.get()
    p=Phone_Number.get()
    q=E_Mail.get()
    insert_query = "insert into student_table (Student_Name, Place, Class, Phone_Number, E_Mail) values ('" + \
        m+"','"+n+"','"+o+"','"+p+"','"+q+"')"

    mysql_cursor.execute(insert_query)

    mysql_conn.commit()

    Name.set(" ")
    Place.set(" ")
    Class.set(" ")
    Phone_Number.set(" ")
    E_Mail.set(" ")

    messagebox.showinfo("Data Info", "Data inserted sucessfully")


def retrival():
    fetch_query = 'select * from student_table'
    mysql_cursor.execute(fetch_query)
    row_index = 14

    headers = [header[0] for header in mysql_cursor.description]
    for index, header in enumerate(headers):
        en = tkinter.Entry(app, width=20, fg='blue', bg='gray')
        en.grid(row=row_index, column=index)
        en.insert(tkinter.END, header.upper())
    row_index += 1

    for data in mysql_cursor.fetchall():
        for index, value in enumerate(data):
            en = tkinter.Entry(app, width=20, fg='blue', bg='gray')
            en.grid(row=row_index, column=index)
            en.insert(tkinter.END, value)
        row_index += 1
def Delete():
    label6 = tkinter.Label(app, text="Enter the student name to delete")
    label6.grid(row='7')

    textEntry6 = tkinter.Entry(app, textvariable=delete, width=15)
    textEntry6.grid(row='7', column='1')

    button5 = tkinter.Button(app, width=15, text="Confirm Delete", command=CDelete,fg='Black',bg='White')
    button5.grid(row='8', column='2')
def CDelete():

    c=delete.get()
    r="DELETE FROM student_table WHERE student_name='"+c+"'"
    mysql_cursor.execute(r) 
    mysql_conn.commit()
    delete.set(" ")      
    messagebox.showinfo("Data Info", "Data sucessfully Deleted")
    retrival()

button1 = tkinter.Button(app, width=15, text="Save", command=insertion)
button1.grid(row='8', column='1')

button2 = tkinter.Button(app, width=15, text="View", command=retrival)
button2.grid(row='9', column='1')

button3 =tkinter.Button(app,text=" Delete",width=15,command=Delete)
button3.grid(row='12',column='1')

button4 = tkinter.Button(app, text="Exit", width=15, command=app.destroy)
button4.grid(row='13',column='1')

app.mainloop()
