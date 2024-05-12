
# from tkinter import *
# import mysql.connector

# top = Tk()
# top.title("Geometry Manager Place Example")
# top.geometry("1400x700")

# # Text box creation
# L1 = Label(top, text="Search here what you want")
# L1.place(x=430, y=30)
# E1 = Entry(top, bd=3)
# E1.place(x=600, y=30, width=500, height=60)

# L2 = Label(top, text="Expected Answer is:")
# L2.place(x=430, y=100)
# E2 = Entry(top, bd=3)
# E2.place(x=600, y=100, width=500, height=80)

# # Database connection
# db = mysql.connector.connect(host='localhost', user='root', password='mani', auth_plugin='caching_sha2_password',database='drdl')
# cur = db.cursor()

# def Ok():
#     global answer
#     question = E1.get()
#     answer = E2.get()

#     try:
#         cur.execute("SELECT * FROM DRDL WHERE QUESTION='" + question + "'")
#         result = cur.fetchall()
#         for x in result:
#             print(x)  # You can modify this part to display the result in your GUI
#         db.close()
#         E2.delete(0, END)
#         for row in result:
#             E2.insert(END, row)  # Display each row of data in the entry widget


#     except Exception as e:
#         print("Error:", e)  # Display a user-friendly error message in your GUI

# # Search button
# b = Button(top, text="Search", padx=50, command=Ok)
# b.place(height=50, x=1150, y=30)

# top.mainloop()





from tkinter import *
import mysql.connector

def Ok():
    question = E1.get()

    try:
        cur.execute("SELECT * FROM DRDL WHERE QUESTION='" + question + "'")
        result = cur.fetchall()

        # Clear the existing content in E2
        E2.delete(0, END)

        # Display each row of data in the entry widget
        for row in result:
            E2.insert(END, row)  # Insert the fetched data into E2

    except Exception as e:
        print("Error:", e)  # Display a user-friendly error message in your GUI

# Create the main window
top = Tk()
top.title("Geometry Manager Place Example")
top.geometry("1400x700")

# Text box creation
L1 = Label(top, text="Search here what you want")
L1.place(x=430, y=30)
E1 = Entry(top, bd=3)
E1.place(x=600, y=30, width=500, height=60)

L2 = Label(top, text="Expected Answer is:")
L2.place(x=430, y=100)
E2 = Entry(top, bd=3)
E2.place(x=600, y=100, width=500, height=80)

# Database connection
db = mysql.connector.connect(host='localhost', user='root', password='mani', auth_plugin='caching_sha2_password', database='drdl')
cur = db.cursor()

# Search button
b = Button(top, text="Search", padx=50, command=Ok)
b.place(height=50, x=1150, y=30)

top.mainloop()
