from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

dag = DAG(
    dag_id = 'Sample-Dag',
    default_args = default_args,
    schedule_interval = None,
    catchup=False,
)


with dag:

    t1 = EmptyOperator(task_id='task1')