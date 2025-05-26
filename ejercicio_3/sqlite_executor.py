"""
Fecha: 2025-05-25
Autor: Juan Pa (o tu nombre)
Descripción:
    Clase que encapsula la ejecución de sentencias SQL sobre una base de datos SQLite.
    Permite ejecutar queries, scripts desde archivos, ejecutar carpetas con múltiples scripts
    y obtener resultados en DataFrames de pandas.
    Maneja la conexión de forma segura y controla errores con logging.
"""

import sqlite3
import os
import pandas as pd
import logging

class SQLiteExecutor:
    def __init__(self, db_path: str):
        # Ruta absoluta al archivo de base de datos SQLite
        self.db_path = os.path.abspath(db_path)
        print("SQLiteExecutor usando base:", self.db_path)
        self.conn = None  # Inicialmente no hay conexión abierta

    def conectar(self):
        """
        Abre conexión a la base de datos SQLite.
        """
        try:
            self.conn = sqlite3.connect(self.db_path)
        except Exception as e:
            logging.error(f"Error al conectar con la base de datos: {e}")
            raise  # Re-lanzar excepción para manejo superior

    def cerrar(self):
        """
        Cierra la conexión si está abierta.
        """
        if self.conn:
            self.conn.close()
            self.conn = None

    def ejecutar_query(self, sql: str, params=None):
        """
        Ejecuta un query o script SQL.
        Si 'params' está definido, ejecuta con parámetros (query parametrizado).
        Si no, ejecuta el script completo.
        """
        try:
            self.conectar()
            cursor = self.conn.cursor()
            if params:
                cursor.execute(sql, params)
            else:
                cursor.executescript(sql)  # Ejecuta script con múltiples sentencias
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error al ejecutar query: {e}")
            raise
        finally:
            self.cerrar()

    def ejecutar_archivo(self, filepath: str):
        """
        Ejecuta el contenido SQL de un archivo.
        """
        try:
            if not os.path.exists(filepath):
                logging.error(f"El archivo SQL no existe: {filepath}")
                raise FileNotFoundError(f"No existe el archivo SQL: {filepath}")
            with open(filepath, "r", encoding="utf-8") as f:
                sql = f.read()
            self.ejecutar_query(sql)
        except Exception as e:
            logging.error(f"Error ejecutando archivo SQL {filepath}: {e}")
            raise

    def ejecutar_folder(self, folder: str):
        """
        Ejecuta todos los archivos .sql en una carpeta (incluyendo subcarpetas),
        ordenados alfabéticamente para controlar el orden de ejecución.
        """
        archivos_sql = sorted([
            os.path.join(dp, f)
            for dp, _, files in os.walk(folder)
            for f in files if f.endswith(".sql")
        ])
        for archivo in archivos_sql:
            self.ejecutar_archivo(archivo)

    def query_a_df(self, filepath: str) -> pd.DataFrame:
        """
        Ejecuta una consulta SQL desde archivo y devuelve el resultado como DataFrame de pandas.
        """
        try:
            if not os.path.exists(filepath):
                raise FileNotFoundError(f"Archivo SQL no encontrado: {filepath}")

            with open(filepath, "r", encoding="utf-8") as f:
                sql = f.read().strip()

            if not sql:
                raise ValueError("El archivo SQL está vacío.")

            self.conectar()

            if self.conn is None:
                raise ConnectionError("La conexión a la base de datos no fue establecida correctamente.")

            df = pd.read_sql_query(sql, self.conn)

            if df is None:
                raise ValueError("El resultado de la consulta fue None.")

            return df

        except Exception as e:
            logging.error(f"Error al convertir archivo SQL a DataFrame: {e}")
            raise

        finally:
            self.cerrar()
