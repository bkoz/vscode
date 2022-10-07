from flask import Flask
import psycopg
import os
import logging
 
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)


@app.route('/')
def hello():

    dbname = os.getenv('POSTGRESQL_DATABASE')
    user = os.getenv('POSTGRESQL_USER')
    password = os.getenv('POSTGRESQL_PASSWORD')
    logging.info(f"POSTGRESQL_DATABASE = {dbname}")
    logging.info(f"POSTGRESQL_USER = {user}")
    logging.info(f"POSTGRESQL_PASSWORD = {password}")

    params = {
    'dbname': dbname,
    'user': user,
    'password': password,
    'host': 'postgresql.python-test',
    'port': 5432
    }

    conn = psycopg.connect(**params)

    cur = conn.cursor()
    dict_cur = cur.execute("SELECT * FROM staff")
    record = dict_cur.fetchone()
    logging.info(f"one database record = {record}")
    # Return the email field.
    ret = record[4]
    return ret

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
