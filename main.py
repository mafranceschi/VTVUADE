import tkinter as tk
from tkinter import ttk, messagebox
import json

# Lista para almacenar los registros de vehículos
vehiculos_registrados = []
montosTipo = [
    ['Auto', 45000, 45000 * 0.21, 45000 * 1.21],
    ['Moto', 26000, 26000 * 0.21, 26000 * 1.21],
    ['Camión', 79000, 79000 * 0.21, 79000 * 1.21]
]

# Función para cargar los vehículos desde un archivo JSON
def cargar_desde_json():
    global vehiculos_registrados
    try:
        with open('vehiculos_registrados.json', 'r') as file:
            vehiculos_registrados = json.load(file)
    except FileNotFoundError:
        vehiculos_registrados = []
    except json.JSONDecodeError:
        vehiculos_registrados = []
        print("Error al decodificar el archivo JSON. Se inicializará una lista vacía.")


def guardar_en_json(vehiculo):
    try:
        with open('vehiculos_registrados.json', 'r+') as file:
            # Intentar cargar el contenido existente
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
            # Añadir el nuevo vehículo
            data.append(vehiculo)
            # Volver al inicio del archivo y escribir los datos actualizados
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
    except FileNotFoundError:
        # Si el archivo no existe, créalo y escribe el primer vehículo
        with open('vehiculos_registrados.json', 'w') as file:
            json.dump([vehiculo], file, indent=4)

def obtener_reporte_tecnico(vehiculo, fallos):
    estado = "Aprobado" if len(fallos) == 0 else "Reprobado"
    reporte = {
        "vehiculo": vehiculo,
        "fallos": fallos,
        "estado": estado,
        "comentarios": {}  # Esto se llenará en calcular_resultado_y_reporte
    }
    return reporte

def imprimir_reporte(reporte):
    mensaje = f"Reporte Técnico para {reporte['vehiculo']['tipo']} - {reporte['vehiculo']['dominio']}\n\n"
    mensaje += f"Estado: {reporte['estado']}\n"
    mensaje += f"Cantidad de fallos detectados: {len(reporte['fallos'])}\n\n"
    
    mensaje += "Comentarios:\n"
    for seccion, comentario in reporte['comentarios'].items():
        mensaje += f"{seccion}: {comentario}\n"

    messagebox.showinfo("Reporte Técnico", mensaje)

def obtener_estado_vtv(reporte):
    cantidad_fallos = len(reporte['fallos'])
    if cantidad_fallos == 0:
        return "VTV aprobada"
    elif cantidad_fallos <= 3:
        return "VTV provisoria"
    else:
        return "VTV reprobada"

def generar_oblea_vtv(reporte):
    estado_vtv = obtener_estado_vtv(reporte)
    mensaje = f"Estado de VTV: {estado_vtv}\n"
    if estado_vtv == "VTV aprobada":
        mensaje += "Se ha emitido la oblea de la VTV vigente de este año."
    elif estado_vtv == "VTV provisoria":
        mensaje += "VTV provisoria sin oblea. Debe reparar los fallos reportados."
    elif estado_vtv == "VTV reprobada":
        mensaje += "VTV reprobada. Presenta fallos demasiado graves como para otorgarle una provisoria."
    messagebox.showinfo("Estado de VTV", mensaje)

# Función para calcular el resultado y generar el reporte técnico
def calcular_resultado_y_reporte(vehiculo, puntajes, comentarios, ventana_evaluacion):
    fallos = []
    secciones = {
        "Interior": [
            "Cierre de puertas", "Visibilidad de ventanillas", "Visibilidad del parabrisas",
            "Tensión y anclaje del cinturón", "Anclaje de asientos", "Anclaje de apoyacabezas",
            "Visibilidad de espejos", "Comando de bocina"
        ],
        "Exterior": [
            "Alineación de luces de corto y largo alcance", "Intensidad de luces de corto y largo alcance",
            "Encendido de luces de posición", "Encendido de luces de freno", "Encendido de luces de reversa",
            "Encendido de luces intermitentes", "Alcance de la bocina", "Funcionamiento de las escobillas"
        ],
        "Mecánica": [
            "Alineación del eje delantero", "Sistema de frenos", "Mecanismo de dirección", "Estado del sistema de escape",
            "Nivel de ruido del escape", "Estado de la suspensión", "Funcionamiento de la suspensión", "Estado de la parte inferior"
        ]
    }
    for seccion, spins in puntajes.items():
        for i, spin in enumerate(spins):
            try:
                valor = int(spin.get())
                if valor < 2:
                    fallos.append(f"{seccion} - {secciones[seccion][i]}: {valor}")
            except ValueError:
                messagebox.showerror("Error", f"Valor inválido en {seccion} - {secciones[seccion][i]}")
                return

    reporte = obtener_reporte_tecnico(vehiculo, fallos)

    # Agregar comentarios al reporte
    reporte["comentarios"] = {seccion: comentario.get() for seccion, comentario in comentarios.items()}

    imprimir_reporte(reporte)
    generar_oblea_vtv(reporte)

    # Actualizar el estado del vehículo
    for v in vehiculos_registrados:
        if v["dominio"] == vehiculo["dominio"]:
            v["estado"] = obtener_estado_vtv(reporte)
            break
    guardar_en_json(vehiculo)
    ventana_evaluacion.destroy()

