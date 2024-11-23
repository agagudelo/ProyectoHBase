import happybase
from datetime import datetime

try:

    connection = happybase.Connection('localhost')
    table = connection.table('laptops')
	
	# Filtro para obtener laptops cuyo precio esté entre 1000 y 1500 euros
	filter_str = "SingleColumnValueFilter('price', 'euro', >, 'binary:1000') AND " \
				 "SingleColumnValueFilter('price', 'euro', <, 'binary:1500')"

	# Realizar el escaneo con el filtro
	print("=== Laptops con precio entre 1000 y 1500 Euros ===")
	for key, data in table.scan(filter=filter_str.encode()):
		print(f"Clave: {key.decode()}")
		print(f"Compañía: {data[b'company:name'].decode()}")
		print(f"Producto: {data[b'company:product'].decode()}")
		print(f"Precio: {data[b'price:euro'].decode()} Euros")
		print("-" * 40)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Cerrar la conexión
    connection.close()