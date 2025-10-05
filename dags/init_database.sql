\c postgres;

DROP DATABASE IF EXISTS job_datawarehouse;
CREATE DATABASE job_datawarehouse;

\c job_datawarehouse;

CREATE SCHEMA bronze;
CREATE SCHEMA silver;
CREATE SCHEMA gold;

