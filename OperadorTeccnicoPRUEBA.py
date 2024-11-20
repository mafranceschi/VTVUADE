from operadorAdminRecepcion import turno
vehiculos = {1:'Auto', 2:'Moto', 3:'Camion'}
#FUNCIONES

def verificar_vehiculo(numero): #Controla que la opcion seleccionada sea correcta 
    while numero < 1 or numero > 3:
        print("ERROR")
        numero = int(input("Ingrese un numero en pantalla: "))
    return numero

def contar_puntajes(puntajes):
    contar = lambda puntajes, valor: puntajes.count(valor)
    mal = contar(puntajes,0)
    regular = contar(puntajes,1)
    bien = contar(puntajes,2)
    return mal, regular, bien

def verificar_puntaje(mensaje):
    valor = int(input(mensaje))
    while valor < 0 or valor > 2:
        print("Valor incorrecto")
        valor = int(input("Ingrese el numero correcto: "))
    return valor 

def verificacion_automovil(): #Proceso tecnico del auto
    puntajeInterior = []
    puntajeExterior = []
    puntajeMecanica = []
    print("\nVerificacion Interior") #Verificacion tecnica del interior
    puertas = verificar_puntaje("Cierre de las puertas: ")
    ventanillas = verificar_puntaje("Visibilidad de las ventanillas: ")
    parabrisas = verificar_puntaje("Visibilidad del parabrisas: ")
    cinturones = verificar_puntaje("Tension y anclaje del cinturon: ")
    asientos = verificar_puntaje("Anclaje de asientos: ")
    apoyaCabezas = verificar_puntaje("Anclaje de apoyacabezas: ")
    espejos = verificar_puntaje("Visibilidad de los espejos: ")
    bocina = verificar_puntaje("Comando de bocina: ")
    print("")
    comentariosUno = input("Comentarios: ")
    print("")
    print("Verificacion Exterior") #Verificacion tecnica del exterior 
    alineacionLuces = verificar_puntaje("Alineacion de luces de corto y largo alcance: ")
    intencidadLuces = verificar_puntaje("Intencidad de luces de corto y largo alcance: ")
    lucesPosicion = verificar_puntaje("Encendido de luces de posicion: ")
    lucesFreno = verificar_puntaje("Encendido de luces de Freno: ")
    lucesReversa = verificar_puntaje("Encendido de luces de Reversa: ")
    lucesIntermitentes = verificar_puntaje("Encendido de luces intermitentes: ")
    alcanceBocina = verificar_puntaje("Alcance de la Bocina: ")
    limpiaParabrisas = verificar_puntaje("Funcionamiento y estado de las escobillas: ")
    print("")
    comentariosDos = input("Comentarios: ")
    print("")
    print("Verificacion Mecanica") #Verificacion tecnica de mecanica
    alineacionEjeDelantero = verificar_puntaje("Alineacion del eje delantero: ")
    frenos = verificar_puntaje("Sistema de frenos: ")
    direccion = verificar_puntaje("Mecanismo de direccion: ")
    roturasFugasEscape = verificar_puntaje("Estado del sistema de escape: ")
    ruidoEscape = verificar_puntaje("Nivel de ruido del escape: ")
    suspencion = verificar_puntaje("Estado de la suspencion: ")
    funcionamientoSuspencion = verificar_puntaje("Funcionamiento de la suspencion: ")
    inferior = verificar_puntaje("Estado de la parte inferior: ")
    print("")
    comentariosTres = input("Comentarios: ")
    puertas = int(input("Cierre de las puertas: "))
    ventanillas = int(input("Visibilidad de las ventanillas: "))
    parabrisas = int(input("Visibilidad del parabrisas: "))
    cinturones = int(input("Tension y anclaje del cinturon: "))
    asientos = int(input("Anclaje de asientos: "))
    apoyaCabezas = int(input("Anclaje de apoyacabezas: "))
    espejos = int(input("Visibilidad de los espejos: "))
    bocina = int(input("Comando de bocina: "))
    print("Verificacion Exterior") #Verificacion tecnica del exterior 
    alineacionLuces = int(input("Alineacion de luces de corto y largo alcance: "))
    intencidadLuces = int(input("Intencidad de luces de corto y largo alcance: "))
    lucesPosicion = int(input("Encendido de luces de posicion: "))
    lucesFreno = int(input("Encendido de luces de Freno: "))
    lucesReversa = int(input("Encendido de luces de Reversa: "))
    lucesIntermitentes = int(input("Encendido de luces intermitentes: "))
    alcanceBocina = int(input("Alcance de la Bocina: "))
    limpiaParabrisas = int(input("Funcionamiento y estado de las escobillas: "))
    print("Verificacion Mecanica") #Verificacion tecnica de mecanica
    alineacionEjeDelantero = int(input("Alineacion del eje delantero: "))
    frenos = int(input("Sistema de frenos: "))
    direccion = int(input("Mecanismo de direccion: "))
    roturasFugasEscape = int(input("Estado del sistema de escape: "))
    ruidoEscape = int(input("Nivel de ruido del escape: "))
    suspencion = int(input("Estado de la suspencion: "))
    funcionamientoSuspencion = int(input("Funcionamiento de la suspencion: "))
    inferior = int(input("Estado de la parte inferior: "))

    puntajeInterior.extend([puertas, ventanillas, parabrisas, cinturones, asientos, apoyaCabezas, espejos, bocina])
    puntajeExterior.extend([alineacionLuces, intencidadLuces, lucesPosicion, lucesFreno, lucesReversa, lucesIntermitentes, alcanceBocina, limpiaParabrisas])
    puntajeMecanica.extend([alineacionEjeDelantero, frenos, direccion, roturasFugasEscape, ruidoEscape, suspencion, funcionamientoSuspencion, inferior])
    
    comentarios = {
        "Interior": comentariosUno,
        "Exterior": comentariosDos,
        "Mecanica": comentariosTres
        }
    
    
    return puntajeInterior, puntajeExterior, puntajeMecanica, comentarios

