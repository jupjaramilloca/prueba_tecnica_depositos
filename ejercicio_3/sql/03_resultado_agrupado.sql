-- ============================================================================
-- Fecha: 2025/05/25
-- Autor: Juan Pablo Jaramillo
-- Script: Crear e insertar en la tabla resultado_agrupado
-- Descripción: Este script crea una tabla con el promedio del monto de las
--              transacciones agrupadas por número de documento del cliente,
--              filtrando solo aquellos cuyo promedio supera los 150,000. 
--              Incluye además la fecha de vinculación más antigua del cliente
--              y la cantidad total de transacciones asociadas.
-- Base de datos: SQLite
-- ============================================================================

-- Elimina la tabla resultado_agrupado si existe para evitar errores al crearla nuevamente
DROP TABLE IF EXISTS resultado_agrupado;

-- Crear tabla resultado_agrupado con estructura adecuada
CREATE TABLE resultado_agrupado (
    num_doc         TEXT,   -- Número de documento del cliente
    monto_promedio  REAL,   -- Promedio del monto de transacciones (por cliente)
    f_vinc          TEXT,   -- Fecha de vinculación más antigua del cliente
    cantidad_trx    INTEGER -- Total de transacciones asociadas al cliente
);

-- Insertar datos agrupados y filtrados desde la tabla de transacciones y clientes
INSERT INTO resultado_agrupado (
    num_doc,              -- Documento del cliente
    monto_promedio,       -- Promedio de monto por cliente
    f_vinc,               -- Fecha de vinculación
    cantidad_trx          -- Cantidad total de transacciones
)
SELECT
    c.num_doc,                                      -- Documento del cliente
    ROUND(AVG(t.mnt_trn), 2) AS monto_promedio,     -- Promedio del monto redondeado
    MIN(c.f_vinc) AS f_vinc,                        -- Fecha más antigua de vinculación
    COUNT(t.mnt_trn) AS cantidad_trx                -- Cantidad de transacciones válidas
FROM transacciones t
JOIN clientes_sin_duplicados c
    ON t.num_cta = c.num_cta                        -- Unión por número de cuenta
GROUP BY c.num_doc
HAVING AVG(t.mnt_trn) > 150000                      -- Solo clientes con promedio alto
ORDER BY f_vinc ASC;                                -- Ordenar por fecha más antigua
