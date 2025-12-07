from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Python Operator

def say_hello():
    print("Hello! Đây là PythonOperator!")
    return "PythonOperator is awesome!"

def print_message(ti):
    message = ti.xcom_pull(task_ids = "task_hello")
    print("Dữ liệu nhận được từ task_hello:", message)





with DAG(
    dag_id = "level2",
    start_date = datetime(2025, 12, 7),
    schedule_interval = None,
    catchup = False,
) as dag :
    
    task_hello = PythonOperator(
        task_id="task_hello",
        python_callable = say_hello,
    )

    task_print = PythonOperator(
        task_id = "task_print",
        python_callable = print_message,
    )

    #dependent
    task_hello >> task_print