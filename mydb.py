import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mysql123'
)

# prepare a cursor object
cursorObject  = dataBase.cursor()

# create a datbase
cursorObject.execute('CREATE DATABASE elderco')

print('All done')