CREATE TABLE IF NOT EXISTS gold.dim_company(
    company_id SERIAL PRIMARY KEY,
    company_name TEXT NOT NULL UNIQUE
);
TRUNCATE TABLE gold.dim_company;
INSERT INTO gold.dim_company (company_name)
SELECT DISTINCT company 
FROM silver.topcv_silver
WHERE company IS NOT NULL;
