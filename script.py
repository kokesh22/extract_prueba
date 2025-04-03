import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Juan Pérez'],
    'Edad': [30],
    'Ciudad': ['Madrid']
}
df = pd.DataFrame(data)

# Guardar el DataFrame como CSV localmente
csv_filename = 'sample_data.csv'
df.to_csv(csv_filename, index=False)
print(f"Archivo {csv_filename} guardado localmente.")
