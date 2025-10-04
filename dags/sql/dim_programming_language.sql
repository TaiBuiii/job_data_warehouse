CREATE TABLE IF NOT EXISTS gold.dim_programming_language(
    programming_language_id SERIAL PRIMARY KEY,
    programming_language TEXT NOT NULL UNIQUE
);
TRUNCATE TABLE gold.dim_programming_language;
INSERT INTO gold.dim_programming_language (programming_language)
SELECT DISTINCT UNNEST(programming_languages) 
FROM silver.topcv_silver
WHERE programming_languages IS NOT NULL;
