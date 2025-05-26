-- ============================================================================
-- Fecha: 2025/05/25
-- Autor: Juan Pablo Jaramillo
-- Script: Crear e insertar en la tabla transacciones_acumuladas
-- Descripción: Este script crea una tabla con la suma total y acumulada del monto
--              de las transacciones agrupadas por fecha (f_aplicacion_trn)
--              y código de transacción (cod_trn), con redondeo a dos decimales.
-- Base de datos: SQLite
-- ============================================================================


-- Elimina la tabla transacciones_acumuladas si existe para evitar errores al crearla nuevamente
DROP TABLE IF EXISTS transacciones_acumuladas;

-- Crear tabla transacciones_acumuladas con estructura adecuada
CREATE TABLE transacciones_acumuladas (
    f_aplicacion_trn     TEXT,  -- Fecha de la transacción
    codigo_transaccion   TEXT,  -- Código de transacción
    monto_total          REAL,  -- Monto total por fecha y código de transacción
    monto_acumulado      REAL   -- Monto acumulado por fecha (ordenado por código)
);

-- Insertar datos agrupados y acumulados desde la tabla original
INSERT INTO transacciones_acumuladas (
    f_aplicacion_trn,           -- Fecha de la transacción
    codigo_transaccion,         -- Código de transacción
    monto_total,                -- Monto total por agrupación
    monto_acumulado             -- Monto acumulado dentro de la partición de fecha
)
SELECT
    f_aplicacion_trn,           -- Fecha de la transacción original
    cod_trn AS codigo_transaccion, -- Alias para mantener consistencia de nombres
    ROUND(SUM(mnt_trn), 2) AS monto_total, -- Suma del monto redondeada a 2 decimales
    ROUND(                                 
        SUM(SUM(mnt_trn)) OVER (           -- Suma acumulada con ventana
            PARTITION BY f_aplicacion_trn  -- Reinicia acumulado por cada fecha
            ORDER BY cod_trn               -- Acumulado en orden de código
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW -- Desde el inicio hasta la fila actual
        ),
        2                                  -- Redondeo a 2 decimales
    ) AS monto_acumulado
FROM transacciones                         -- Tabla fuente
GROUP BY f_aplicacion_trn, cod_trn;        -- Agrupación por fecha y código
