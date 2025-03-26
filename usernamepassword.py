import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase1"
)
cursor = mydb.cursor()
username=input("ENTER USERNAME")
password=input("ENTER PASSWORD")
cursor.execute( "SELECT * FROM student_registration WHERE username = %s AND password = %s",(username, password))

if cursor.fetchone():
  print("Logged in")
else:
  print("Invalid USERNAME OR PASSWORD")
cursor.close()
mydb.close()

