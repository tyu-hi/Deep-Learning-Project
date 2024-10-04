import json
import boto3

sagemaker_runtime = boto3.client('sagemaker-runtime')

def lambda_handler(event, context):
    # parse user message 
    body = json.loads(event['body'])
    user_message = body['message']

    # call SageMaker endpoint
    response = sagemaker_runtime.invoke_endpoint(
        EndpointName='chatbot-endpoint',
        ContentType='application/json',
        Body=json.dumps({'message': user_message})
    )
    
    # parse SageMaker model's response
    result = json.loads(response['Body'].read().decode())
    chatbot_reply = result['response']

    # return response to API Gateway
    return {
        'statusCode': 200,
        'body': json.dumps({'response': chatbot_reply})
    }
