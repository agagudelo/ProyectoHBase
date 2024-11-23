import happybase
from datetime import datetime

try:

    connection = happybase.Connection('localhost')
    table = connection.table('laptops')
	
	
    count_asus = 0
    count_dell = 0

    for key, data in table.scan():
        company = data.get(b'company:name', b'').decode()  # Obtener la columna company:name
        if company == 'Asus':
            count_asus += 1
        elif company == 'Dell':
            count_dell += 1

    
    print(f"Cantidad de equipos Asus: {count_asus}")
    print(f"Cantidad de equipos Dell: {count_dell}")


except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Cerrar la conexión
    connection.close()