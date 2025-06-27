import random

def generate_instance_specific(instance_name, num_clients, connectivity_percentage):
    """
    Genera una instancia específica del problema de distribución con un número de nodos y conectividad dados.

    Args:
        instance_name (str): Nombre de la instancia (e.g., "instance_120_nodes_80_percent_connected").
        num_clients (int): Cantidad de clientes (nodos).
        connectivity_percentage (float): Porcentaje de conectividad (ej. 0.8 para 80%).
    """

    # Parámetros fijos o con rangos para esta instancia específica
    # Ajusta estos valores según tus necesidades, ya que no se especificaron en la solicitud
    cost_repartidor = random.randint(30, 80)
    d_max = random.randint(50, 150)

    # Clientes refrigerados: 10-20% aleatorio
    num_refrigerated = int(num_clients * random.uniform(0.1, 0.2))
    refrigerated_clients = random.sample(range(1, num_clients + 1), num_refrigerated)

    # Clientes exclusivos: 5-15% aleatorio
    num_exclusivos = int(num_clients * random.uniform(0.05, 0.15))
    exclusivos_clients = random.sample(range(1, num_clients + 1), num_exclusivos)

    # Generar distancias y costos
    distances_costs_list = []
    for i in range(1, num_clients + 1):
        for j in range(1, num_clients + 1):
            if i == j:
                # Distancia y costo 0 para el mismo nodo
                # No se escriben en el archivo si se sigue la lógica de "no figuran" para grandes.
                # Pero si se desea incluirlos explícitamente para el modelado, aquí estarían.
                pass
            else:
                if random.random() < connectivity_percentage:
                    dist = random.randint(100, 1000) # Rango de distancias para 120 nodos
                    cost = random.randint(100, 1000) # Rango de costos para 120 nodos
                    distances_costs_list.append(f"{i} {j} {dist} {cost}\n")

    # Crear el archivo de instancia
    with open(f"{instance_name}.txt", "w") as f:
        f.write(f"{num_clients}\n") # cant_clientes
        f.write(f"{cost_repartidor}\n") # costo_repartidor
        f.write(f"{d_max}\n") # dist_max

        f.write(f"{num_refrigerated}\n") # cant_refrigerados
        for client_id in refrigerated_clients:
            f.write(f"{client_id}\n") # id de clientes refrigerados

        f.write(f"{num_exclusivos}\n") # cant_exclusivos
        for client_id in exclusivos_clients:
            f.write(f"{client_id}\n") # id de clientes exclusivos

        # Escribir distancias y costos solo para las conexiones generadas
        for line in distances_costs_list:
            f.write(line)

# --- Generación de la instancia específica ---
if __name__ == "__main__":
    print("Generando instancia específica...")

    generate_instance_specific(
        instance_name="instance_120_nodes_80_percent_connected",
        num_clients=120,
        connectivity_percentage=0.8 # Asumiendo 80% de conectividad
    )
