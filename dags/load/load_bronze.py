import psycopg2
from extract.extract import extract_jobcv
from logger import setup_logger
from psycopg2.extras import execute_batch


logger = setup_logger('load_bronze')
DB_config ={
    'host': 'postgres',
    'user': 'airflow',
    'password': 'airflow',
    'database' : 'job_datawarehouse',
    'port': 5432
}

def truncate_table(cursor):
    """
    Truncate table topcv_bronze in the bronze layer
    """
    cursor.execute("""
    TRUNCATE TABLE bronze.topcv_bronze;
    """)
    logger.info(f"Truncated table bronze.topcv_bronze")


def create_table(cursor):
    """
    Create table topcv_bronze in the bronze layer
    """
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bronze.topcv_bronze(
        title TEXT,
        description TEXT,
        requirement TEXT,
        location TEXT,
        position TEXT,
        education TEXT,
        quantity TEXT,
        salary TEXT,
        experience TEXT,
        company TEXT
    );
    """)
    logger.info(f"Created table bronze.topcv_bronze")

def insert_table(cursor,n):
    """
    Insert n jobs into topcv_bronze in the bronze layer
    """
    job_data = extract_jobcv(n)
    if job_data:
        query = """
        INSERT INTO bronze.topcv_bronze(title,description,requirement,location,position,education,quantity,salary,experience,company)
        VALUES (%(title)s,%(description)s,%(requirement)s,%(location)s,%(position)s,%(education)s,%(quantity)s,%(salary)s,%(experience)s,%(company)s)
        """
        execute_batch(cursor,query,job_data,page_size = 10)
        logger.info("Inserted table bronze.topcv_bronze")
    else:
        logger.warning("No job data fetched, skipping insertion")


def load_bronze(n = 10):
    """
    Create, truncate, and insert n jobs into topcv_bronze in the bronze layer
    """
    with psycopg2.connect(**DB_config) as conn:
        try:
            with conn.cursor() as cursor:
                create_table(cursor)
                truncate_table(cursor)
                insert_table(cursor,n)   
                conn.commit()
            logger.info(f"=========== Loaded successfully {n} jobs into bronze layer==============")

        except Exception as e:
            logger.error(f"Error loading bronze {e}",exc_info= True)
            conn.rollback()

if __name__ == '__main__':
    load_bronze(50)