def obtener_items_seccion(seccion):
    if seccion == "Interior":
        return ["Cierre de puertas", "Visibilidad de ventanillas", "Visibilidad del parabrisas",
            "Tensión y anclaje del cinturón", "Anclaje de asientos", "Anclaje de apoyacabezas",
            "Visibilidad de espejos", "Comando de bocina"]
    elif seccion == "Exterior":
        return ["Alineación de luces de corto y largo alcance", "Intensidad de luces de corto y largo alcance",
            "Encendido de luces de posición", "Encendido de luces de freno", "Encendido de luces de reversa",
            "Encendido de luces intermitentes", "Alcance de la bocina", "Funcionamiento de las escobillas"]
    elif seccion == "Mecánica":
        return ["Alineación del eje delantero", "Sistema de frenos", "Mecanismo de dirección", "Estado del sistema de escape",
            "Nivel de ruido del escape", "Estado de la suspensión", "Funcionamiento de la suspensión", "Estado de la parte inferior"]
    return []

# Ventana de evaluación técnica
def evaluar_automovil(vehiculo):
    ventana_evaluacion = tk.Toplevel()
    ventana_evaluacion.title(f"Evaluación Técnica - {vehiculo['tipo']}")
    ventana_evaluacion.geometry("600x700")

    # Crear un diccionario para almacenar las variables de los puntajes
    puntajes = {}
    
    # Función para aplicar el puntaje general a una sección
    def aplicar_puntaje_general(seccion):
        puntaje = puntaje_general_vars[seccion].get()
        if puntaje != "":
            for spinbox in puntajes[seccion]:
                spinbox.set(puntaje)

    notebook = ttk.Notebook(ventana_evaluacion)
    notebook.pack(fill="both", expand=True)

    puntajes = {"Interior": [], "Exterior": [], "Mecánica": []}

    comentarios = {"Interior": tk.StringVar(), "Exterior": tk.StringVar(), "Mecánica": tk.StringVar()}

    puntaje_general_vars = {}

    for seccion in ["Interior", "Exterior", "Mecánica"]:
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=seccion)

        # Crear un frame interno para centrar el contenido
        inner_frame = ttk.Frame(frame)
        inner_frame.pack(expand=True)

        # Agregar selector general para la sección
        ttk.Label(inner_frame, text=f"Puntaje general {seccion}:").grid(row=0, column=0, padx=5, pady=5)
        puntaje_general_vars[seccion] = tk.StringVar()
        ttk.Spinbox(inner_frame, from_=0, to=2, textvariable=puntaje_general_vars[seccion], width=5).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(inner_frame, text="Aplicar", command=lambda s=seccion: aplicar_puntaje_general(s)).grid(row=0, column=2, padx=5, pady=5)

        # Agregar campos de evaluación específicos para cada sección
        items = obtener_items_seccion(seccion)
        for i, item in enumerate(items):
            ttk.Label(inner_frame, text=item).grid(row=i+1, column=0, sticky='w', padx=5, pady=2)
            spinbox = ttk.Spinbox(inner_frame, from_=0, to=2, width=5)
            spinbox.grid(row=i+1, column=1, padx=5, pady=2)
            puntajes[seccion].append(spinbox)

        # Campo para comentarios de la sección
        ttk.Label(inner_frame, text=f"Comentarios {seccion}:").grid(row=len(items)+1, column=0, sticky='w', padx=5, pady=5)
        comentario_entry = ttk.Entry(inner_frame, textvariable=comentarios[seccion], width=30)
        comentario_entry.grid(row=len(items)+1, column=1, columnspan=2, padx=5, pady=5, sticky='w')

    ttk.Button(
        ventana_evaluacion,
        text="Finalizar Evaluación",
        command=lambda: calcular_resultado_y_reporte(vehiculo, puntajes, comentarios, ventana_evaluacion)
    ).pack(pady=20)

    
