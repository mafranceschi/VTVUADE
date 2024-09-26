#FUNCIONES


def obtener_reporte_tecnico():
    # Simulación obtención del reporte técnico como un diccionario
    return {
        "programa": "Operador Tecnico",
        "diagnostico": "no aprobado",  # Puede ser "aprobado", "provisorio" o "no aprobado"
        "fallos": ["frenos, espejos, luces de freno, suspension"]
    }

def imprimir_reporte(reporte):
    print(f"Reporte técnico: {reporte['programa']}")
    print(f"Diagnóstico: {reporte.get('diagnostico', 'No disponible')}")
    if "fallos" in reporte:
        print(f"Fallos: {', '.join(reporte['fallos'])}")
    else:
        print("No se encontraron fallos.")
        
def obtener_estado_vtv(reporte):
    # Determina estado de la VTV a partir del diagnóstico realizado
    diagnostico = reporte.get('diagnostico')
    
    if diagnostico == "aprobado":
        return "VTV aprobada"
    elif diagnostico == "no aprobado":
        return "VTV reprobada"
    elif diagnostico == "provisorio":
        return "VTV provisoria"

def generar_oblea_vtv(reporte):
    estado_vtv = obtener_estado_vtv(reporte)
    if estado_vtv == "VTV aprobada":
        print("Se imprime la oblea de la VTV vigente de este año.")
    elif estado_vtv == "VTV provisoria":
        print("VTV provisoria sin oblea. Debe reparar los fallos reportados.")
    elif estado_vtv == "VTV reprobada":
        print("VTV reprobada. Presenta fallos demasiado graves como para otorgarle una provisoria.")
        

# PRINCIPAL
reporte = obtener_reporte_tecnico()
imprimir_reporte(reporte)
generar_oblea_vtv(reporte)