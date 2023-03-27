import sqlite3

# Establish a connection to the database
con = sqlite3.connect('vendors.db')

# Create a cursor object
cur = con.cursor()

# Execute SQL commands to create the table
cur.execute('''CREATE TABLE vendors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                address TEXT,
                city TEXT,
                state TEXT,
                zip TEXT,
                phone TEXT,
                email TEXT,
                latitude REAL,
                longitude REAL
            );''')

# Insert some data into the table
cur.execute('''INSERT INTO vendors (name, address, city, state, zip, phone, email, latitude, longitude)
                VALUES ('Vendor A', '123 Bosso Town', 'minna', 'Niger', '12345', '555-123-4567', 'vendorA@example.com', 9.652219, 6.52606),
                       ('Vendor B', '456 Chanchaga', 'minna', 'Niger', '67890', '555-234-5678', 'vendorB@example.com', 9.6278, 6.5463),
                       ('Vendor C', '789 Maitunbi', 'minna', 'Niger', '45678', '555-345-6789', 'vendorC@example.com', 9.6316, 6.5719);''')

# Commit changes to the database
con.commit()

# Get al rows and all columns by order
cur.execute("SELECT * FROM vendors")
print(cur.fetchall())


# Close the database connection
con.close()

# import sqlite3
#
# # Establish a connection and create a cursor
# con = sqlite3.connect('vendors.db')
# cur = con.cursor()
#
# # Get al rows and all columns by order
# cur.execute("SELECT * FROM vendors")
# print(cur.fetchall())