# Define the Lambda function code
# The actual function logic is implemented in the `lambda_handler` function
# You should have a file named `hello_world_lambda.py` with a function named `lambda_handler`
# that handles the Lambda function logic
def lambda_handler(event, context):
  print("The first function has been invoked!!")
  return {
    'statusCode': 200,
    'body': "Hello, World!.\n This is the first function."
  }
