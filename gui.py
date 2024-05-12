#from tkinter import *
#root = Tk()

#mybutton=Button(root,text="click Me!" ,state=DISABLED,background="blue")
#mybutton.pack()
#root.mainloop()

# import mysql.connector

# db = mysql.connector.connect(host='localhost',user='root',password='mani')
# cur=db.cursor()
# cur.execute("SHOW DATABASES")
# databases=cur.fetchall()
# print(databases)
# for database in databases:
#     print(database)
# print("connection established")

import mysql.connector

# Replace with your actual database credentials
host = 'localhost'
user = 'root'
password = 'mani'
database = 'drdl'

try:
    # Establish a connection
    db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
       auth_plugin='caching_sha2_password'
    )

    # Create a cursor object and execute queries
    # ...

    # Don't forget to close the connection
    db.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")

