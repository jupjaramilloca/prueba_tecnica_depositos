-- ============================================================================
-- Fecha: 2025/05/25
-- Autor: Juan Pablo Jaramillo
-- Script: Crear e insertar en la tabla resultado_agrupado
-- Descripción: Este script realiza una consulta a la tabla resultado agrupado
-- para poder realizar una descarga en un df
-- Base de datos: SQLite
-- ============================================================================

select 
    num_doc,              -- Documento del cliente
    monto_promedio,       -- Promedio de monto por cliente
    f_vinc,               -- Fecha de vinculación
    cantidad_trx          -- Cantidad total de transacciones
from resultado_agrupado
