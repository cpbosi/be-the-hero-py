import sqlite3

con = sqlite3.connect("ong.db")
print("Database connected successfully!")

con.execute("create table Ong(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, whatsapp TEXT)")  
print("Table ONG created successfully!")

con.close()