CREATE TABLE IF NOT EXISTS gold.bridge_job_location( 
    job_id INT NOT NULL,
    location_id INT NOT NULL,
    PRIMARY KEY (job_id,location_id), 
    CONSTRAINT fk_job FOREIGN KEY (job_id) 
    REFERENCES gold.dim_job(job_id), 
    CONSTRAINT fk_location 
    FOREIGN KEY (location_id) 
    REFERENCES gold.dim_location(location_id) ); 
TRUNCATE TABLE gold.bridge_job_location; 
INSERT INTO gold.bridge_job_location (job_id,location_id) 
SELECT DISTINCT gold.dim_job.job_id, gold.dim_location.location_id 
FROM silver.topcv_silver LEFT JOIN gold.dim_job ON gold.dim_job.job_name = silver.topcv_silver.title 
CROSS JOIN LATERAL UNNEST(silver.topcv_silver.locations) AS sub(location) 
LEFT JOIN gold.dim_location ON gold.dim_location.location = sub.location