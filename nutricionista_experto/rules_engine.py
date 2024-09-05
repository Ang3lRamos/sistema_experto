def diagnosticar_problema(sintomas, modelo):
    problemas = []

    # Reglas para diagnóstico en base a síntomas y modelo de vehículo
    if "no arranca" in sintomas:
        if "clic" in sintomas:
            problemas.append("Posible falla en la batería o el motor de arranque.")
        if "tablero apagado" in sintomas:
            problemas.append("Posible falla eléctrica o batería completamente descargada.")
        if "luces encendidas" in sintomas:
            problemas.append("Posible problema con el motor de arranque o fusibles.")
        if "humo" in sintomas:
            problemas.append("Posible cortocircuito o sobrecalentamiento en el sistema eléctrico.")
    
    if "ruido del motor" in sintomas:
        if "no arranca" not in sintomas:
            problemas.append("Posible problema con las bujías, filtros, o el sistema de combustión.")
        if "humo" in sintomas:
            problemas.append("Posible sobrecalentamiento del motor o problemas en el sistema de escape.")
    
    if "frenos" in sintomas:
        if "ruido al frenar" in sintomas:
            problemas.append("Posible desgaste en las pastillas de freno o discos.")
        else:
            problemas.append("Posible falla en el sistema de frenos o falta de líquido de frenos.")
    
    # Reglas para problemas eléctricos
    if "tablero apagado" in sintomas:
        if "luces encendidas" in sintomas:
            problemas.append("Falla en el sistema eléctrico o alternador defectuoso.")
        else:
            problemas.append("Posible batería descargada o fusibles quemados.")
    
    if "luces encendidas" in sintomas:
        problemas.append("Sistema eléctrico en funcionamiento, pero posible problema con el alternador o batería.")
    
    # Reglas adicionales para modelos específicos
    if modelo == "SUV":
        if "humo" in sintomas and "no arranca" in sintomas:
            problemas.append("Posible sobrecalentamiento del motor o problema grave con el sistema de encendido en SUVs.")
        if "frenos" in sintomas:
            problemas.append("Los SUVs pueden tener desgaste acelerado en los frenos debido al peso del vehículo.")

    if modelo == "Camión":
        if "humo" in sintomas:
            problemas.append("Posible problema en el sistema de inyección de combustible en camiones.")
        if "ruido del motor" in sintomas:
            problemas.append("Posible problema con los inyectores o turbocompresor en camiones.")

    if modelo == "Motocicleta":
        if "ruido del motor" in sintomas:
            problemas.append("Posible fallo en el sistema de encendido o escape de la motocicleta.")
        if "frenos" in sintomas:
            problemas.append("Posible desgaste acelerado en los frenos de la motocicleta.")
    
    # Si no se encuentran problemas coincidentes
    if not problemas:
        problemas.append("No se encontraron problemas coincidentes con los síntomas seleccionados.")
    
    return problemas
