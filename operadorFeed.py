#FUNCIONES
from OperadorTeccnicoPRUEBA import turno, incorrecto, regular, bien

def obtener_reporte_tecnico():
    # Simulación obtención del reporte técnico como un diccionario
    reporte = {
        "programa": "Operador Tecnico",
        "Dominio": turno["dominio"],
        "vehiculo":  turno["modelo"],
        "diagnostico": turno["estado"],  # Puede ser "aprobado", "provisorio" o "no aprobado"
        "fallos": incorrecto
    }
    if reporte["fallos"] == 0:
        del reporte["fallos"]
    return reporte

def imprimir_reporte(reporte):
    print(f"\nReporte técnico: {reporte['programa']}")
    print(f"Dominio: {reporte['Dominio']}")
    print(f"Diagnóstico: {reporte['diagnostico']}")
    if "fallos" in reporte:
        print(f"Fallos: {reporte['fallos']}")
    else:
        print("No se encontraron fallos.")
        
def obtener_estado_vtv(reporte):
    # Determina estado de la VTV a partir del diagnóstico realizado
    diagnostico = reporte.get('diagnostico')
    
    if diagnostico == "Aprueba":
        return "VTV aprobada"
    elif diagnostico == "No Aprueba":
        return "VTV reprobada"
    elif diagnostico == "Provisoria":
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