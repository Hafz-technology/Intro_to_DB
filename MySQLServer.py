# Write a simple python script that creates the database alx_book_store in your MySQL server.

# Name of python script should be MySQLServer.py
# If the database alx_book_store already exists, your script should not fail
# You are not allowed to use the SELECT or SHOW statements
# NOTE :

# Required to print message such as Database 'alx_book_store' created successfully! when database is successfully created.

# Print error message to handle errors when failing to connect to the DB.

# handle open and close of the DB in your script.
#!/usr/bin/python3
"""
A Python script to create the 'alx_book_store' database in a MySQL server.
"""

import mysql.connector
from mysql.connector import errorcode

def create_database():
    """
    Connects to MySQL and creates the alx_book_store database if it doesn't exist.
    """
    try:
        # Establish connection to MySQL server
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="your_password"  # Replace with your MySQL password
        )
        print("Successfully connected to MySQL server.")

        cursor = db_connection.cursor()

        # SQL command to create the database if it doesn't exist
        sql_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

        # Execute the query
        cursor.execute(sql_query)
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # Handle different types of errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(f"Error: {err}")
    finally:
        # Close the cursor and connection to ensure proper resource management
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
