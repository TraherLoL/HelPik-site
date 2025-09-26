import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

def ProductDB():
    ListDb = cursor.execute('SELECT * FROM produkt')
    connection.close()
    return ListDb.fetchall()
