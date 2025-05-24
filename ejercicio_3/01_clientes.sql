-- Crea la tabla clientes_sin_duplicados con registros únicos por tipo_doc, num_doc, cod_apli_prod y num_cta,
-- dejando solo el registro con la fecha de vinculación (f_vinc) más antigua.
CREATE TABLE clientes_sin_duplicados AS
SELECT *
FROM clientes c1
WHERE f_vinc = (
    SELECT MIN(f_vinc)
    FROM clientes c2
    WHERE c2.tipo_doc = c1.tipo_doc
      AND c2.num_doc = c1.num_doc
      AND c2.cod_apli_prod = c1.cod_apli_prod
      AND c2.num_cta = c1.num_cta
);