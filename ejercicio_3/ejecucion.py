"""
Fecha: 2025-05-25
Autor: Juan Pablo Jaramillo
Descripción:
    Script para orquestar la ejecución de procesos ETL definidos en pasos (steps).
    Carga configuración desde un archivo JSON, configura logging y ejecuta cada paso, 
    manejando errores y registrando logs de inicio y fin de cada paso.
"""

import os             # Para manipulación de rutas y directorios
import json           # Para cargar configuración desde archivo JSON
import logging        # Para registro de logs de ejecución
from datetime import datetime  # Para manejar fechas y horas
from etl import Clientes_sin_duplicado,Transacciones_acumuladas,Resultado_agrupado,Resultado_agrupado_txt  # Importa la clase de proceso ETL específico

class RunOrquestador:
    def __init__(self):
        # Construye la ruta del archivo config.json en el mismo directorio del script
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        # Abre y carga el archivo de configuración JSON en un diccionario
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)
        # Define la lista de pasos (steps) a ejecutar; actualmente solo un paso Clientes_sin_duplicado
        
        self.steps = [
            Clientes_sin_duplicado(), # -> Solución ejercicio 3 punto 1
            Transacciones_acumuladas(), # -> Solución ejercicio 3 punto 2
            Resultado_agrupado(), # -> Solución ejercicio 3 punto 3
            Resultado_agrupado_txt()
            
        ]

    def run(self):
        # Registra el momento de inicio de la ejecución
        start = datetime.now()
        # Obtiene la ruta para logs desde la configuración o usa 'logs' por defecto
        log_path = self.config.get("log_path", "logs")
        # Crea el directorio para logs si no existe
        os.makedirs(log_path, exist_ok=True)
        # Configura el sistema de logging para guardar logs en archivo y mostrar en consola
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                # Archivo de log con timestamp en el nombre para cada ejecución
                logging.FileHandler(os.path.join(log_path, f"ejecucion_{start.strftime('%Y%m%d_%H%M%S')}.log"), encoding="utf-8"),
                # Log en consola (stdout)
                logging.StreamHandler()
            ]
        )
        try:
            # Ejecuta secuencialmente cada paso definido
            for step in self.steps:
                logging.info(f"Iniciando: {step.__class__.__name__}")  # Log de inicio del paso
                step.ejecutar()  # Método principal del paso que realiza la lógica ETL
                logging.info(f"Finalizado: {step.__class__.__name__}") # Log de finalización del paso
        except Exception as e:
            # Captura cualquier error que ocurra y lo registra en el log con traceback
            logging.exception(f"Error en ejecución del orquestador: {e}")
        finally:
            # Log que indica que la ejecución completa (con éxito o error) finalizó
            logging.info("Ejecución completada.")

def main():
    # Función principal que inicia el orquestador
    RunOrquestador().run()

# Punto de entrada principal del script
if __name__ == "__main__":
    main()
