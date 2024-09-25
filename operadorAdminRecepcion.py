from registro import  impresion, registro_vehicular

turno = registro_vehicular()

montoAbonar = int(input("Ingrese el monto a cobrar: "))
turno["monto"] = montoAbonar
impresion(turno)

