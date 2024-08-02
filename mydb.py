

import psycopg2
from psycopg2 import sql

try:
    dataBase = psycopg2.connect(
        host='localhost',
        user='venkat',
        password='venkat98',
        port='5432'
    )
    cursorObj = dataBase.cursor()
    dataBase.autocommit = True
    cursorObj.execute("CREATE DATABASE CRM_Apk")

    print("Database 'CRM_Apk' created successfully")

except psycopg2.Error as e:
    print(f"Error: {e}")

finally:
    dataBase.autocommit = False  
    if cursorObj:
        cursorObj.close()
    if dataBase:
        dataBase.close()
