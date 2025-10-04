CREATE TABLE IF NOT EXISTS gold.dim_education_level(
    education_level_id SERIAL PRIMARY KEY,
    education_level TEXT UNIQUE NOT NULL
);
TRUNCATE TABLE gold.dim_education_level;
INSERT INTO gold.dim_education_level (education_level)
SELECT DISTINCT education 
FROM silver.topcv_silver
WHERE education IS NOT NULL;