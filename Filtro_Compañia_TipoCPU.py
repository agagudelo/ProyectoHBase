import happybase
from datetime import datetime

try:
	
    connection = happybase.Connection('localhost')
    table = connection.table('laptops')
	
	# Filtro para obtener solo los registros de ASUS con CPU tipo 'Core i7 7500U'
	filter_str = "SingleColumnValueFilter('cpu', 'cpu_type', =, 'binary:Core i7 7500U') AND " \
             "SingleColumnValueFilter('company', 'name', =, 'binary:Asus')"

	
	print("=== Registros de ASUS con CPU tipo 'Core i7 7500U' ===")
	for key, data in table.scan(filter=filter_str.encode()):
		print(f"Clave: {key.decode()}")
		print(f"Compañía: {data[b'company:name'].decode()}")
		print(f"Producto: {data[b'company:product'].decode()}")
		print(f"Tipo de CPU: {data[b'cpu:cpu_type'].decode()}")
		print(f"Precio: {data[b'price:euro'].decode()}")
		print("-" * 40)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Cerrar la conexión
    connection.close()