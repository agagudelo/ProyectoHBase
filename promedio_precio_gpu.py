import happybase
from datetime import datetime

try:

    connection = happybase.Connection('localhost')
    table = connection.table('laptops')
	
	gpu_data = {}

    
    for key, data in table.scan():
        try:
            # Obtener GPU_Company y el precio
            gpu_company = data.get(b'gpu:gpu_company', b'').decode().strip()
            price = data.get(b'price:euro', b'')

       
            if not gpu_company or not price:
                print(f"Advertencia: Fila con clave '{key.decode()}' tiene GPU_Company o precio vacío.")
                continue

            try:
                price = float(price.decode())
            except ValueError:
                print(f"Advertencia: Precio inválido en la fila con clave '{key.decode()}': '{price.decode()}'")
                continue

            # Sumar precios y contar por GPU_Company
            if gpu_company not in gpu_data:
                gpu_data[gpu_company] = {'sum': 0.0, 'count': 0}
            gpu_data[gpu_company]['sum'] += price
            gpu_data[gpu_company]['count'] += 1

        except Exception as e:
            print(f"Error procesando la fila '{key.decode()}': {e}")

    # Calcular y mostrar promedios
    print("\n=== Promedio de Precio por GPU_Company ===")
    for gpu, values in gpu_data.items():
        if values['count'] > 0:
            avg_price = values['sum'] / values['count']
            print(f"GPU Company: {gpu}, Promedio de Precio: {avg_price:.2f} Euros")
        else:
            print(f"GPU Company: {gpu} no tiene precios válidos para calcular el promedio.")




except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Cerrar la conexión
    connection.close()