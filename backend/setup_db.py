import sqlite3
import pandas as pd
from tabulate import tabulate

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect("planes_cozy.db")
cursor = conn.cursor()

# Crear la tabla de planes
cursor.execute('''
CREATE TABLE IF NOT EXISTS planes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    icono TEXT,
    titulo TEXT NOT NULL,
    tier TEXT CHECK(tier IN ('bronze', 'silver', 'gold')) NOT NULL,
    descripcion TEXT NOT NULL,
    materiales TEXT,
    indoor_outdoor TEXT CHECK(indoor_outdoor IN ('indoor', 'outdoor', 'both')) NOT NULL
)
''')

# Leer los datos desde el archivo Excel
file_path = 'data/planes_cozy.csv'
df = pd.read_csv(file_path, delimiter=",", quotechar='"')

# Asegurarse de que las columnas del archivo Excel coinciden con los nombres esperados
# Suponiendo que el archivo tiene las columnas: 'icono', 'titulo', 'tier', 'descripcion', 'detalles', 'indoor_outdoor'
# Si es necesario, puedes modificar estos nombres en el DataFrame para que coincidan con la estructura de la base de datos

# Insertar los datos leídos en la base de datos
for _, row in df.iterrows():
    cursor.execute('''
    INSERT INTO planes (icono, titulo, tier, descripcion, materiales, indoor_outdoor)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (row['icono'], row['titulo'], row['tier'], row['descripcion'], row['materiales'], row['indoor_outdoor']))

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()

print("Base de datos actualizada con los datos del archivo Excel.")

# Función para visualizar los planes de manera cuca
def visualizar_planes():
    conn = sqlite3.connect("planes_cozy.db")
    df = pd.read_sql_query("SELECT icono, titulo, tier, indoor_outdoor, descripcion FROM planes", conn)
    conn.close()
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

# Llamar a la función para ver los planes
visualizar_planes()
