import os
import pandas as pd
import psycopg2

def merge_postgresql_datasets(table_names):
    connection_params = {
        'host': 'localhost',
        'port': '5432',
        'database': 'example_databse',
        'user': os.getenv('DB_USERNAME'),
        'password': os.getenv('DB_PASSWORD')
    }

    conn = psycopg2.connect(**connection_params)


    datasets = []
    for table_name in table_names:
        #For e.g. this query selects and returns items from specific category which have avg price above 100  
        query = f"SELECT category, AVG(price) FROM {table_name} GROUP BY category HAVING AVG(price) > 100;"
        dataset = pd.read_sql(query, conn)
        datasets.append(dataset)

    merged_dataset = pd.concat(datasets)
    
    conn.close()

    return merged_dataset

