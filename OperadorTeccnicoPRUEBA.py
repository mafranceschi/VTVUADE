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
    

def verificacion_automovil(): #Proceso tecnico del auto
    puntajeInterior = []
    puntajeExterior = []
    puntajeMecanica = []
    print("\nVerificacion Interior") #Verificacion tecnica del interior
    puertas = int(input("Cierre de las puertas: "))
    ventanillas = int(input("Visibilidad de las ventanillas: "))
    parabrisas = int(input("Visibilidad del parabrisas: "))
    cinturones = int(input("Tension y anclaje del cinturon: "))
    asientos = int(input("Anclaje de asientos: "))
    apoyaCabezas = int(input("Anclaje de apoyacabezas: "))
    espejos = int(input("Visibilidad de los espejos: "))
    bocina = int(input("Comando de bocina: "))
    comentariosUno = input("Comentarios: ")
    print("Verificacion Exterior") #Verificacion tecnica del exterior 
    alineacionLuces = int(input("Alineacion de luces de corto y largo alcance: "))
    intencidadLuces = int(input("Intencidad de luces de corto y largo alcance: "))
    lucesPosicion = int(input("Encendido de luces de posicion: "))
    lucesFreno = int(input("Encendido de luces de Freno: "))
    lucesReversa = int(input("Encendido de luces de Reversa: "))
    lucesIntermitentes = int(input("Encendido de luces intermitentes: "))
    alcanceBocina = int(input("Alcance de la Bocina: "))
    limpiaParabrisas = int(input("Funcionamiento y estado de las escobillas: "))
    comentariosDos = input("Comentarios: ")
    print("Verificacion Mecanica") #Verificacion tecnica de mecanica
    alineacionEjeDelantero = int(input("Alineacion del eje delantero: "))
    frenos = int(input("Sistema de frenos: "))
    direccion = int(input("Mecanismo de direccion: "))
    roturasFugasEscape = int(input("Estado del sistema de escape: "))
    ruidoEscape = int(input("Nivel de ruido del escape: "))
    suspencion = int(input("Estado de la suspencion: "))
    funcionamientoSuspencion = int(input("Funcionamiento de la suspencion: "))
    inferior = int(input("Estado de la parte inferior: "))
    comentariosTres = input("Comentarios: ")
    puntajeInterior.extend([puertas, ventanillas, parabrisas, cinturones, asientos, apoyaCabezas, espejos, bocina])
    puntajeExterior.extend([alineacionLuces, intencidadLuces, lucesPosicion, lucesFreno, lucesReversa, lucesIntermitentes, alcanceBocina, limpiaParabrisas])
    puntajeMecanica.extend([alineacionEjeDelantero, frenos, direccion, roturasFugasEscape, ruidoEscape, suspencion, funcionamientoSuspencion, inferior])
    return puntajeInterior, puntajeExterior, puntajeMecanica

def verificacion_moto(): #Proceso tecnico de la moto
    puntajeExterior = []
    puntajeMecanico = []
    puntajeConductor = []
    print("Verificacion exterior")
    alineacionLuces = int(input("Alineacion de luces de corto y largo alcance: "))
    intencidadLuces = int(input("Intencidad de luces de corto y largo alcance: "))
    lucesPosicion = int(input("Encendido de luces de posicion: "))
    lucesFreno = int(input("Encendido de luces de Freno: "))
    lucesIntermitentes = int(input("Encendido de luces intermitentes: "))
    alcanceBocina = int(input("Alcance de la Bocina: "))
    nChasis = int(input("Numero de chasis legible: "))
    comentariosUno = input("Comentarios: ")
    print("Verificacion Mecanica")
    manubrio = int(input("Alineacion y estado del manubrio: "))
    frenos = int(input("Sistema de frenos: "))
    roturasFugasEscape = int(input("Estado del sistema de escape: "))
    ruidoEscape = int(input("Nivel de ruido del escape: "))
    suspencion = int(input("Estado de la suspencion: "))
    funcionamientoSuspencion = int(input("Funcionamiento de la suspencion: "))
    chasis = int(input("Estado del chasis"))
    cubiertas = int(input("Estado de las cubiertas: "))
    comentariosDos = input("Comentarios: ")
    print("Verificacion Conductor")
    casco = int(input("Estado general del casco: "))
    ropa = int(input("Estado general de ropa protectora: "))
    comentariosTres = input("Comentarios: ")
    puntajeExterior.extend([alineacionLuces, intencidadLuces, lucesPosicion, lucesFreno, lucesIntermitentes, alcanceBocina, nChasis])
    puntajeMecanico.extend([manubrio, frenos, roturasFugasEscape, ruidoEscape, suspencion, funcionamientoSuspencion, chasis, cubiertas])
    puntajeConductor.extend([casco, ropa])
    return puntajeExterior, puntajeMecanico, puntajeConductor

