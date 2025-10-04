CREATE TABLE IF NOT EXISTS gold.dim_job(
    job_id SERIAL PRIMARY KEY,
    job_name TEXT UNIQUE NOT NULL
);
TRUNCATE TABLE gold.dim_job;
INSERT INTO gold.dim_job (job_name)
SELECT DISTINCT title 
FROM silver.topcv_silver
WHERE title IS NOT NULL;
