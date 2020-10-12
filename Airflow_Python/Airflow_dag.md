
### Airflow

> syntax: ` `

#### Operators 
* every single task in an airflow workflow is called an Operator.
  * They run independently.
  * there are various types of Operators
  
> Types of Operators
  **BashOperator, PythonOperator, EmailOperator **
  
-Bash Operators
* used to execute bash command and scripts 
* run the command in a temporary directory 

```py 
from airflow.operators.bash_operator import BashOperator
example_task = BashOperator(task_id = 'bash_task',
                            bash_command = 'echo 1',
                            dag = dag)
bash_task = BashOperator(task_id = 'clean_addresses'
                        bash_command='cat addresses.txt | awk "NF == 10" > cleaned.txt',
                        dag = dag)
```


* Defining a task SLA
  To define SLA task on a specific task 
  
```py
# Import the timedelta object
from datetime import timedelta

test_dag = DAG('test_workflow', start_date=datetime(YYYY,M,DD), schedule_interval='@None')

# Create the task with the SLA
task1 = ChoiceofOperator(task_id='random_task_id_Name',
                     sla=timedelta((days=4, hours=10, minutes=20, seconds=30)),
                     bash_command='insert_bash_file_name_here.sh',
                     dag= insert_dag_name)
```
