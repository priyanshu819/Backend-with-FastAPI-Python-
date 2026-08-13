import sqlite3
import os

# Check current working directory
print('Current directory:', os.getcwd())

# Use correct path to database - it's in the same folder as this script
db_path = os.path.join(os.path.dirname(__file__), 'test.db')
print('Database path:', db_path)

conn=sqlite3.connect(db_path)
cursor=conn.cursor()

# list all tables in databse
cursor.execute("SELECT name FROM sqlite_master WHERE type ='table';")
tables=cursor.fetchall()
print('Tables:',tables)
print('Number of tables:', len(tables))

# Query from the first table
if tables:
    table_name=tables[0][0]
    cursor.execute(f"SELECT * FROM {table_name}")
    rows=cursor.fetchall()
    for row in rows:
        print(row)

conn.close()