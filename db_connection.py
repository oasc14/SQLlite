# coding -*- coding: utf-8 -*-

import sqlite3
import hashlib

# connection to the db
conn = sqlite3.connect(':memory:')

# cursor
cursor = conn.cursor()

# create table
cursor.execute("""CREATE TABLE currency 
            (ID integer primary key, name text, symbol text)""")

# save changes
conn.commit()

# Insert coin data
cursor.execute("INSERT INTO currency VALUES(1,'Peso (ARG)','$')")
cursor.execute("INSERT INTO currency VALUES(2, 'Dolar', 'U$S')")

# revert the changes
conn.rollback()

# I consult the coins
query = "SELECT * FROM currency"

# search the result 
currencies = cursor.execute(query).fetchall()

print(currencies)

# close data base
conn.close()

# create function
def md5sum(t):
    return hashlib.md5(t).hexdigest()

conn = sqlite3.connect(":memory:")
conn.create_function("md5",1,md5sum)
cursor = conn.cursor()
cursor.execute("select md5(?)", (b"foo",))
print(cursor.fetchone()[0])

# close db connection
conn.close()

class MySum:
    def __init__(self):
        self.count = 0
    
    def step(self,value):
        self.count += value

    def finalize(self):
        return self.count

conn = sqlite3.connect(":memory:")
conn.create_aggregate("mysum", 1, MySum)
cursor = conn.cursor()
cursor.execute("create table test(i)")
cursor.execute("insert into test(i) values(1)")
cursor.execute("insert into test(i) values(2)")
cursor.execute("select mysum(i) from test")
print(cursor.fetchone()[0])

# close db connection
conn.close()
