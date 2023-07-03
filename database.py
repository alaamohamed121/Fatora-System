import sqlite3

# Connect to or create a database file
conn = sqlite3.connect('fatora_database.db')

# Create a cursor object
c = conn.cursor()

# Create a table with columns for id, name, quantity, price, and company
c.execute('''CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, price REAL, company TEXT ,country TEXT)''')


# Commit the changes and close the connection
conn.commit()
conn.close()
