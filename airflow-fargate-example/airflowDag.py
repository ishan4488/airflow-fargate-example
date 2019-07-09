import sys
from datetime import datetime
from datetime import timedelta

from airflow import DAG

from airflow.operators.dummy_operator import DummyOperator
from airflow.contrib.operators.ecs_operator import ECSOperator

DAG_NAME = 'Test_Dag'

default_args = {
    'owner': 'Ishan Rastogi',
    'start_date': datetime(2019, 6, 8),
    'email': ['ishan4488@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=1)
}


def get_ecs_operator_args(param):

    return dict(
        launch_type="FARGATE",
        # The name of your task as defined in ECS
        task_definition="my_automation_task",
        # The name of your ECS cluster
        cluster="my-cluster",
        network_configuration={
            'awsvpcConfiguration': {
                'securityGroups': ['sg-hijk', 'sg-abcd'],
                'subnets': ['subnet-lmn'],
                'assignPublicIp': "ENABLED"
            }
        },
        overrides={
            'containerOverrides': [
                {
                    'name': "my-container",
                    'command': ["python", "myCode.py",
                                str(param)]
                }
            ]
        },

        region_name="us-east-1")


ecs_args = get_ecs_operator_args("{{ dag_run.conf['name'] }}")

dag = DAG( DAG_NAME,
          schedule_interval=None,
          default_args=default_args)

start_process = DummyOperator(task_id="start_process", dag=dag)

fargate_task = ECSOperator(task_id="fargate_task", **ecs_args, dag=dag)

start_process >> fargate_task