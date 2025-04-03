def add_service(services):
    nombre = input("Nombre del paquete fotográfico: ")
    precio = float(input("Precio del paquete: "))
    tipo_evento = input("Tipo de evento (boda, retrato, etc.): ")
    duracion = float(input("Duración estimada (en horas): "))
    
    service = {
        "nombre": nombre,
        "precio": precio,
        "tipo_evento": tipo_evento,
        "duracion": duracion
    }
    services.append(service)
