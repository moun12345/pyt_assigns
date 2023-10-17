import sqlite3

connection = sqlite3.connect('store.db')
cursor = connection.cursor()
#creating table

comm1 = """CREATE TABLE IF NOT EXISTS 
stores(store_id INTEGER PRIMARY KEY, location TEXT)"""

cursor.execute(comm1)

connection.commit()
connection.close()