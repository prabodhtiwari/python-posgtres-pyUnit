import configparser
import psycopg2

config = configparser.ConfigParser()
config.read('config.ini')

def connect():
    return psycopg2.connect(database=config['postgresDB']['database'], user=config['postgresDB']['user'], password=config['postgresDB']['password'], host=config['postgresDB']['host'], port=config['postgresDB']['port'])