def verificacion_moto(): #Proceso tecnico de la moto
    puntajeExterior = []
    puntajeMecanico = []
    puntajeConductor = []
    print("Verificacion exterior")
    alineacionLuces = verificar_puntaje("Alineacion de luces de corto y largo alcance: ")
    intencidadLuces = verificar_puntaje("Intencidad de luces de corto y largo alcance: ")
    lucesPosicion = verificar_puntaje("Encendido de luces de posicion: ")
    lucesFreno = verificar_puntaje("Encendido de luces de Freno: ")
    lucesIntermitentes = verificar_puntaje("Encendido de luces intermitentes: ")
    alcanceBocina = verificar_puntaje("Alcance de la Bocina: ")
    nChasis = verificar_puntaje("Numero de chasis legible: ")
    print("")
    comentariosUno = input("Comentarios: ")
    print("")
    print("Verificacion Mecanica")
    manubrio = verificar_puntaje("Alineacion y estado del manubrio: ")
    frenos = verificar_puntaje("Sistema de frenos: ")
    roturasFugasEscape = verificar_puntaje("Estado del sistema de escape: ")
    ruidoEscape = verificar_puntaje("Nivel de ruido del escape: ")
    suspencion = verificar_puntaje("Estado de la suspencion: ")
    funcionamientoSuspencion = verificar_puntaje("Funcionamiento de la suspencion: ")
    chasis = verificar_puntaje("Estado del chasis")
    cubiertas = verificar_puntaje("Estado de las cubiertas: ")
    print("")
    comentariosDos = input("Comentarios: ")
    print("")
    print("Verificacion Conductor")
    casco = verificar_puntaje("Estado general del casco: ")
    ropa = verificar_puntaje("Estado general de ropa protectora: ")
    comentariosTres = input("Comentarios: ")
    puntajeExterior.extend([alineacionLuces, intencidadLuces, lucesPosicion, lucesFreno, lucesIntermitentes, alcanceBocina, nChasis])
    puntajeMecanico.extend([manubrio, frenos, roturasFugasEscape, ruidoEscape, suspencion, funcionamientoSuspencion, chasis, cubiertas])
    puntajeConductor.extend([casco, ropa])
    
    comentarios = {
        "Exterior": comentariosUno,
        "Mecanica": comentariosDos,
        "Conductor": comentariosTres
        }
    
    return puntajeExterior, puntajeMecanico, puntajeConductor, comentarios

