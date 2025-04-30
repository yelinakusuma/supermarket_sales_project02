from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import psycopg2 as db # untuk connect PostgreSQL dengan python
import pandas as pd
import datetime as dt
from datetime import timedelta
from elasticsearch import Elasticsearch

# Fetch from Postgresql
def getData():
    '''
    Fungsi ini digunakan untuk mengambl data dari PostgreSQL 
    untuk selanjutnya dilakukan data cleaning
    '''
    conn_string = "dbname='project_m3' host='postgres' user='airflow' password='airflow'"
    conn = db.connect(conn_string)

    # Mengambil data menggunakan pandas
    df = pd.read_sql('SELECT * FROM public.table_m3', conn)
    df.to_csv('/opt/airflow/dags/P2M3_yelina_kusuma_data_raw.csv', index = False)
    print("======Data Saved======")

# Data Cleaning
def cleanData():
    '''
    Fungsi ini digunakan untuk melakukan data cleaning dari dataset,
    data akan disimpan lagi untuk di import ke ElasticSearch
    '''
    df = pd.read_csv('/opt/airflow/dags/P2M3_yelina_kusuma_data_raw.csv')
    df = df.drop_duplicates()
    df = df.fillna(0)
    df.columns = (df.columns.str.strip().str.lower().str.replace(' ', '_'))
    df.to_csv('/opt/airflow/dags/P2M3_yelina_kusuma_data_clean.csv', index = False)

# Post to Elasticsearch
def insertElastic():
    '''
    Fungsi ini digunakan untuk import hasil data cleaning ke Elasticsearch
    '''
    es = Elasticsearch("http://elasticsearch:9200")
    print('Connection status : ', es.ping())
    df = pd.read_csv('/opt/airflow/dags/P2M3_yelina_kusuma_data_clean.csv')
    for i, r in df.iterrows():
        doc = r.to_json()
        res = es.index(index = "m3", doc_type = 'doc', body = doc)
        print(res)

default_args = {
    'owner': 'yelin',
    'start_date': dt.datetime(2024, 11, 2, 9, 10, 0) - timedelta(hours=7),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
}

with DAG("M3CleanData",
         default_args = default_args,
         schedule_interval = '10-30/10 9 * * 6',
         catchup = False
         ) as dag:
    FetchfromPostgreSQL = PythonOperator(task_id = 'get', python_callable = getData)
    DataCleaning = PythonOperator(task_id = 'clean', python_callable = cleanData)
    PosttoElasticsearch = PythonOperator(task_id = 'insert', python_callable = insertElastic)

FetchfromPostgreSQL >> DataCleaning >> PosttoElasticsearch