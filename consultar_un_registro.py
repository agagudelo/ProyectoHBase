import happybase
from datetime import datetime

try:

    connection = happybase.Connection('localhost')
    table = connection.table('laptops')

    # Recuperar un registro específico por clave
    row_key = b'laptop_0123'
    data = table.row(row_key)
    if data:
        print(f"Datos del registro con clave {row_key.decode()}:")
        for key, value in data.items():
            print(f"{key.decode()}: {value.decode()}")
    else:
        print("No se encontró el registro.")

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Cerrar la conexión
    connection.close()