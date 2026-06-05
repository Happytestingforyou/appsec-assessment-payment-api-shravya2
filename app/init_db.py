import sqlite3 
conn = sqlite3.connect("payments.db") 
cursor = conn.cursor() 
cursor.execute("DROP TABLE IF EXISTS users") 
cursor.execute("DROP TABLE IF EXISTS payments") 
cursor.execute(""" 
CREATE TABLE users ( 
id INTEGER PRIMARY KEY, 
username TEXT, 
password TEXT, 
role TEXT 
) 
""") 
cursor.execute(""" 
CREATE TABLE payments ( 
id INTEGER PRIMARY KEY, 
username TEXT, 
amount INTEGER, 
status TEXT 
) 
""") 
cursor.execute("INSERT INTO users VALUES (1, 'admin', 'Admin@123', 
'admin')") 
cursor.execute("INSERT INTO users VALUES (2, 'alice', 'Alice@123', 
'user')") 
cursor.execute("INSERT INTO users VALUES (3, 'bob', 'Bob@123', 'user')") 
cursor.execute("INSERT INTO payments VALUES (1, 'alice', 5000, 
'processed')") 
cursor.execute("INSERT INTO payments VALUES (2, 'bob', 7500, 'pending')") 
cursor.execute("INSERT INTO payments VALUES (3, 'admin', 99999, 
'approved')") 
conn.commit() 
conn.close() 
print("Database initialized successfully") 
