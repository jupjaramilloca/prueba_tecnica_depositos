-- ============================================================================
-- Fecha: 2025/05/25
-- Autor: Juan Pablo Jaramillo
-- Script: Crear e insertar en la tabla clientes_sin_duplicados
-- Descripción: Este script crea una tabla que almacena registros únicos 
--              de la tabla clientes, según los campos tipo_doc, num_doc,
--              cod_apli_prod y num_cta. En caso de duplicados, se conserva 
--              únicamente el registro con la fecha de vinculación (f_vinc) 
--              más antigua.
-- Base de datos: SQLite
-- ============================================================================

-- Elimina la tabla clientes_sin_duplicados si existe para evitar errores al crearla nuevamente
DROP TABLE IF EXISTS clientes_sin_duplicados;

-- Crea la tabla clientes_sin_duplicados con los campos especificados y sus tipos de datos
CREATE TABLE clientes_sin_duplicados (
    tipo_doc        TEXT,      -- Tipo de documento del cliente
    num_doc         TEXT,      -- Número de documento del cliente
    f_vinc          INTEGER,   -- Fecha de vinculación (en formato numérico)
    cod_apli_prod   TEXT,      -- Código de aplicación o producto asociado
    num_cta         TEXT       -- Número de cuenta asociado
);

-- Inserta los registros únicos en clientes_sin_duplicados
INSERT INTO clientes_sin_duplicados (tipo_doc,num_doc,f_vinc,cod_apli_prod,num_cta)
    WITH clts AS (
        SELECT
            tipo_doc,
            num_doc,
            f_vinc,
            cod_apli_prod,
            num_cta,
            ROW_NUMBER() OVER (
                PARTITION BY tipo_doc, num_doc, cod_apli_prod, num_cta  -- Agrupa posibles duplicados
                ORDER BY f_vinc ASC                                     -- Ordena por la fecha más antigua
            ) AS rn                                                     -- Número de fila por grupo
        FROM clientes
    )
    -- Selecciona solo el primer registro (más antiguo) de cada grupo duplicado
    SELECT
        tipo_doc,
        num_doc,
        f_vinc,
        cod_apli_prod,
        num_cta
    FROM clts
    WHERE rn = 1;  -- Mantiene solo el primer registro de cada grupo (fecha más antigua)
