import os
import json
import pyrfc # The pyrfc library is used to interact with SAP via RFC.

# Define the connection parameters
conn_params = {
    'ashost': os.getenv('SAP_HOST'),   # SAP application host
    'sysnr': os.getenv('SAP_SYSNR'),   # System number
    'client': os.getenv('SAP_CLIENT'), # Client number
    'user': os.getenv('SAP_USER'),     # SAP username
    'passwd': os.getenv('SAP_PASS'),   # SAP password
    'lang': 'EN'                       # Language
}

try:
    # Establish the SAP connection
    conn = pyrfc.Connection(**conn_params)

    # Define the RFC function module to call SAP
    rfc_function = 'RFC_READ_TABLE' # Example RFC function to read table data
    table_name = 'KNA1'             # SAP table for customer master data

    # Call the RFC function in SAP
    result = conn.call(rfc_function, QUERY_TABLE=table_name, DELIMITER='|')

    # Process the result to extract customer data
    customers = []
    for row in result['DATA']:
        # Split the row data based on the delimiter
        fields = row['WA'].split('|')
        # Assuming the structure of KNA1 table, map fields to customer data
        customer = {
            'CustomerID': fields[0],
            'Name': fields[1],
            'City': fields[2],
            'Country': fields[3]
            # Add more fields as needed
        }
        customers.append(customer)

    # Convert the list of customers to JSON format
    customers_json = json.dumps(customers, indent=4)

    # Print the JSON data
    print(customers_json)

except pyrfc.exceptions.RfcConnectionError as e:
    # Handle connection errors (e.g., incorrect connection parameters)
    print(f"Error connecting to SAP: {e}")
except pyrfc.exceptions.RfcCommunicationError as e:
    # Handle communication errors (e.g., network issues)
    print(f"Communication error: {e}")
except pyrfc.exceptions.RfcAbapError as e:
    # Handle errors returned by the SAP system
    print(f"SAP system error: {e}")
except KeyError as e:
    # Handle missing keys in the result, for example if 'DATA' doesn't exist
    print(f"Error processing the result: Missing key {e}")
except Exception as e:
    # Catch all other exceptions
    print(f"An unexpected error occurred: {e}")
finally:
    # Ensure the connection is closed
    if conn:
        conn.close()