def verificar_camion(): #Proceso tecnico del camion
    puntajeInterior = []
    puntajeExterior = []
    puntajeMecanica = []
    print("Verificacion Interior") #Verificacion tecnica del interior
    puertas = verificar_puntaje("Cierre de las puertas: ")
    ventanillas = verificar_puntaje("Visibilidad de las ventanillas: ")
    parabrisas = verificar_puntaje("Visibilidad del parabrisas: ")
    cinturones = verificar_puntaje("Tension y anclaje del cinturon: ")
    asientos = verificar_puntaje("Anclaje de asientos: ")
    apoyaCabezas = verificar_puntaje("Anclaje de apoyacabezas: ")
    espejos = verificar_puntaje("Visibilidad de los espejos: ")
    bocina = verificar_puntaje("Comando de bocina: ")
    print("")
    comentariosUno = input("Comentarios: ")
    print("")
    print("Verificacion Exterior") #Verificacion tecnica del exterior 
    alineacionLuces = verificar_puntaje("Alineacion de luces de corto y largo alcance: ")
    intencidadLuces = verificar_puntaje("Intencidad de luces de corto y largo alcance: ")
    lucesPosicion = verificar_puntaje("Encendido de luces de posicion: ")
    lucesFreno = verificar_puntaje("Encendido de luces de Freno: ")
    lucesReversa = verificar_puntaje("Encendido de luces de Reversa: ")
    lucesIntermitentes = verificar_puntaje("Encendido de luces intermitentes: ")
    alcanceBocina = verificar_puntaje("Alcance de la Bocina: ")
    limpiaParabrisas = verificar_puntaje("Funcionamiento y estado de las escobillas: ")
    print("")
    comentariosDos = input("Comentarios: ")
    print("")
    print("Verificacion Mecanica") #Verificacion tecnica de mecanica
    alineacionEjeDelantero = verificar_puntaje("Alineacion del eje delantero: ")
    frenos = verificar_puntaje("Sistema de frenos: ")
    direccion = verificar_puntaje("Mecanismo de direccion: ")
    roturasFugasEscape = verificar_puntaje("Estado del sistema de escape: ")
    ruidoEscape = verificar_puntaje("Nivel de ruido del escape: ")
    suspencion = verificar_puntaje("Estado de la suspencion: ")
    funcionamientoSuspencion = verificar_puntaje("Funcionamiento de la suspencion: ")
    inferior = verificar_puntaje("Estado de la parte inferior: ")
    print("")
    comentariosTres = input("Comentarios: ")

    print("")

    puntajeInterior.extend([puertas, ventanillas, parabrisas, cinturones, asientos, apoyaCabezas, espejos, bocina])
    puntajeExterior.extend([alineacionLuces, intencidadLuces, lucesPosicion, lucesFreno, lucesReversa, lucesIntermitentes, alcanceBocina, limpiaParabrisas])
    puntajeMecanica.extend([alineacionEjeDelantero, frenos, direccion, roturasFugasEscape, ruidoEscape, suspencion, funcionamientoSuspencion, inferior])
    
    comentarios = {
        "Interior": comentariosUno,
        "Exterior": comentariosDos,
        "Mecanica": comentariosTres
        }
    
    return puntajeInterior, puntajeExterior, puntajeMecanica, comentarios


#PRINCIPAL
comentarios_totales = {}
tipoVehiculo = int(turno["Tipo"])
while tipoVehiculo != -1:
    tipoVehiculo = verificar_vehiculo(tipoVehiculo)
    incorrecto = 0
    regular = 0
    bien = 0
    if vehiculos[tipoVehiculo] == 'Auto':
        tipoVehiculo = -1
        puntajeInterior, puntajeExterior, puntajeMecanica, comentarios = verificacion_automovil()
        
        malInterior, regularInterior, bienInterior = contar_puntajes(puntajeInterior)
        malExterior, regularExterior, bienExterior = contar_puntajes(puntajeExterior)
        malMecanica, regularMecanica, bienMecanica = contar_puntajes(puntajeMecanica)
        
        incorrecto += malInterior + malExterior + malMecanica
        regular += regularInterior + regularExterior + regularMecanica
        bien += bienInterior + bienExterior + bienMecanica
        
        comentarios_totales["Auto"] = comentarios
    
    elif vehiculos[tipoVehiculo] == 'Moto':
        tipoVehiculo = -1
        puntajeExterior, puntajeMecanico, puntajeConductor, comentarios = verificacion_moto()
        
        malExterior, regularExterior, bienExterior = contar_puntajes(puntajeExterior)
        malMecanico, regularMecanico, bienMecanico = contar_puntajes(puntajeMecanico)
        malConductor, regularConductor, bienConductor = contar_puntajes(puntajeConductor)
        
        
        incorrecto += malExterior + malMecanico + malConductor
        regular += regularExterior + regularMecanico + regularConductor
        bien += bienExterior + bienMecanico + bienConductor
    
        comentarios_totales["Moto"] = comentarios
    
    else:
        tipoVehiculo = -1
        puntajeInterior, puntajeExterior, puntajeMecanica, comentarios = verificacion_automovil()
        
        malInterior, regularInterior, bienInterior = contar_puntajes(puntajeInterior)
        malExterior, regularExterior, bienExterior = contar_puntajes(puntajeExterior)
        malMecanica, regularMecanica, bienMecanica = contar_puntajes(puntajeMecanica)
        
        incorrecto += malInterior + malExterior + malMecanica
        regular += regularInterior + regularExterior + regularMecanica
        bien += bienInterior + bienExterior + bienMecanica
        
        comentarios_totales["Camion"] = comentarios
        
    if incorrecto > 0:
        turno["estado"] = "No Aprueba"
        for clave, valor in turno.items():
            print(f"{clave}: {valor}")
    elif regular > 12:
        turno["estado"] = "Provisoria"
        for clave, valor in turno.items():
            print(f"{clave}: {valor}")
    else:
        turno["estado"] = "Aprueba"
        for clave, valor in turno.items():
            print(f"{clave}: {valor}")
   
    print("Comentarios")
    for seccion, comentario in comentarios.items():
        print(f"{seccion}: {comentario}")
   
    