def verificar_camion(): #Proceso tecnico del camion
    puntajeInterior = []
    puntajeExterior = []
    puntajeMecanica = []
    print("Verificacion Interior") #Verificacion tecnica del interior
    puertas = int(input("Cierre de las puertas: "))
    ventanillas = int(input("Visibilidad de las ventanillas: "))
    parabrisas = int(input("Visibilidad del parabrisas: "))
    cinturones = int(input("Tension y anclaje del cinturon: "))
    asientos = int(input("Anclaje de asientos: "))
    apoyaCabezas = int(input("Anclaje de apoyacabezas: "))
    espejos = int(input("Visibilidad de los espejos: "))
    bocina = int(input("Comando de bocina: "))
    comentariosUno = input("Comentarios: ")
    print("Verificacion Exterior") #Verificacion tecnica del exterior 
    alineacionLuces = int(input("Alineacion de luces de corto y largo alcance: "))
    intencidadLuces = int(input("Intencidad de luces de corto y largo alcance: "))
    lucesPosicion = int(input("Encendido de luces de posicion: "))
    lucesFreno = int(input("Encendido de luces de Freno: "))
    lucesReversa = int(input("Encendido de luces de Reversa: "))
    lucesIntermitentes = int(input("Encendido de luces intermitentes: "))
    alcanceBocina = int(input("Alcance de la Bocina: "))
    limpiaParabrisas = int(input("Funcionamiento y estado de las escobillas: "))
    comentariosDos = input("Comentarios: ")
    print("Verificacion Mecanica") #Verificacion tecnica de mecanica
    alineacionEjeDelantero = int(input("Alineacion del eje delantero: "))
    frenos = int(input("Sistema de frenos: "))
    direccion = int(input("Mecanismo de direccion: "))
    roturasFugasEscape = int(input("Estado del sistema de escape: "))
    ruidoEscape = int(input("Nivel de ruido del escape: "))
    suspencion = int(input("Estado de la suspencion: "))
    funcionamientoSuspencion = int(input("Funcionamiento de la suspencion: "))
    inferior = int(input("Estado de la parte inferior: "))
    comentariosTres = input("Comentarios: ")
    puntajeInterior.extend([puertas, ventanillas, parabrisas, cinturones, asientos, apoyaCabezas, espejos, bocina])
    puntajeExterior.extend([alineacionLuces, intencidadLuces, lucesPosicion, lucesFreno, lucesReversa, lucesIntermitentes, alcanceBocina, limpiaParabrisas])
    puntajeMecanica.extend([alineacionEjeDelantero, frenos, direccion, roturasFugasEscape, ruidoEscape, suspencion, funcionamientoSuspencion, inferior])
    return puntajeInterior, puntajeExterior, puntajeMecanica


#PRINCIPAL
tipoVehiculo = int(turno["Tipo"])
while tipoVehiculo != -1:
    tipoVehiculo = verificar_vehiculo(tipoVehiculo)
    incorrecto = 0
    regular = 0
    bien = 0
    if vehiculos[tipoVehiculo] == 'Auto':
        tipoVehiculo = -1
        puntajeInterior, puntajeExterior, puntajeMecanica = verificacion_automovil()
        
        malInterior, regularInterior, bienInterior = contar_puntajes(puntajeInterior)
        malExterior, regularExterior, bienExterior = contar_puntajes(puntajeExterior)
        malMecanica, regularMecanica, bienMecanica = contar_puntajes(puntajeMecanica)
        
        incorrecto += malInterior + malExterior + malMecanica
        regular += regularInterior + regularExterior + regularMecanica
        bien += bienInterior + bienExterior + bienMecanica
    
    elif vehiculos[tipoVehiculo] == 'Moto':
        tipoVehiculo = -1
        puntajeExterior, puntajeMecanico, puntajeConductor = verificacion_moto()
        
        malExterior, regularExterior, bienExterior = contar_puntajes(puntajeExterior)
        malMecanico, regularMecanico, bienMecanico = contar_puntajes(puntajeMecanico)
        malConductor, regularConductor, bienConductor = contar_puntajes(puntajeConductor)
        
        
        incorrecto += malExterior + malMecanico + malConductor
        regular += regularExterior + regularMecanico + regularConductor
        bien += bienExterior + bienMecanico + bienConductor
    
    else:
        tipoVehiculo = -1
        puntajeInterior, puntajeExterior, puntajeMecanica = verificacion_automovil()
        
        malInterior, regularInterior, bienInterior = contar_puntajes(puntajeInterior)
        malExterior, regularExterior, bienExterior = contar_puntajes(puntajeExterior)
        malMecanica, regularMecanica, bienMecanica = contar_puntajes(puntajeMecanica)
        
        incorrecto += malInterior + malExterior + malMecanica
        regular += regularInterior + regularExterior + regularMecanica
        bien += bienInterior + bienExterior + bienMecanica
        
        
    if incorrecto > 0:
        print("\nNO APROBADO: ",turno)
    elif regular > 12:
        print("\nPROVISORIO: ",turno)
    else:
        print("\nAPROBADO:")
        for clave, valor in turno.items():
            print(f"{clave}: {valor}")
   
    
   
    

