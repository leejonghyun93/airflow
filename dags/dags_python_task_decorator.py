from airflow import DAG
import pendulum
from airflow.decorators import task


with DAG(
    dag_id="dags_python_task_Decorator",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2025, 11, 10, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    
    @task(task_id="python_task_1")
    def print_context(some_input):
        print(some_input)
    
    run_this = print_context('task_Decorator 실행')