def evaluar_camion(vehiculo):
    ventana_evaluacion = tk.Toplevel()
    ventana_evaluacion.title(f"Evaluación Técnica - {vehiculo['tipo']}")
    ventana_evaluacion.geometry("600x700")

    # Crear un diccionario para almacenar las variables de los puntajes
    puntajes = {}
    
    # Función para aplicar el puntaje general a una sección
    def aplicar_puntaje_general(seccion):
        puntaje = puntaje_general_vars[seccion].get()
        if puntaje != "":
            for spinbox in puntajes[seccion]:
                spinbox.set(puntaje)

    notebook = ttk.Notebook(ventana_evaluacion)
    notebook.pack(fill="both", expand=True)
    # Definición de las secciones
    puntajes = {"Interior": [], "Exterior": [], "Mecánica": []}

    comentarios = {"Interior": tk.StringVar(), "Exterior": tk.StringVar(), "Mecánica": tk.StringVar()}

    puntaje_general_vars = {}

    for seccion in ["Interior", "Exterior", "Mecánica"]:
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=seccion)

        # Crear un frame interno para centrar el contenido
        inner_frame = ttk.Frame(frame)
        inner_frame.pack(expand=True)

        # Agregar selector general para la sección
        ttk.Label(inner_frame, text=f"Puntaje general {seccion}:").grid(row=0, column=0, padx=5, pady=5)
        puntaje_general_vars[seccion] = tk.StringVar()
        ttk.Spinbox(inner_frame, from_=0, to=2, textvariable=puntaje_general_vars[seccion], width=5).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(inner_frame, text="Aplicar", command=lambda s=seccion: aplicar_puntaje_general(s)).grid(row=0, column=2, padx=5, pady=5)

        # Agregar campos de evaluación específicos para cada sección
        items = obtener_items_seccion(seccion)
        for i, item in enumerate(items):
            ttk.Label(inner_frame, text=item).grid(row=i+1, column=0, sticky='w', padx=5, pady=2)
            spinbox = ttk.Spinbox(inner_frame, from_=0, to=2, width=5)
            spinbox.grid(row=i+1, column=1, padx=5, pady=2)
            puntajes[seccion].append(spinbox)

        # Campo para comentarios de la sección
        ttk.Label(inner_frame, text=f"Comentarios {seccion}:").grid(row=len(items)+1, column=0, sticky='w', padx=5, pady=5)
        comentario_entry = ttk.Entry(inner_frame, textvariable=comentarios[seccion], width=50)
        comentario_entry.grid(row=len(items)+1, column=0, columnspan=3, padx=5, pady=5)

    ttk.Button(
        ventana_evaluacion,
        text="Finalizar Evaluación",
        command=lambda: calcular_resultado_y_reporte(vehiculo, puntajes, comentarios, ventana_evaluacion)
    ).pack(pady=20)


def evaluar_moto(vehiculo):
    ventana_evaluacion = tk.Toplevel()
    ventana_evaluacion.title(f"Evaluación Técnica - {vehiculo['tipo']}")
    ventana_evaluacion.geometry("600x700")

    # Crear un diccionario para almacenar las variables de los puntajes
    puntajes = {}
    
    # Función para aplicar el puntaje general a una sección
    def aplicar_puntaje_general(seccion):
        puntaje = puntaje_general_vars[seccion].get()
        if puntaje != "":
            for spinbox in puntajes[seccion]:
                spinbox.set(puntaje)

    notebook = ttk.Notebook(ventana_evaluacion)
    notebook.pack(fill="both", expand=True)
    # Definición de las secciones

    puntajes = {"Interior": [], "Exterior": [], "Mecánica": []}

    comentarios = {"Interior": tk.StringVar(), "Exterior": tk.StringVar(), "Mecánica": tk.StringVar()}

    puntaje_general_vars = {}

    for seccion in ["Interior", "Exterior", "Mecánica"]:
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=seccion)

        # Crear un frame interno para centrar el contenido
        inner_frame = ttk.Frame(frame)
        inner_frame.pack(expand=True)

        # Agregar selector general para la sección
        ttk.Label(inner_frame, text=f"Puntaje general {seccion}:").grid(row=0, column=0, padx=5, pady=5)
        puntaje_general_vars[seccion] = tk.StringVar()
        ttk.Spinbox(inner_frame, from_=0, to=2, textvariable=puntaje_general_vars[seccion], width=5).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(inner_frame, text="Aplicar", command=lambda s=seccion: aplicar_puntaje_general(s)).grid(row=0, column=2, padx=5, pady=5)

        # Agregar campos de evaluación específicos para cada sección
        items = obtener_items_seccion(seccion)
        for i, item in enumerate(items):
            ttk.Label(inner_frame, text=item).grid(row=i+1, column=0, sticky='w', padx=5, pady=2)
            spinbox = ttk.Spinbox(inner_frame, from_=0, to=2, width=5)
            spinbox.grid(row=i+1, column=1, padx=5, pady=2)
            puntajes[seccion].append(spinbox)

        # Campo para comentarios de la sección
        ttk.Label(inner_frame, text=f"Comentarios {seccion}:").grid(row=len(items)+1, column=0, sticky='w', padx=5, pady=5)
        comentario_entry = ttk.Entry(inner_frame, textvariable=comentarios[seccion], width=50)
        comentario_entry.grid(row=len(items)+1, column=0, columnspan=3, padx=5, pady=5)

    ttk.Button(
        ventana_evaluacion,
        text="Finalizar Evaluación",
        command=lambda: calcular_resultado_y_reporte(vehiculo, puntajes, comentarios, ventana_evaluacion)
    ).pack(pady=20)
