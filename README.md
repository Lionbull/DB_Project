# DB_Project
Project for "Basics of Database Systems" course.

To run the program on Windows you should execute next lines in PowerShell:
```
python -m venv venv
Set-ExecutionPolicy Unrestricted -Scope Process
.\venv\Scripts\Activate.ps1
pip install bokeh
python .\project.py
```
The repository already contains "database.db" which is not modified. However, if you will to create a default database.db file yourself, run following command on **UNIX BASED** OS.
```
sqlite3 database.db < database.sql
```

[Link for the video about the interface.](https://youtu.be/t5Pkvn_wGQA)
