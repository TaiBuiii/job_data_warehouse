from airflow import DAG  # type: ignore
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator  # type: ignore

from load.load_bronze import load_bronze
from load.load_silver import load_silver
from load.load_gold import load_gold

default_args = {
    'owner': 'MyName',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='job_datawarehouse',
    default_args=default_args,
    description='ELT',
    start_date=datetime(2025, 9, 20),
    schedule='@weekly',  
    catchup=False
) as dag:

    task_bronze = PythonOperator(
        task_id='load_bronze',
        python_callable=load_bronze
    )

    task_silver = PythonOperator(
        task_id='load_silver',
        python_callable=load_silver
    )

    task_gold = PythonOperator(
        task_id='load_gold',
        python_callable=load_gold
    )

    task_bronze >> task_silver >> task_gold