# Función para imprimir un vehículo en el formato solicitado
def impresion(vehiculo):
    return (f"\nResumen del turno solicitado:\n"
            f"Dominio del vehículo: {vehiculo['dominio']}\n"
            f"DNI del titular: {vehiculo['dni']}\n"
            f"Nombre del titular: {vehiculo['nombre']}\n"
            f"Modelo del vehículo: {vehiculo['modelo']}\n"
            f"Marca del vehículo: {vehiculo['marca']}\n"
            f"Año del vehículo: {vehiculo['año']}\n"
            f"El monto a abonar es: {vehiculo['monto']}\n"
            f"Estado: {vehiculo['estado']}\n")
    
def mostrar_historial(boton_historial):
    cargar_desde_json()  # Cargar los vehículos registrados del archivo JSON

    historial = "\nHistorial de Registros de Vehículos:\n"
    for vehiculo in vehiculos_registrados:
        historial += impresion(vehiculo) + "\n"  # Imprimir cada vehículo

    # Crear una nueva ventana para mostrar el historial
    ventana_historial = tk.Toplevel()
    ventana_historial.title("Historial de Vehículos")
    ventana_historial.geometry("600x400")

    # Crear un widget de texto con barra de desplazamiento
    text_widget = tk.Text(ventana_historial, wrap="word")
    scrollbar = ttk.Scrollbar(ventana_historial, command=text_widget.yview)
    text_widget.configure(yscrollcommand=scrollbar.set)

    # Insertar el historial en el widget de texto
    text_widget.insert("1.0", historial)
    text_widget.config(state="disabled")  # Hacer que el texto sea de solo lectura

    # Empaquetar el widget de texto y la barra de desplazamiento
    text_widget.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Deshabilitar el botón de historial
    boton_historial.config(state="disabled")

    # Función para habilitar el botón cuando se cierre la ventana de historial
    def habilitar_boton():
        boton_historial.config(state="normal")
        ventana_historial.destroy()

    ventana_historial.protocol("WM_DELETE_WINDOW", habilitar_boton)

def mover_a_siguiente(event, siguiente_widget):
    siguiente_widget.focus_set()
# Ventana principal para registrar vehículos
def crear_interfaz():
    ventana_principal = tk.Tk()
    ventana_principal.title("Registro de Vehículos para VTV")
    ventana_principal.geometry("400x500")

    campos = [
        ("Dominio:", 7),
        ("DNI:", 10),
        ("Nombre:", 50),
        ("Modelo:", 20),
        ("Marca:", 20),
        ("Año:", 4)
    ]
    entradas = {}
    for i, (texto, longitud) in enumerate(campos):
        tk.Label(ventana_principal, text=texto).grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entrada = tk.Entry(ventana_principal, width=30)
        entrada.grid(row=i, column=1, padx=10, pady=5)
        entrada.config(validate="key", validatecommand=(ventana_principal.register(lambda char, max_len=longitud: len(char) <= max_len), "%P"))
        entradas[texto[:-1].lower()] = entrada

    # Configurar los eventos de Return después de crear todas las entradas
    for i, (texto, _) in enumerate(campos[:-1]):
        entradas[texto[:-1].lower()].bind("<Return>", lambda event, next_widget=entradas[campos[i+1][0][:-1].lower()]: mover_a_siguiente(event, next_widget))
    tipo_vehiculo = tk.StringVar(value="Auto")
    tk.Label(ventana_principal, text="Tipo de Vehículo:").grid(row=len(campos), column=0, padx=10, pady=5, sticky="e")
    tk.OptionMenu(ventana_principal, tipo_vehiculo, "Auto", "Moto", "Camión").grid(row=len(campos), column=1, padx=10, pady=5, sticky="w")

    tk.Button(
        ventana_principal,
        text="Registrar Vehículo",
        command=lambda: registrar_vehiculo(
            entradas["dominio"],
            entradas["dni"],
            entradas["nombre"],
            entradas["marca"],
            entradas["modelo"],
            entradas["año"],
            tipo_vehiculo,
            ventana_principal
        ),
    ).grid(row=len(campos)+1, column=0, columnspan=2, pady=20)

    boton_historial = tk.Button(
        ventana_principal,
        text="Mostrar Historial",
        command=lambda: mostrar_historial(boton_historial)
    )
    boton_historial.grid(row=len(campos)+2, column=0, columnspan=2, pady=10)

    ventana_principal.mainloop()

