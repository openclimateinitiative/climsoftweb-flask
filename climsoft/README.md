# Using climsoft41.models

The ClimsoftWeb application can connect to multiple databases (see config.py SQLALCHEMY_BINDS).

The user selects with database to connect to when they log in.

Whenever you access a climsoft database you therefore need to change engine:

```
with users_choice_of_db:
    query = Station.query.get(stationId)


```



# Creating models from existing schema

```
pip install flask-sqlacodegen

python -m sqlacodegen.main --flask --outfile models.py mysql+mysqldb://<username>:<password>@<database-ip>:<port>/<database-name> [--tables <tablenames>] [--notables]

```

The models.py file contains `dt.Table` for those tables without primary keys since the SQLAlchemy ORM [requires a primary key](https://docs.sqlalchemy.org/en/14/faq/ormconfiguration.html#how-do-i-map-a-table-that-has-no-primary-key).
