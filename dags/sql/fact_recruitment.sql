CREATE TABLE IF NOT EXISTS gold.fact_recruitment(
    id SERIAL PRIMARY KEY,
    job_id INT NOT NULL,
    company_id INT,
    position_id INT,
    education_level_id INT,
    experience INT,
    quantity INT,
    min_salary FLOAT,
    max_salary FLOAT,
    CONSTRAINT fk_job FOREIGN KEY (job_id) REFERENCES gold.dim_job(job_id),
    CONSTRAINT fk_company FOREIGN KEY (company_id) REFERENCES gold.dim_company(company_id),
    CONSTRAINT fk_position FOREIGN KEY (position_id) REFERENCES gold.dim_position(position_id),
    CONSTRAINT fk_education_level FOREIGN KEY (education_level_id) REFERENCES gold.dim_education_level(education_level_id)
);

TRUNCATE TABLE gold.fact_recruitment;
INSERT INTO gold.fact_recruitment (job_id,company_id,position_id,education_level_id,experience,quantity,min_salary,max_salary)
SELECT  gold.dim_job.job_id, 
        gold.dim_company.company_id,
        gold.dim_position.position_id,
        gold.dim_education_level.education_level_id,
        silver.topcv_silver.experience,
        silver.topcv_silver.quantity,
        silver.topcv_silver.min_salary,
        silver.topcv_silver.max_salary
FROM silver.topcv_silver
LEFT JOIN gold.dim_job ON gold.dim_job.job_name = silver.topcv_silver.title
LEFT JOIN gold.dim_company ON gold.dim_company.company_name = silver.topcv_silver.company
LEFT JOIN gold.dim_position ON gold.dim_position.position_name = silver.topcv_silver.position
LEFT JOIN gold.dim_education_level ON gold.dim_education_level.education_level = silver.topcv_silver.education
