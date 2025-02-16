import os
import json
import pyodbc # pip install pyodbc
import signal
import sys
import traceback

class SqlServerEnvironment:
    REQUIRED_VARS = ["server", "user", "password", "database"]

    DATABASE_CONFIG = {
        "server": os.getenv("DB_SERVER"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_NAME"),
        "encrypt": True,
        "trust_server_certificate": os.getenv("DB_TRUST_CERT", "false").lower() == "true",
    }

    QUERY_USERS = os.getenv("DB_QUERY_ALL_USERS", "SELECT * FROM Users")

    @classmethod
    def validate_config(cls):
        """Validates that all mandatory variables have been defined correctly."""
        missing_vars = [var for var in cls.REQUIRED_VARS if not cls.DATABASE_CONFIG[var]]
        if missing_vars:
            raise ValueError(f"Invalid configuration. Missing: {', '.join(missing_vars)}")

class SqlServer:
    @staticmethod
    def _get_connection():
        """Creates and returns a database connection."""
        try:
            env = SqlServerEnvironment

            if not env.DATABASE_CONFIG["server"]:
                raise ValueError("DB_SERVER was not configured correctly.")

            connection_string = ";".join(["DRIVER={ODBC Driver 17 for SQL Server}",
                f"SERVER={env.DATABASE_CONFIG['server']}",
                f"DATABASE={env.DATABASE_CONFIG['database']}",
                f"UID={env.DATABASE_CONFIG['user']}",
                f"PWD={env.DATABASE_CONFIG['password']}",
                "Encrypt=YES"
                    if env.DATABASE_CONFIG["encrypt"]
                    else "Encrypt=NO",
                "TrustServerCertificate=YES"
                    if env.DATABASE_CONFIG["trust_server_certificate"]
                    else "TrustServerCertificate=NO"])
            return pyodbc.connect(connection_string)
        except pyodbc.Error as e:
            print(f"Error connecting to SQL Server: {e}")
            raise

    @staticmethod
    def execute_query(query: str):
        """Executes an SQL query and returns the results."""
        connection = None
        try:
            connection = SqlServer._get_connection()
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in rows]
        except pyodbc.Error as e:
            print("Error executing query:", e)
            traceback.print_exc()
            raise
        finally:
            if connection:
                connection.close()

    @staticmethod
    def get_query_json(query: str) -> str:
        """Executes an SQL query and returns the result in JSON format."""
        try:
            data = SqlServer.execute_query(query)
            return json.dumps(data, indent=4)
        except Exception as e:
            print("Error converting query to JSON:", e)
            traceback.print_exc()
            raise

def main():
    """Main function to test the connection and query execution."""
    try:
        env = SqlServerEnvironment
        print("Testing get_query_json()...")
        json_result = SqlServer.get_query_json(env.QUERY_USERS)
        print(json_result)
    except Exception as e:
        print("Error fetching JSON from query:", e)
        traceback.print_exc()

def signal_handler(sig, frame):
    """Signal handling to terminate the program correctly."""
    print("Closing the program...")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    main()
