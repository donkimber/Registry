import sqlite3

con = sqlite3.connect('db.sqlite3')
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
for line in cursor.fetchall():
    print line

