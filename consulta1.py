import happybase
from datetime import datetime

try:

    connection = happybase.Connection('localhost')
    table = connection.table('laptops')
	
    print("Conexión establecida con HBase")

    print("\n=== Se muestra los primeros 5 laptops ===")
	count = 0
	for key, data in table.scan():
		if count < 5: 
			print(f"\nLaptop  ID: {key.decode()}")
			print(f"Compañia: {data[b'company:name'].decode()}")
			print(f"Producto: {data[b'company:product'].decode()}")
			print(f"Tipo de CPU: {data[b'cpu_type'].decode()}")
			print(f"RAM: {data[b'memory:ram'].decode()}")
			print(f"Precio: {data[b'price:euro'].decode()}")
			count += 1
        else:
            break
          
           
except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Cerrar la conexión
    connection.close()
		