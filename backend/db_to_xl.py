import sqlite3
import pandas as pd

# Conectar a la base de datos SQLite
conn = sqlite3.connect('planes_cozy.db')

# Leer los datos de la tabla 'planes' en un DataFrame
df = pd.read_sql_query("SELECT * FROM planes", conn)

# Cerrar la conexión a la base de datos
conn.close()

# Exportar el DataFrame a un archivo Excel
excel_file = 'planes_cozy.xlsx'
df.to_excel(excel_file, index=False, engine='openpyxl')

print(f"Los datos se han exportado exitosamente a {excel_file}")
