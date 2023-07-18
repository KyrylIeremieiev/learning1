import mysql.connector as connector

conn = connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pythonDB")

sql = "CREATE TABLE relics (name VARCHAR(225), expansion VARCHAR(20));"

mycursor = conn.cursor()

mycursor.execute(sql)

#comman line program with class start asks for
#create if not exist