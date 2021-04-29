# 1. Import module
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator


# 2. Default arguments
default_args = {
    'owner': 'airflow-dag',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2),
    'email': ['dan.phan.mq@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,

}

# 3. Instantiate a DAG

dag = DAG(
    'first_dag_demo',
    default_args=default_args,
    description="A first simple DAG",
    schedule_interval=timedelta(days=1)
)

# 4. Tasks

t1 = BashOperator(
    task_id='print_data',
    bash_command='date',
    dag=dag,
)

t1.doc_md = """
### Task documentation
You can document your task using attributes `doc_md` markdown
"""

dag.doc_md = __doc__

t2 = BashOperator(
    task_id='sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    dag=dag,
)

templated_command = """
{% for i in range(5) %}
    echo "{{ ds }}"
    echo "{{ macros.ds_add(ds, 7)}}"
    echo "{{ params.my_param }}"
{% endfor %}
"""

t3 = BashOperator(
    task_id='templated',
    depends_on_past=False,
    bash_command=templated_command,
    params={'my_param': 'Paramater I passed in'},
    dag=dag,
)

# 5. Set up dependencies
t1 >> [t2, t3]