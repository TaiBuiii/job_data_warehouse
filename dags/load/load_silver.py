import psycopg2
import pandas as pd
from logger import setup_logger
from transform.transform import transform_topcv
from psycopg2.extras import execute_batch
logger = setup_logger("load_silver")

DB_config = {
    'host': 'postgres',
    'user': 'airflow',
    'password': 'airflow',
    'port': 5432,
    'database': 'job_datawarehouse'
}
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS silver.topcv_silver(
        id serial,
        title VARCHAR(50),
        programming_languages TEXT[],
        required_skills TEXT[],
        education VARCHAR(50),
        experience INT,
        position VARCHAR(50),
        locations TEXT[],
        quantity INT,
        min_salary FLOAT,
        max_salary FLOAT,
        company VARCHAR(255)
    );
    """)
def truncate_table(cursor):
    cursor.execute("""
    TRUNCATE TABLE silver.topcv_silver;
    """)
def load_table(cursor, df : pd.DataFrame):
    records = df.to_dict(orient="records")
    insert_query = """
    INSERT INTO silver.topcv_silver(title,programming_languages,required_skills,education,experience,position,locations,quantity,min_salary,max_salary,company)
    VALUES (%(title)s,%(programming_languages)s,%(required_skills)s,%(education)s,%(experience)s,%(position)s,%(locations)s,%(quantity)s,%(min_salary)s,%(max_salary)s,%(company)s)
    """
    execute_batch(cursor, insert_query, records)


def load_silver():
    try:
        with psycopg2.connect(**DB_config) as conn:
            with conn.cursor() as cursor:
                raw_df = pd.read_sql("SELECT * FROM bronze.topcv_bronze", conn)
                logger.info("Extracting data from bronze.topcv_bronze table...")
                clean_df = transform_topcv(raw_df)
                create_table(cursor)
                logger.info("Creating table...")
                truncate_table(cursor)
                logger.info("Truncating table...")
                load_table(cursor,clean_df)
                logger.info("Loading to silver.topcv_silver")
                conn.commit()
                logger.info("Load silver successfully")
    except Exception as e:
        logger.error(f"Error loading silver {e}",exc_info= True)
        conn.rollback()
    return clean_df

if __name__ == '__main__':
    load_silver()
