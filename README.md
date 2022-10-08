Using vscode with python on Openshift

Simple app that connects and logs the host address.
```
from flask import Flask
import logging
import psycopg
import os


logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def hello():
    logging.info("called hello endpoint")


    dbname = os.getenv('POSTGRESQL_DATABASE')
    user = os.getenv('POSTGRESQL_USER')
    password = os.getenv('POSTGRESQL_PASSWORD')
    logging.info(f"POSTGRESQL_DATABASE = {dbname}")
    logging.info(f"POSTGRESQL_USER = {user}")
    logging.info(f"POSTGRESQL_PASSWORD = {password}")

    #
    # Make sure the service name and namespace are correct.
    # Should probably just read the POSTGRESQL_SERVICE_HOST env varible
    #
    params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'postgresql.bktest01',
    'port': 5432
    }

    conn = psycopg.connect(**params)
    logging.info(f"connection = {conn.info.hostaddr}")


    return "Hello Python!"

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
```

```
oc new-app python-test

oc new-app --template=postgresql-ephemeral -p POSTGRESQL_USER=postgresql -p POSTGRESQL_PASSWORD=postgresql -p POSTGRESQL_DATABASE=sampledb

oc rsync data postgresql-1-878q8:/var/tmp

oc rsh postgresql-podtutorial.com/postgresql-administration/postgresql-create-database/)
```

Connect
```
psql $POSTGRESQL_DATABASE $POSTGRESQL_USER
```
To manually create a database and a table see the 
[tutorial](https://www.postgresqltutorial.com/postgresql-administration/postgresql-create-database/)

Works but errors out
```
pg_restore -U $POSTGRESQL_USER -d $POSTGRESQL_DATABASE /var/tmp/data/dvdrental.tar
```
Misc admin commands
```
\l
\db
\dt
```

Silent but creates tables
```
pg_restore -U $POSTGRESQL_USER  -P $POSTGRESQL_PASSWORD -d $POSTGRESQL_DATABASE /var/tmp/data/dvdrental.tar
```

Pod Debugging
```
oc rsh postgres-pod
psql $POSTGRESQL_DATABASE $POSTGRESQL_USER
default=> \dt
default=> select * from welcome_pageview;
```

```
