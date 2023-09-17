import mysql.connector

try:
    # establish connection to your MySQL server
    db_config = {
        "host": "localhost",
        "user": "testdb",
        "password": "Sandeep@123",
        "database": "test_database"
    }
    connection = mysql.connector.connect(**db_config)

    # create cursor object to execute sql queries
    cursor = connection.cursor()

    # write sql query to create the table
    # create_table_query = """
    # CREATE TABLE IF NOT EXISTS test_table (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     name VARCHAR(255) NOT NULL,
    #     age INT
    # )
    # """
    # Execute the SQL Query
    # cursor.execute(create_table_query)

    # inserts data
    insert_data = """
    INSERT INTO test_table (name, age)
    VALUES ('UAS', 30)
    """

    # Execute the SQL Query
    cursor.execute(insert_data)

    # commit the changes
    connection.commit()
    print("Data successfully inserted")

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()