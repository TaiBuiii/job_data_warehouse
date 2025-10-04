-- Đang kết nối vào postgres
\c postgres;

-- Drop và tạo lại DB
DROP DATABASE IF EXISTS job_datawarehouse;
CREATE DATABASE job_datawarehouse;

-- Kết nối vào DB mới
\c job_datawarehouse;

-- Tạo schema
CREATE SCHEMA bronze;
CREATE SCHEMA silver;
CREATE SCHEMA gold;
