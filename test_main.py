import unittest
from unittest.mock import patch, MagicMock
from main import (cargar_desde_json, guardar_en_json, obtener_reporte_tecnico,
                  obtener_estado_vtv, calcular_resultado_y_reporte)
import json
import os

class TestVTVUADE(unittest.TestCase):

    def setUp(self):
        # Configuración inicial para las pruebas
        self.vehiculo_prueba = {
            "dominio": "ABC123",
            "dni": "12345678",
            "nombre": "Juan Perez",
            "modelo": "Corolla",
            "marca": "Toyota",
            "año": 2020,
            "monto": 54450.0,
            "estado": "Pendiente",
            "tipo": "Auto"
        }

    @patch('main.open', new_callable=unittest.mock.mock_open, read_data='[{"dominio": "ABC123"}]')
    def test_cargar_desde_json(self, mock_file):
        resultado = cargar_desde_json()
        self.assertEqual(resultado, [{"dominio": "ABC123"}])

    @patch('main.open', new_callable=unittest.mock.mock_open)
    @patch('json.dump')
    def test_guardar_en_json(self, mock_json_dump, mock_file):
        guardar_en_json(self.vehiculo_prueba)
        mock_json_dump.assert_called_once()

    def test_obtener_reporte_tecnico(self):
        fallos = ["Fallo 1", "Fallo 2"]
        reporte = obtener_reporte_tecnico(self.vehiculo_prueba, fallos)
        self.assertEqual(reporte['vehiculo'], self.vehiculo_prueba)
        self.assertEqual(reporte['fallos'], fallos)
        self.assertEqual(reporte['estado'], "Reprobado")

    def test_obtener_estado_vtv(self):
        reporte_sin_fallos = {'fallos': []}
        self.assertEqual(obtener_estado_vtv(reporte_sin_fallos), "VTV aprobada")

        reporte_con_pocos_fallos = {'fallos': ["Fallo 1", "Fallo 2"]}
        self.assertEqual(obtener_estado_vtv(reporte_con_pocos_fallos), "VTV provisoria")

        reporte_con_muchos_fallos = {'fallos': ["Fallo 1", "Fallo 2", "Fallo 3", "Fallo 4"]}
        self.assertEqual(obtener_estado_vtv(reporte_con_muchos_fallos), "VTV reprobada")

    @patch('main.imprimir_reporte')
    @patch('main.generar_oblea_vtv')
    @patch('main.crear_oblea_pdf')
    def test_calcular_resultado_y_reporte(self, mock_crear_oblea, mock_generar_oblea, mock_imprimir):
        puntajes = {
            "Interior": [MagicMock(get=lambda: "2") for _ in range(8)],
            "Exterior": [MagicMock(get=lambda: "2") for _ in range(8)],
            "Mecánica": [MagicMock(get=lambda: "2") for _ in range(8)]
        }
        comentarios = {
            "Interior": MagicMock(get=lambda: "Comentario interior"),
            "Exterior": MagicMock(get=lambda: "Comentario exterior"),
            "Mecánica": MagicMock(get=lambda: "Comentario mecánica")
        }
        ventana_evaluacion = MagicMock()

        calcular_resultado_y_reporte(self.vehiculo_prueba, puntajes, comentarios, ventana_evaluacion)

        mock_imprimir.assert_called()
        mock_generar_oblea.assert_called()
        mock_crear_oblea.assert_called()
        ventana_evaluacion.destroy.assert_called()

if __name__ == '__main__':
    unittest.main()