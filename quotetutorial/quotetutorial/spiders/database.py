import sqlite3

conn = sqlite3.connect("myquotes.db")
# creating a connection
cursor = conn.cursor()
# cursor are structures that allow us to do actions
# while we are running the registers

# cursor.execute("""CREATE TABLE quotes
#                 (title TEXT,
#                 author TEXT,
#                 tag TEXT)""")
# here I am using the dot execute to create a table

cursor.execute("""INSERT INTO quotes VALUES('Python is awesome', 'pedrozamorini', 'python')""")

conn.commit()
# using to save the changes in the db
conn.close()
# it is a god practice to close the connection
