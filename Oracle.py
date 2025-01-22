import cx_Oracle # Ensure the cx_Oracle package is installed using pip install cx_Oracle.

host = "host" # Replace with your database host
port = "1521" # Default Oracle port
service_name = "service_name" # Replace with your service name
username = "username" # Replace with your username
password = "password" # Replace with your password

dsn = cx_Oracle.makedsn(host, port, service_name=service_name)
try:
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    cursor = connection.cursor()
    sql_query = "SELECT * FROM some_table"  # Replace 'some_table' with your table name
    cursor.execute(sql_query)
    for row in cursor:
        print(row)

except cx_Oracle.DatabaseError as e:
    print("Database error:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
        print("Connection closed.")
