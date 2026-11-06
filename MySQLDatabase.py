import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database ="StudentDB"
)
mycursor = mydb.cursor()
mycursor.execute("""
                CREATE TABLE IF NOT EXISTS Student (
                StudentID INT PRIMARY KEY,"
                Name VARCHAR(50),
                Department VARCHAR(50)
               )
            """)
print("Database created")
