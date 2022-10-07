from flask import Flask
import psycopg
import os
 
app = Flask(__name__)


@app.route('/')
def hello():

    dbname = os.getenv('POSTGRESQL_DATABASE')
    print(f"dbname = {dbname}")
    # Get these from the env
    params = {
    'dbname': 'sampledb',
    'user': 'user3AC',
    'password': '4aE7FULrxjXrsyA1',
    'host': 'postgresql.python-test.svc.cluster.local',
    'port': 5432
    }

    conn = psycopg.connect(**params)

    cur = conn.cursor()
    dict_cur = cur.execute("SELECT * FROM staff")
    print(f"dict_cur = {dict_cur}")
    record = dict_cur.fetchone()
    print(f"record = {record}")
    ret = record[4]
    print(f"return = {ret}")
    return ret

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
