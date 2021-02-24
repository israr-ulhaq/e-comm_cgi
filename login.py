#!C:\Users\israr\AppData\Local\Programs\Python\Python38-32\python.exe


import cgitb
cgitb.enable()
import cgi

admin_password="israr"
print("content-type: text/html\n\n" )
form = cgi.FieldStorage()
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="shopDatabase",
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
name = form.getvalue("name")
password= form.getvalue("password")

if password == admin_password:
    print("<h1>Welcome to the main page</h1>")
    print("""<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>SHOP</title>
  </head>
  <body>
    <h1>Your Products</h1>""")
    for i in products:
        print("""<div class="card" style="width: 18rem;">
        <img class="card-img-top" src="..." alt="Card image cap">
        <div class="card-body">
        <h5 class="card-title"></h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <a href="#" class="btn btn-primary">Place Order</a>
        </div>
        </div>""")

else:
    print("<h2>Please enter right credentials</h2>")