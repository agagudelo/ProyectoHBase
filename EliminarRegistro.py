import happybase
from datetime import datetime

try:
	
    connection = happybase.Connection('localhost')
    table = connection.table('laptops')
	#Eliminar un registro
    row_key = b'laptop_0123'
	table.delete(row_key)
	print(f"Registro con clave {row_key.decode()} eliminado.")

	
	
except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Cerrar la conexión
    connection.close()