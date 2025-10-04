CREATE TABLE IF NOT EXISTS gold.dim_position(
    position_id SERIAL PRIMARY KEY,
    position_name TEXT UNIQUE NOT NULL
);
TRUNCATE TABLE gold.dim_position;
INSERT INTO gold.dim_position (position_name)
SELECT DISTINCT position
FROM silver.topcv_silver
WHERE position IS NOT NULL;