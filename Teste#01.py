import psycopg2
import pandas as pd



conn = psycopg2.connect(dbname="tributos_estaduais", user="postgres", password="c4Mp1N45", host="localhost")
data = pd.read_sql_table('Tributos', conn)


