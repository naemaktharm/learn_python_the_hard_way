import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create table
c.execute('''SELECT * FROM stocks''')

print c.fetchone()

conn.close()