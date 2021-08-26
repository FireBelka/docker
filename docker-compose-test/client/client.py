#import urllib.request
#import urllib#http = urllib3.PoolManager()
#payload = '+add info'
#encoded_data = json.dumps(payload).encode('utf-8')
#r = http.request('POST', 'http://localhost:1234',
#                body=payload, headers={'Content-Type': 'text/html'}
#)
#print(r.data)

import time
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            port=3306
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def update_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name,
            port=3306
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection
def write_to_db(connection,message):
 cursor=connection.cursor()
 try:
  cursor.execute(message)
  print(message+ " Message wrote to db")
 except Error as e:
  print("Error during writing message to db: '{e}'")

def request_to_db(connection,message):
 cursor=connection.cursor()
 try:
  cursor.execute(message)
  resp=cursor.fetchall()
  print(resp)
 except Error as e:
  print("Error during writing message to db: '{e}'")


time.sleep(5)
connection = create_connection('localhost', 'root', 'Cat_1234')
create_database_query = "CREATE DATABASE IF NOT EXISTS sm_app"
create_database(connection, create_database_query)
connection = update_connection('localhost', 'root', 'Cat_1234', 'sm_app')
create_table="""CREATE TABLE IF NOT EXISTS posts(data TEXT );"""
write_to_db(connection, create_table)
write_data="""INSERT INTO posts(data) VALUES ('hello world');"""
write_to_db(connection, write_data)
write_data="""SELECT * FROM posts;"""
request_to_db(connection, write_data)

connection.close()
