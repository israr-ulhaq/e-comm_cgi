#!C:\Users\israr\AppData\Local\Programs\Python\Python38-32\python.exe


import cgitb
cgitb.enable()
print("content-type: text/html\n\n" )
print("<br><B>hello python</B>")

print ('<html>')
print ('<head>')
print ('<title>Hello World - First CGI Program</title>')
print ('</head>')
print ('<body>')
print ('<h2>Hello World! This is my first CGI program</h2>')
print ('</body>')
print ('</html>')

print('<button>Add product</button>')
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="shopDatabase",
)

print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)