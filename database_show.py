import sqlite3
# Connect to the database
conn = sqlite3.connect('fatora_database.db')

# Create a cursor object
c = conn.cursor()

# Build the SELECT statement
select_stmt = "SELECT * FROM products"

# Execute the statement
c.execute(select_stmt)

# Fetch all the rows
rows = c.fetchall()

# Iterate through the rows
for row in rows:
    print(row)

# Close the cursor and connection
c.close()
conn.close()
