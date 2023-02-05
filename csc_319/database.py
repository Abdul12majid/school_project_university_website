import mysql.connector

my_db = mysql.connector.connect(host="localhost", user="root", passwd="Non12$ense")

my_cursor = my_db.cursor()
my_cursor.execute("CREATE DATABASE csc_319_db")
my_cursor.execute("SHOW DATATBASES")

for db in my_cursor:
	print(db)