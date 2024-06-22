import mysql.connector
from mysql.connector import errorcode

# MySQL RDS credentials and connection details
rds_endpoint = "userdatabase.c54ugca0ewft.us-west-2.rds.amazonaws.com"
port = 3306
db_name = "userdatabase"
username = "admin"
password = "Sonu619@"

# Define the table creation query
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""

try:
    # Establish the database connection
    connection = mysql.connector.connect(
        host=rds_endpoint, port=port, user=username, password=password, database=db_name
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Execute the table creation query
    cursor.execute(create_table_query)

    # Commit the changes
    connection.commit()

    print("User table created successfully.")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    elif err.errno == 2003:  # Can't connect to MySQL server
        print(f"Can't connect to MySQL server on '{rds_endpoint}:{port}'")
    else:
        print(err)
finally:
    try:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    except NameError:
        print("Connection was never established")