def validacion_dominio(dominio):
    dominio = dominio.upper()
    letraPatenteCorta = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U")
    letraPatenteLarga = ("A","B","C","D","E")
    if len(dominio) == 6:
        primerasTres = dominio[:3]
        ultimasTres = dominio[-3:]
        if ultimasTres.isdigit() and primerasTres.isalpha():
            if dominio[0] in letraPatenteCorta:
                return True
    elif len(dominio) == 7 and dominio[0] in letraPatenteLarga:
        primerasDos = dominio[:2]
        segundasTres = dominio[2:5]
        ultimasDos = dominio[-2:]
        if primerasDos.isalpha() and segundasTres.isdigit() and ultimasDos.isalpha():
            return True 
    return False

# Función para registrar un vehículo
def registrar_vehiculo(dominio, dni, nombre, modelo, marca, año, tipo_vehiculo, ventana_principal):
    try:
        # Validar que todos los campos estén llenos
        if not all([dominio.get(), dni.get(), nombre.get(), modelo.get(), marca.get(), año.get(), tipo_vehiculo.get()]):
            raise ValueError("Todos los campos deben estar llenos")
        
        # Validar el dominio del vehículo
        if not validacion_dominio(dominio.get()):
            raise ValueError("Dominio del vehículo inválido. Debe tener un formato válido.")
        
        dni_value = int(dni.get())
        if dni_value < 15000000 or dni_value > 60000000:
            raise ValueError("Número de DNI inválido. Debe estar entre 15000000 y 60000000.")

        # Validar año del vehículo
        año_value = int(año.get())
        if año_value < 1910 or año_value > 2025:
            raise ValueError("Año del vehículo inválido. Debe estar entre 1910 y 2025.")

        # Buscar el monto correspondiente al tipo de vehículo
        monto_base, iva, monto_total = 0, 0, 0
        for fila in montosTipo:
            if fila[0] == tipo_vehiculo.get():
                monto_base, iva, monto_total = fila[1], fila[2], fila[3]
                break

        vehiculo = {
            "dominio": dominio.get(),
            "dni": dni_value,
            "nombre": nombre.get(),
            "modelo": modelo.get(),
            "marca": marca.get(),
            "año": año_value,
            "monto_base": monto_base,
            "iva": iva,
            "monto": monto_total,  # Cambiado de monto_total a monto para coincidir con impresion()
            "estado": "Pendiente",
            "tipo": tipo_vehiculo.get()
        }
        vehiculos_registrados.append(vehiculo)
        guardar_en_json(vehiculo)  # Guardar en JSON
        messagebox.showinfo("Registro exitoso", f"El vehículo ha sido registrado con éxito.\nMonto total a abonar: ${monto_total:.2f}")
        '''
        ventana_principal.destroy()  se busca cerrar ventana, esto geneaba la ventana en blanco de tk,
        luego se modificao para borrar la informacion de cada campo antes de volver a abrir una ventana nueva y el bug fue arreglado
        '''
        # Limpiar los campos después del registro exitoso
        for entry in ventana_principal.winfo_children():
            if isinstance(entry, tk.Entry):
                entry.delete(0, tk.END)
                
        if vehiculo["tipo"] == "Auto":
            evaluar_automovil(vehiculo)
        elif vehiculo["tipo"] == "Moto":
            evaluar_moto(vehiculo)
        elif vehiculo["tipo"] == "Camión":
            evaluar_camion(vehiculo)
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error inesperado: {str(e)}")

crear_interfaz()
