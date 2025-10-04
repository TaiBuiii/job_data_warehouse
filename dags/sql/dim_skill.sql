CREATE TABLE IF NOT EXISTS gold.dim_skill(
    skill_id SERIAL PRIMARY KEY,
    skill_name TEXT NOT NULL UNIQUE
);
TRUNCATE TABLE gold.dim_skill;
INSERT INTO gold.dim_skill (skill_name)
SELECT DISTINCT UNNEST(required_skills)
FROM silver.topcv_silver
WHERE required_skills IS NOT NULL;
