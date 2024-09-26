#DECLARACIONES

#FUNCIONES
"""def menu:
    print ("1 - Inscripcion")
    print ("2 - Seleccion de Fecha")
    print ("3 - Impresion")
    print ("0 - Salir del programa")
    return"""
def registro_vehicular(): #Carga y verificacion de datos
    
    nombreTitular = input("Ingrese su nombre y apellido: ")
    nombreTitular = nombreTitular.upper()
    
    dni = int (input("Ingrese su numero de DNI: "))
    while dni < 15000000 or dni > 60000000:
        print("Numero de DNI invalido!")
        dni = int (input("Ingrese su numero de DNI: "))
    
    dominio = input("Ingrese el numero de dominio del vehiculo: ")
    while len(dominio) != 6:
        print("Numero de dominio invalido")
        dominio = input("Ingrese el numero de dominio del vehiculo: ")
    dominio = dominio.upper()
    
    tipoDeVehiculo = input("Ingrese el tipo de vehiculo('auto=1','moto=2' o 'camion=3'):")
    tipoDeVehiculo = tipoDeVehiculo.upper()
    
    marca = input("Ingrese marca del vehiculo: ")
    marca = marca.upper()
    
    modelo = (input("Ingrese modelo del vehiculo: "))
    modelo = modelo.upper()
    
    año = int (input("Ingrese año del vehiculo: "))
    while año < 1910 or año > 2024:
        print("Año del vehiculo erroneo!")
        año = int (input("Ingrese año del vehiculo: "))
    
    vehiculo = {
        "Tipo" : tipoDeVehiculo,
        "dominio": dominio,
        "dni": dni,
        "nombre": nombreTitular,
        "modelo": modelo,
        "marca": marca,
        "año": año
    }
    
    return vehiculo

"""def fecha_hora (cargaInicial): #Seleccion de fecha y hora del turno y carga en variable global.
    return turno"""

def impresion (vehiculo):#Impresion por pantalla del resumen del turno
    print("\nResumen del turno solicitado:")
    print(f"Dominio del vehículo: {vehiculo['dominio']}")
    print(f"DNI del titular: {vehiculo['dni']}")
    print(f"Nombre del titular: {vehiculo['nombre']}")
    print(f"Modelo del vehículo: {vehiculo['modelo']}")
    print(f"Marca del vehículo: {vehiculo['marca']}")
    print(f"Año del vehículo: {vehiculo['año']}")
    print(f"El monto a abonar es: {vehiculo['monto']}")
#PRINCIPAL
