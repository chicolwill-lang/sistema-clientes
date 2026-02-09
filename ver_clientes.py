import sqlite3

conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM clientes")
cantidad = cursor.fetchone()[0]

print("Clientes en la base de datos:", cantidad)

conn.close()
