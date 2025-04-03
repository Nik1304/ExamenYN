def add_service(servicio):
    nombre = input("Nombre del paquete fotográfico: ")
    precio = float(input("Precio del paquete: "))
    tipo_evento = input("Tipo de evento (boda, retrato, etc.): ")
    duracion = float(input("Duración estimada (en horas): "))
    
    servicio = {
        "nombre": nombre,
        "precio": precio,
        "tipo_evento": tipo_evento,
        "duracion": duracion
    }
    servicio.append(servicio)
    
