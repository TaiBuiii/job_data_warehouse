import os
import psycopg2
from logger import setup_logger

logger = setup_logger("load_gold")

DB_config = {
    'host': 'postgres',     
    'user': 'airflow',
    'password': 'airflow',
    'port': 5432,
    'database': 'job_datawarehouse'
}

sql_files = [
    "dim_location.sql",
    "dim_position.sql",
    "dim_programming_language.sql",
    "dim_skill.sql",
    "dim_company.sql",
    "dim_education.sql",
    "dim_job.sql",
    "fact_recruitment.sql",
    "bridge_job_location.sql",
    "bridge_job_programming_language.sql",
    "bridge_job_skill.sql"
]


def reset_gold_schema(cursor):
    """Xóa và tạo lại schema gold"""
    logger.info("Dropping and recreating schema 'gold'...")
    cursor.execute("""
    DROP SCHEMA IF EXISTS gold CASCADE;
    CREATE SCHEMA gold;
    """)


def execute_sql_files(cursor):
    """Đọc và thực thi các file SQL"""
    # Xác định đường dẫn tuyệt đối đến thư mục sql/
    base_path = os.path.join(os.path.dirname(__file__), "../sql")
    base_path = os.path.abspath(base_path)

    logger.info(f"SQL directory resolved to: {base_path}")

    for sql_file in sql_files:
        file_path = os.path.join(base_path, sql_file)

        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"{file_path} not found")

        logger.info(f"Executing {sql_file}...")
        with open(file_path, "r") as script:
            sql_command = script.read()
            cursor.execute(sql_command)


def load_gold():
    """Main function để load dữ liệu vào schema gold"""
    conn = None
    try:
        conn = psycopg2.connect(**DB_config)
        with conn.cursor() as cursor:
            logger.info("Resetting gold schema if exists...")
            reset_gold_schema(cursor)

            execute_sql_files(cursor)

            conn.commit()
            logger.info("✅ Load gold successfully completed!")

    except Exception as e:
        logger.error(f"❌ Error loading gold: {e}", exc_info=True)
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
            logger.info("Connection closed.")


if __name__ == "__main__":
    load_gold()
