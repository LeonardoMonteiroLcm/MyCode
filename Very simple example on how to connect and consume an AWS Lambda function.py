import boto3 # pip install boto3
import json

# Replace with your AWS region and Lambda function name
AWS_REGION = "us-east-1"
LAMBDA_FUNCTION_NAME = "your_lambda_function_name"

def invoke_lambda(payload):
    # Initialize a session using the default credentials
    client = boto3.client("lambda", region_name=AWS_REGION)

    try:
        # Invoke the Lambda function
        response = client.invoke(
            FunctionName=LAMBDA_FUNCTION_NAME,
            InvocationType="RequestResponse",  # Can be "Event" for async calls
            Payload=json.dumps(payload),
        )

        # Read the response
        response_payload = json.load(response["Payload"])
        print("Response from Lambda:", response_payload)

        return response_payload

    except Exception as e:
        print(f"Error invoking Lambda function: {e}")
        return None

# Example payload to send to the Lambda function
example_payload = {
    "key1": "value1",
    "key2": "value2"
}

# Invoke the function
invoke_lambda(example_payload)
