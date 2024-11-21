import tkinter as tk
from tkinter import ttk, messagebox
import json

# Lista para almacenar los registros de vehículos
vehiculos_registrados = []

# Función para guardar los vehículos registrados en un archivo JSON
def guardar_en_json():
    with open("vehiculos_registrados.json", "w") as archivo:
        json.dump(vehiculos_registrados, archivo, indent=4)

# Función para cargar los vehículos desde un archivo JSON
def cargar_desde_json():
    global vehiculos_registrados
    try:
        with open("vehiculos_registrados.json", "r") as archivo:
            vehiculos_registrados = json.load(archivo)
    except FileNotFoundError:
        vehiculos_registrados = []

# FUNCIONES EXTERNAS
def obtener_reporte_tecnico(vehiculo, fallos):
    reporte = {
        "programa": "Operador Tecnico",
        "Dominio": vehiculo["dominio"],
        "vehiculo": vehiculo["modelo"],
        "diagnostico": vehiculo["estado"],  # Puede ser "Aprueba", "Provisoria" o "No Aprueba"
        "fallos": fallos,
    }
    if fallos == 0:
        del reporte["fallos"]
    return reporte

def imprimir_reporte(reporte):
    mensaje = f"\nReporte técnico: {reporte['programa']}\n"
    mensaje += f"Dominio: {reporte['Dominio']}\n"
    mensaje += f"Diagnóstico: {reporte['diagnostico']}\n"
    if "fallos" in reporte:
        mensaje += f"Fallos: {reporte['fallos']}\n"
    else:
        mensaje += "No se encontraron fallos.\n"
    messagebox.showinfo("Reporte Técnico", mensaje)  # Mostrar en GUI

def obtener_estado_vtv(reporte):
    diagnostico = reporte.get("diagnostico")
    if diagnostico == "Aprueba":
        return "VTV aprobada"
    elif diagnostico == "No Aprueba":
        return "VTV reprobada"
    elif diagnostico == "Provisoria":
        return "VTV provisoria"

def generar_oblea_vtv(reporte):
    estado_vtv = obtener_estado_vtv(reporte)
    mensaje = ""
    if estado_vtv == "VTV aprobada":
        mensaje = "Se imprime la oblea de la VTV vigente de este año."
    elif estado_vtv == "VTV provisoria":
        mensaje = "VTV provisoria sin oblea. Debe reparar los fallos reportados."
    elif estado_vtv == "VTV reprobada":
        mensaje = "VTV reprobada. Presenta fallos demasiado graves como para otorgarle una provisoria."
    messagebox.showinfo("Estado de VTV", mensaje)  # Mostrar en GUI

# Función para calcular el resultado y generar el reporte técnico
def calcular_resultado_y_reporte(vehiculo, puntajes, ventana_evaluacion):
    total_mal = 0
    total_regular = 0
    total_bien = 0

    # Calcular puntajes
    for seccion in puntajes:
        for spin in puntajes[seccion]:
            valor = int(spin.get())
            if valor == 0:
                total_mal += 1
            elif valor == 1:
                total_regular += 1
            else:
                total_bien += 1

    # Determinar estado del vehículo
    if total_mal > 0:
        vehiculo["estado"] = "No Aprueba"
    elif total_regular > 12:
        vehiculo["estado"] = "Provisoria"
    else:
        vehiculo["estado"] = "Aprueba"

    # Generar reporte técnico
    reporte = obtener_reporte_tecnico(vehiculo, total_mal)
    imprimir_reporte(reporte)
    generar_oblea_vtv(reporte)

    # Guardar cambios en el archivo JSON
    guardar_en_json()
    ventana_evaluacion.destroy()

