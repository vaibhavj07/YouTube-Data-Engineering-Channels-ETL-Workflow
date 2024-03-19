from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from Youtube_API import fetch_data_engineering_channels

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['user@google.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'DAG_youtube',
    default_args=default_args,
    description='ETL Pipeline for fetching Youtube Data about Data Engineering channels',
    schedule_interval=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='Complete_Youtube_ETL',
    python_callable=fetch_data_engineering_channels,
    dag=dag, 
)

run_etl