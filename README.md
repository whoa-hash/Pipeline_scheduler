This is a workthrough of using Airflow, a task scheduler. 

It uses Python and can be seen on the Airflow UI (usually localhost:8080 if you are just starting out).

I used Ubuntu for WS for Linux as well as VSCode for Github access and a virtual python env.

For Windows system (VSCode):
{your venv name}/Scripts/Activate.ps1 activates the venv

For Linux system (Ubuntu):
{your venv name}\bin\activate

Things I came across:
Things I had to manually download include:
  graphviz (sudo install) (approve sudo install in settings)
  gcc
edits to the airflow config file with [Default] as a file header and _airflow db init: airflow scheduler_ - this is in the same folder that the venv is in.
airflow dags reserialize - to gather the dag/s
put the dags in the same folder that the venv is in
