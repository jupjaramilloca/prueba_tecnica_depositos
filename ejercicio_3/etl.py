"""
Fecha: 2025-05-25
Autor: Juan Pablo Jaramillo
Descripción:
    Hereda de la clase base 'Step', lo que le permite aprovechar la gestión
    centralizada de configuración, rutas y ejecución de scripts SQL.
    
    Esta estructura modular facilita la incorporación de nuevos pasos ETL,
    haciendo que el proceso sea fácilmente escalable y mantenible.
    Además, permite integrar nuevos componentes como análisis avanzados,
    validaciones adicionales o modelos predictivos, ampliando las capacidades
    del flujo ETL sin afectar la arquitectura base.
"""

import os
from step import Step  # Clase base para pasos ETL que provee métodos comunes


## Solución ejercicio 3 punto 1

class Clientes_sin_duplicado(Step):
    def ejecutar(self):
        """
        Método principal que ejecuta el paso ETL.
        Ejecuta un script SQL que crea y llena la tabla clientes_sin_duplicados
        con registros únicos según reglas definidas.
        """
        # Construye la ruta completa al archivo SQL relativo a la ubicación estándar de scripts SQL
        path_sql = os.path.join(self.getSQLPath(), "01_clientes_sin_duplicados.sql")
        
        # Ejecuta el archivo SQL usando un método común heredado de Step
        self.executeFile(path_sql)

## Solución ejercicio 3 punto 2

class Transacciones_acumuladas(Step):
    def ejecutar(self):
        """
        Ejecuta el proceso de creación e inserción en la tabla 'transacciones_acumuladas'
        Esto permite automatizar la actualización de la tabla 'transacciones_acumuladas'
        con los datos agrupados y acumulados de la tabla original de transacciones

        """
        # Construye la ruta completa al archivo SQL relativo a la ubicación estándar de scripts SQL
        path_sql = os.path.join(self.getSQLPath(), "02_transacciones_acumuladas.sql")
        
        # Ejecuta el archivo SQL usando un método común heredado de Step
        self.executeFile(path_sql)
        
        
## Solución ejercicio 3 punto 3
        

class Resultado_agrupado(Step):
    def ejecutar(self):
        """
        Ejecuta el proceso de creación e inserción en la tabla 'transacciones_acumuladas'
        Esto permite automatizar la actualización de la tabla 'transacciones_acumuladas'
        con los datos agrupados y acumulados de la tabla original de transacciones

        """
        # Construye la ruta completa al archivo SQL relativo a la ubicación estándar de scripts SQL
        path_sql = os.path.join(self.getSQLPath(), "03_resultado_agrupado.sql")
        
        # Ejecuta el archivo SQL usando un método común heredado de Step
        self.executeFile(path_sql)
        
## Solución ejercicio 3 punto 4


class Resultado_agrupado_txt(Step):
    def ejecutar(self):
        """
        Ejecuta una consulta SQL y exporta el resultado como un archivo .txt separado por tabuladores.

        - SQL: 04_resultado_agrupado_df.sql
        - Salida: ruta definida en config['ruta_resultado']
        """
        path_sql = os.path.join(self.getSQLPath(), "04_resultado_agrupado_df.sql")
        path_df = self.config['ruta_resultado']
        print(path_df)
        df = self.getDF(path_sql)
        df.to_csv(path_df,sep='\t', index=False, encoding='utf-8')
        
        
        
