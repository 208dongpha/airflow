from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id = "level1",
    start_date = datetime(2025, 12, 7),
    schedule_interval = "@daily",
    catchup = False,
) as dag:
    
    start = BashOperator(
        task_id = "start",
        bash_command = "echo 'Start task running!'",
    )

    process = BashOperator(
        task_id = "process",
        bash_command = "echo 'Processing data...'",
    )

    finish = BashOperator(
        task_id = "finish",
        bash_command = "echo 'Finished succesfully!'",
    )

    #dependecy
    start >> process >> finish