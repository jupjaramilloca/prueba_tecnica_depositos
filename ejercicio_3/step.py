"""
Fecha: 2025-05-25
Autor: Juan Pablo Jaramillo
Descripción:
    Clase base 'Step' que actúa como plantilla fundamental para la creación de
    pasos modulares dentro de procesos ETL (Extracción, Transformación y Carga).
    Gestiona la configuración centralizada, rutas absolutas para recursos clave
    (base de datos SQLite, scripts SQL y archivos de log) y facilita la ejecución
    controlada y segura de scripts SQL a través del componente 'SQLiteExecutor'.

    Este diseño modular permite construir pipelines escalables y mantenibles,
    donde cada paso puede representar una tarea específica (limpieza de datos,
    transformación, carga, etc.). Además, la estructura es flexible para integrar
    componentes avanzados, como modelos analíticos, validaciones o procesos
    complementarios dentro del mismo framework ETL, promoviendo así un desarrollo
    robusto y extensible.

    En resumen, esta clase base no solo soporta operaciones tradicionales de
    bases de datos, sino que habilita un ecosistema para crecimiento e innovación
    en la orquestación de flujos de datos complejos.
"""

import os
import json
import logging
from sqlite_executor import SQLiteExecutor  # Componente para ejecución SQL en SQLite

class Step:
    def __init__(self, config_path=None):
        # Obtiene la ruta absoluta del directorio actual (donde está este archivo)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Si no se pasa ruta de configuración, utiliza config.json dentro del mismo directorio
        if config_path is None:
            config_path = os.path.join(current_dir, "config.json")
        
        # Carga la configuración desde el archivo JSON
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)

        # Ajusta rutas absolutas para base de datos, SQL y logs, garantizando portabilidad
        self.config["db_path"] = os.path.join(current_dir, self.config["db_path"])
        self.config["sql_path"] = os.path.join(current_dir, self.config.get("sql_path", "sql"))
        self.config["log_path"] = os.path.join(current_dir, self.config.get("log_path", "logs"))

        # Instancia el ejecutor SQLite para manejar consultas y scripts SQL
        self.executor = SQLiteExecutor(self.config["db_path"])

    def getSQLPath(self):
        """
        Retorna la ruta absoluta donde se encuentran los scripts SQL.
        """
        return self.config["sql_path"]

    def getLogPath(self):
        """
        Retorna la ruta absoluta donde se guardan los archivos de log.
        """
        return self.config["log_path"]

    def executeFolder(self, folder):
        """
        Ejecuta todos los archivos SQL dentro de la carpeta especificada,
        permitiendo ejecutar procesos completos o batchs de scripts de forma ordenada.
        """
        logging.info(f"Ejecutando SQL desde carpeta: {folder}")
        self.executor.ejecutar_folder(folder)

    def executeFile(self, filepath):
        """
        Ejecuta un archivo SQL específico, útil para tareas puntuales dentro del flujo.
        """
        logging.info(f"Ejecutando SQL desde archivo: {filepath}")
        self.executor.ejecutar_archivo(filepath)

    def getDF(self, filepath):
        """
        Ejecuta una consulta SQL y retorna el resultado como un DataFrame de pandas,
        facilitando la integración con componentes analíticos o de machine learning.
        """
        logging.info(f"Descargando resultado de query a DataFrame desde: {filepath}")
        return self.executor.query_a_df(filepath)
