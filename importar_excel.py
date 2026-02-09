import pandas as pd
import sqlite3

df = pd.read_excel("clientes.xlsx")

conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

for _, fila in df.iterrows():
    plan = int(fila["plan"])  # 👈 aseguramos número

    cursor.execute(
        "INSERT INTO clientes (nombre, plan) VALUES (?, ?)",
        (fila["nombre"], plan)
    )

conn.commit()
conn.close()

print("Clientes importados correctamente")
