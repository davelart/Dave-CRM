import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'P@$$w@rd123'
)

# prepare a cursor.object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute('CREATE DATABASE decipher')

print('All Done!')