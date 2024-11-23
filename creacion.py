import happybase
import pandas as pd
from datetime import datetime

# Bloque principal de ejecución
try:
	# 1. Establecer conexión con HBase
	connection = happybase.Connection('localhost')
	print("Conexión establecida con HBase")
	
	# 2. Crear la tabla con las familias de columnas
	table_name = 'laptops'
	families = {
	'company': dict(),  # Familia para datos de la compañía y producto
	'display': dict(),  # Familia para datos de la pantalla
	'cpu': dict(),      # Familia para datos del CPU
    'memory': dict(),   # Familia para datos de memoria
    'gpu': dict(),      # Familia para datos del GPU
    'system': dict(),   # Familia para datos del sistema operativo y peso
    'price': dict()     # Familia para el precio
	}
	
	# Eliminar la tabla si ya existe
	if table_name.encode() in connection.tables():
		print(f"Eliminando tabla existente - {table_name}")
		connection.delete_table(table_name, disable=True)
	
	# Crear nueva tabla
	connection.create_table(table_name, families)
	table = connection.table(table_name)
	print("Tabla 'laptops' creada exitosamente")
	
	# 3. Cargar company del CSV
	laptops_data = pd.read_csv('laptop_price-dataset.csv')
	
	# Iterar sobre el DataFrame usando el índice
	for index, row in laptops_data.iterrows():
		# Generar row key basado en el índice
		row_key = f'laptop_{index:04d}'.encode()
		
	# Organizar los company en familias de columnas
        data = {
            b'company:name': str(row['Company']).encode(),
            b'company:product': str(row['Product']).encode(),
            
            b'display:type_name': str(row['TypeName']).encode(),
            b'display:inches': str(row['Inches']).encode(),		
            b'display:resolution': str(row['ScreenResolution']).encode(),
            
            b'cpu:cpu_company': str(row['CPU_Company']).encode(),
            b'cpu:cpu_type': str(row['CPU_Type']).encode(),
            b'cpu:cpu_frequency': str(row['CPU_Frequency (GHz)']).encode(),
            
            b'memory:ram': str(row['RAM (GB)']).encode(),
            b'memory:storage': str(row['Memory']).encode(),
            
            b'gpu:gpu_company': str(row['GPU_Company']).encode(),
            b'gpu:gpu_type': str(row['GPU_Type']).encode(),
            
            b'system:os': str(row['OpSys']).encode(),
            b'system:weight': str(row['Weight (kg)']).encode(),
            
            b'price:euro': str(row['Price (Euro)']).encode(),
        }
	
        table.put(row_key, data)
        
	print("Datos cargados exitosamente")
	
except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Cerrar la conexión
    connection.close()
	