import happybase
from datetime import datetime

try:

    connection = happybase.Connection('localhost')
    table = connection.table('laptops')

    # Actualizar datos del registro 
	row_key = b'laptop_0123'
	updated_data = {
		b'price:euro': b'1500',  # Actualiza el precio
		b'memory:ram': b'32',    # Actualiza la RAM
	}

	table.put(row_key, updated_data)
	print(f"Datos actualizados para la clave: {row_key.decode()}")


except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Cerrar la conexión
    connection.close()