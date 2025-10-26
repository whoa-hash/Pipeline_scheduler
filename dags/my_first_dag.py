from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta

with DAG(
	'my_first_dag',
	start_date=datetime(2024, 1, 1),
	catchup=False
) as dag:


	def print_hello():
		print('Hi there!')

	hello_task = PythonOperator(
		task_id='hello_task',
		python_callable=print_hello
	)
