# Project: Connect Database

This is a repo for managing PostgreSQL project. It provides lots of features:

- Connect PostgrepSQL Database
- show all databases in PostgrepSQL Database
- show all table names in PostgrepSQL Database
- show all table datas in PostgrepSQL Database
- filter datas in PostgrepSQL Database

# Projectile in Action

- show all databases in PostgrepSQL Database
  ![](./output/01_index_databases.png)

- show all table names in PostgrepSQL Database
  ![](./output/02_get_tablenames.png)

- show all table datas in PostgrepSQL Database
  ![](./output/03_get_table_all_datas.png)
- filter datas in PostgrepSQL Database
  ![](./output/04_get_table_filter_datas.png)
- show all table datas in PostgrepSQL Database
  ![](./output/05_get_course_table_all_datas.png)

# Quickstart

The instructions that follow are meant to get you from zero to a running Project setup in a minute.

First, install requirements.txt

```
pip install -r requirements.txt
```

Secondly, Open your PostgreSQL, make sure it runs in your computer and port is 5432.

Last but not least, run the django project

```bash
python manage.py runserver 9900
```

Open your browser and visit the url `http://127.0.0.1:9900`

