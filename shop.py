#!C:\Users\israr\AppData\Local\Programs\Python\Python38-32\python.exe


import cgitb
cgitb.enable()
import cgi


print("content-type: text/html\n\n" )
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="shopDatabase",
)

sql_select_Query = "select * from products"
cursor = mydb.cursor()
cursor.execute(sql_select_Query)
# get all records
total_products = cursor.fetchall()
print("<h1>Total number of rows in table: </h1>", cursor.rowcount)

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
from jinja2 import Template
for data in total_products:
  name=data[1]
  desc=data[2]
  price=data[3]
  img=data[4]
  date=data[5]
  print(name)
  print("""
<div class="card" style="width: 18rem;">
  <img class="card-img-top" src='{{img}}' alt="Card image cap">
  <div class="card-body">
    <h5 class="card-title">{{name}}</h5>
    <p class="card-text">{{desc}}</p>
    <a href="#" class="btn btn-primary">Place Order</a>
  </div>
</div>""")

print("""
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>""")

