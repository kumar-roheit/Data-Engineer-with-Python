
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
