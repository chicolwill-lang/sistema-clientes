import sqlite3

conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    plan TEXT NOT NULL
)
""")



conn.commit()
conn.close()
