from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG (
    "hello_airflow",
    start_date = datetime(2025, 12, 7),
    schedule="@daily"
):
    
    task = BashOperator(
        task_id="say_hello",
        bash_command = "echo 'Hello from Airflow!!!'"
    )