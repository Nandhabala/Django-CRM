"""ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root@1234';
FLUSH PRIVILEGES;"""

"""import mysql.connector

database=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root@1234'
)

#perpare cursor object
cursorObject=database.cursor()
#create database
cursorObject.execute("CREATE DATABASE nandha")

print("All done!")"""
import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    database = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root@1234',
        auth_plugin='mysql_native_password'  # Specify authentication plugin
    )

    if database.is_connected():
        print("Connected to MySQL server")

        # Prepare cursor object
        cursorObject = database.cursor()

        # Create database
        cursorObject.execute("CREATE DATABASE IF NOT EXISTS crm")
        print("Database 'crm' created successfully")

except Error as e:
    print(f"Error: {e}")

finally:
    if 'database' in locals() and database.is_connected():
        cursorObject.close()
        database.close()
        print("MySQL connection is closed")

print("All done!")