# Ventana de evaluación técnica
def evaluar_automovil(vehiculo):
    ventana_evaluacion = tk.Toplevel()
    ventana_evaluacion.title(f"Evaluación Técnica - {vehiculo['tipo']}")
    ventana_evaluacion.geometry("600x700")

    notebook = ttk.Notebook(ventana_evaluacion)
    notebook.pack(fill="both", expand=True)

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

    puntajes = {"Interior": [], "Exterior": [], "Mecánica": []}

    for seccion, criterios in secciones.items():
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=seccion)
        tk.Label(frame, text=f"Verificación {seccion}", font=("Arial", 14)).pack(pady=10)
        for criterio in criterios:
            tk.Label(frame, text=criterio).pack()
            spin = tk.Spinbox(frame, from_=0, to=2, width=5)
            spin.pack()
            puntajes[seccion].append(spin)

    tk.Button(
        ventana_evaluacion,
        text="Calcular Resultado",
        command=lambda: calcular_resultado_y_reporte(vehiculo, puntajes, ventana_evaluacion),
    ).pack(pady=20)
    
def evaluar_camion(vehiculo):
    ventana_evaluacion = tk.Toplevel()
    ventana_evaluacion.title(f"Evaluación Técnica - {vehiculo['tipo']}")
    ventana_evaluacion.geometry("600x700")

    notebook = ttk.Notebook(ventana_evaluacion)
    notebook.pack(fill="both", expand=True)

    # Definición de las secciones
    secciones = {
        "Interior": [
            "Cierre de puertas", "Visibilidad de ventanillas", "Tensión y anclaje de cinturones",
            "Anclaje de asientos", "Anclaje de apoyacabezas", "Visibilidad de espejos", "Comando de bocina"
        ],
        "Exterior": [
            "Alineación de luces", "Intensidad de luces", "Encendido de luces de posición",
            "Encendido de luces de freno", "Encendido de luces de reversa", "Encendido de luces intermitentes",
            "Estado de las escobillas", "Visibilidad de parabrisas"
        ],
        "Mecánica": [
            "Alineación del eje delantero", "Sistema de frenos", "Mecanismo de dirección",
            "Estado del sistema de escape", "Nivel de ruido del escape", "Estado de la suspensión",
            "Funcionamiento de la suspensión", "Estado de la parte inferior"
        ]
    }

    puntajes = {"Interior": [], "Exterior": [], "Mecánica": []}

    for seccion, criterios in secciones.items():
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=seccion)
        tk.Label(frame, text=f"Verificación {seccion}", font=("Arial", 14)).pack(pady=10)
        for criterio in criterios:
            tk.Label(frame, text=criterio).pack()
            spin = tk.Spinbox(frame, from_=0, to=2, width=5)
            spin.pack()
            puntajes[seccion].append(spin)

    tk.Button(
        ventana_evaluacion,
        text="Calcular Resultado",
        command=lambda: calcular_resultado_y_reporte(vehiculo, puntajes, ventana_evaluacion),
    ).pack(pady=20)


