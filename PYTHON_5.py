#This is mini project in python
import mysql.connector
from tkinter import *
from tkinter import messagebox

#below are the data base details
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db2"
)

cursor = db.cursor()

def insert():
    name = name_entry.get()
    rollno = rollno_entry.get()
    mobile = mobile_entry.get()
    city = city_entry.get()
    
    if name and rollno and mobile and city:
        query = "INSERT INTO student (rollno, name, mobile, city) VALUES (%s, %s, %s, %s)"
        values = (rollno, name, mobile, city)
        cursor.execute(query, values)
        db.rollback()
        db.commit()
        
        messagebox.showinfo("Success", "Record inserted successfully")
    else:
        messagebox.showerror("Error", "Please fill all fields")

def update():
    name = name_entry.get()
    rollno = rollno_entry.get()
    mobile = mobile_entry.get()
    city = city_entry.get()
    
    if rollno:
        query = "UPDATE student SET name=%s, mobile=%s, city=%s WHERE rollno=%s"
        values = (name, mobile, city, rollno)
        cursor.execute(query, values)
        db.rollback()
        db.commit()
        
        messagebox.showinfo("Success", "Record updated successfully")
    else:
        messagebox.showerror("Error", "Please enter rollno")

def delete():
    rollno = rollno_entry.get()
    
    if rollno:
        query = "DELETE FROM student WHERE rollno=%s"
        values = (rollno,)
        cursor.execute(query, values)
        db.rollback()
        
        db.commit()
        
        messagebox.showinfo("Success", "Record deleted successfully")
    else:
        messagebox.showerror("Error", "Please enter rollno")

def select():
    rollno = rollno_entry.get()
    
    if rollno:
        query = "SELECT * FROM student WHERE rollno=%s"
        values = (rollno,)
        cursor.execute(query, values)

        result = cursor.fetchone()
        
        if result:
            name_entry.delete(0, END)
            name_entry.insert(0, result[1])
            mobile_entry.delete(0, END)
            mobile_entry.insert(0, result[2])
            city_entry.delete(0, END)
            city_entry.insert(0, result[3])
            messagebox.showinfo('Information',' RECORD SELECTED')
        else:
            messagebox.showerror("Error", "Record not found")
    else:
        messagebox.showerror("Error", "Please enter rollno")
          
        db.rollback()        
window = Tk()
window.geometry("600x500")

window.title("STUDENT REGISTRATION INFORMATION")
font=("GoudyStout",16,'bold')



blank=Label(window,text="Prepared by:DAGIYA NITESH",font=("GoudyStout",8,'bold')).pack(side=BOTTOM)
rollno_label = Label(window, text="ROLL NO:",font=font).place(x=50,y=50)


name_label = Label(window, text="STUDENT NAME:",font=font).place(x=50,y=100)

mobile_label = Label(window, text="MOBILE NUMBER:",font=font).place(x=50,y=150)

city_label = Label(window, text="CITY:",font=font).place(x=50,y=200)

rollno_entry = Entry(window)
rollno_entry.place(x=250,y=50)
rollno_entry.config(width=22,bd=3,font=font)

name_entry = Entry(window)
name_entry.place(x=250,y=100)
name_entry.config(width=22,bd=3,font=font)

mobile_entry = Entry(window)
mobile_entry.place(x=250,y=150)
mobile_entry.config(width=22,bd=3,font=font)

city_entry = Entry(window)
city_entry.place(x=250,y=200)
city_entry.config(width=22,bd=3,font=font)

font=("Verdana",12,'bold')
insert_button = Button(window, text="INSERT",command=insert,font=font,bd=4).place(x=80,y=270)

update_button = Button(window, text="UPDATE", command=update,font=font,bd=4).place(x=200,y=270)


delete_button = Button(window, text="DELETE", command=delete,font=font,bd=4).place(x=320,y=270)


select_button = Button(window, text="SELECT", command=select,font=font,bd=4).place(x=430,y=270)


window.mainloop()

#added some comments this is optional