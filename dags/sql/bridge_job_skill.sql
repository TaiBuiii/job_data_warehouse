CREATE TABLE IF NOT EXISTS gold.bridge_job_skill(
    job_id INT NOT NULL,
    skill_id INT NOT NULL,
    PRIMARY KEY (job_id,skill_id),
    CONSTRAINT fk_job FOREIGN KEY (job_id) REFERENCES gold.dim_job(job_id),
    CONSTRAINT fk_skill FOREIGN KEY (skill_id) REFERENCES gold.dim_skill(skill_id)
);

TRUNCATE TABLE gold.bridge_job_skill;

INSERT INTO gold.bridge_job_skill(job_id,skill_id)
SELECT DISTINCT gold.dim_job.job_id , gold.dim_skill.skill_id
FROM silver.topcv_silver
LEFT JOIN gold.dim_job ON gold.dim_job.job_name = silver.topcv_silver.title
CROSS JOIN LATERAL UNNEST(silver.topcv_silver.required_skills) AS sub(skill)
LEFT JOIN gold.dim_skill ON gold.dim_skill.skill_name = sub.skill;