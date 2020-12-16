import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="VMBB",
    password="vlocmalhbostb",
    database="lkstock"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT Descripcion FROM lkstock.productos LIMIT 10")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
