CREATE TABLE IF NOT EXISTS gold.dim_location(
    location_id SERIAL PRIMARY KEY,
    location TEXT UNIQUE NOT NULL
);
TRUNCATE TABLE gold.dim_location;
INSERT INTO gold.dim_location (location)
SELECT DISTINCT UNNEST(silver.topcv_silver.locations)
FROM silver.topcv_silver
WHERE locations IS NOT NULL;