def evaluar_moto(vehiculo):
    ventana_evaluacion = tk.Toplevel()
    ventana_evaluacion.title(f"Evaluación Técnica - {vehiculo['tipo']}")
    ventana_evaluacion.geometry("600x700")

    notebook = ttk.Notebook(ventana_evaluacion)
    notebook.pack(fill="both", expand=True)

    # Definición de las secciones
    secciones = {
        "Exterior": [
            "Alineación de luces", "Intensidad de luces", "Encendido de luces de posición",
            "Encendido de luces de freno", "Encendido de luces intermitentes", "Estado del chasis",
            "Estado de las cubiertas"
        ],
        "Mecánica": [
            "Alineación del manubrio", "Sistema de frenos", "Estado del sistema de escape",
            "Nivel de ruido del escape", "Estado de la suspensión", "Funcionamiento de la suspensión"
        ],
        "Conductor": [
            "Estado general del casco", "Estado general de ropa protectora"
        ]
    }

    puntajes = {"Exterior": [], "Mecánica": [], "Conductor": []}

    for seccion, criterios in secciones.items():
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=seccion)
        tk.Label(frame, text=f"Verificación {seccion}", font=("Arial", 14)).pack(pady=10)
        for criterio in criterios:
            tk.Label(frame, text=criterio).pack()
            spin = tk.Spinbox(frame, from_=0, to=2, width=5)
            spin.pack()
            puntajes[seccion].append(spin)

    tk.Button(
        ventana_evaluacion,
        text="Calcular Resultado",
        command=lambda: calcular_resultado_y_reporte(vehiculo, puntajes, ventana_evaluacion),
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
    
def mostrar_historial():
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

def mover_a_siguiente(event, siguiente_widget):
    siguiente_widget.focus_set()
# Ventana principal para registrar vehículos
def crear_interfaz():
    cargar_desde_json()  # Cargar datos guardados previamente

    ventana = tk.Tk()
    ventana.title("Registro de Vehículos")
    ventana.geometry("500x600")

    tk.Label(ventana, text="Tipo de vehículo:").pack(pady=5)
    tipo_vehiculo = ttk.Combobox(ventana, values=["Auto", "Moto", "Camión"])
    tipo_vehiculo.pack()
    
    tk.Label(ventana, text="Dominio:").pack(pady=5)
    dominio = tk.Entry(ventana)
    dominio.pack()

    tk.Label(ventana, text="DNI:").pack(pady=5)
    dni = tk.Entry(ventana)
    dni.pack()

    tk.Label(ventana, text="Nombre del titular:").pack(pady=5)
    nombre = tk.Entry(ventana)
    nombre.pack()

    tk.Label(ventana, text="Modelo:").pack(pady=5)
    modelo = tk.Entry(ventana)
    modelo.pack()

    tk.Label(ventana, text="Marca:").pack(pady=5)
    marca = tk.Entry(ventana)
    marca.pack()

    tk.Label(ventana, text="Año:").pack(pady=5)
    año = tk.Entry(ventana)
    año.pack()

    tk.Label(ventana, text="Monto a abonar:").pack(pady=5)
    monto = tk.Entry(ventana)
    monto.pack()
    
     # Asociamos la tecla Enter con el siguiente campo
    dominio.bind("<Return>", lambda event: mover_a_siguiente(event, dni))
    dni.bind("<Return>", lambda event: mover_a_siguiente(event, nombre))
    nombre.bind("<Return>", lambda event: mover_a_siguiente(event, modelo))
    modelo.bind("<Return>", lambda event: mover_a_siguiente(event, marca))
    marca.bind("<Return>", lambda event: mover_a_siguiente(event, año))
    año.bind("<Return>", lambda event: mover_a_siguiente(event, monto))
    monto.bind("<Return>", lambda event: mover_a_siguiente(event, tipo_vehiculo))
    tipo_vehiculo.bind("<Return>", lambda event: registrar_vehiculo(dominio, dni, nombre, modelo, marca, año, monto, tipo_vehiculo, ventana))

    tk.Button(
        ventana,
        text="Registrar Vehículo",
        command=lambda: registrar_vehiculo(dominio, dni, nombre, modelo, marca, año, monto, tipo_vehiculo, ventana),
    ).pack(pady=10)
    
    tk.Button(
        ventana,
        text="Ver Historial",
        command=mostrar_historial
    ).pack(pady=10)

    ventana.mainloop()

    ventana.mainloop()

# Función para registrar un vehículo
def registrar_vehiculo(dominio, dni, nombre, modelo, marca, año, monto, tipo_vehiculo, ventana_principal):
    try:
        vehiculo = {
            "dominio": dominio.get(),
            "dni": int(dni.get()),
            "nombre": nombre.get(),
            "modelo": modelo.get(),
            "marca": marca.get(),
            "año": int(año.get()),
            "monto": float(monto.get()),
            "estado": "Pendiente",
            "tipo": tipo_vehiculo.get()
        }
        vehiculos_registrados.append(vehiculo)
        guardar_en_json()  # Guardar en JSON
        messagebox.showinfo("Registro exitoso", "El vehículo ha sido registrado con éxito.")
        ventana_principal.destroy()
        if vehiculo["tipo"] == "Auto":
            evaluar_automovil(vehiculo)
        elif vehiculo["tipo"] == "Moto":
            evaluar_moto(vehiculo)
        elif vehiculo["tipo"] == "Camión":
            evaluar_camion(vehiculo)
    except ValueError:
        messagebox.showerror("Error", "Verifique que todos los campos estén correctamente llenados.")


crear_interfaz()
