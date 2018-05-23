import os
import psycopg2

def connect():
    return psycopg2.connect(database=os.environ["DB"], user=os.environ["USER"], password=os.environ["PASSWORD"], host=os.environ["HOST"], port=os.environ["PORT"])

