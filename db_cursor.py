# -*- coding: utf-8 -*-

import sqlite3
#from sqlite3.dbapi2 import Cursor

# conection to the data base
conn = sqlite3.connect(':memory:')

# cursor
cursor = conn.cursor()

# create table
cursor.execute("""CREATE TABLE currency 
            (ID integer primary key, name text, symbol text)""")

# Insert coin data
cursor.execute("INSERT INTO currency VALUES(1,'Peso (ARG)','$')")
cursor.execute("INSERT INTO currency VALUES(2, 'Dolar', 'U$S')")

# save the cahnges
conn.commit()

# I consult the coins
query = "SELECT * FROM currency"

# search the result 
currencies = cursor.execute(query).fetchone()
print(currencies)

print(cursor.fetchone())
print(cursor.fetchone())

currencies = cursor.execute(query).fetchall()
print(currencies)

# close data base
conn.close()