CREATE TABLE IF NOT EXISTS gold.bridge_job_programming_language(
    job_id INT NOT NULL,
    programming_language_id INT NOT NULL,
    PRIMARY KEY(job_id,programming_language_id),
    CONSTRAINT fk_job FOREIGN KEY (job_id) REFERENCES gold.dim_job(job_id),
    CONSTRAINT fk_programming_language FOREIGN KEY (programming_language_id) REFERENCES gold.dim_programming_language(programming_language_id)
);

TRUNCATE TABLE gold.bridge_job_programming_language;

INSERT INTO gold.bridge_job_programming_language (job_id,programming_language_id)
SELECT DISTINCT gold.dim_job.job_id, gold.dim_programming_language.programming_language_id
FROM silver.topcv_silver
LEFT JOIN gold.dim_job ON gold.dim_job.job_name = silver.topcv_silver.title
CROSS JOIN LATERAL UNNEST(silver.topcv_silver.programming_languages) AS sub(language)
LEFT JOIN gold.dim_programming_language ON gold.dim_programming_language.programming_language = sub.language;
