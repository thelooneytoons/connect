import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sql-instance-4",
  database="sql-db-2",
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Divakar", "1234567890")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")