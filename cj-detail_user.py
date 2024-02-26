import json
import boto3
from custom_encoder import CustomEncoder

dynamodbTableName = 'clone-jobs'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(dynamodbTableName)

def lambda_handler(event, context):

  user_pk = event['queryStringParameters']['PK']
  user_sk = event['queryStringParameters']['SK']

  response = table.get_item(
    Key = {'PK': user_pk, 'SK': user_sk}
  )
  if 'Item' in response:
    return response_builder(200, response['Item'])
  return response_builder(404, {"message":"User %s not found" % user_pk})
  
def response_builder(statusCode, body=None):
  res_data = {
    'statusCode' : statusCode,
    'headers': {
      'Content-Type':'application/json',
      'Acess-Control-Allow-Origin': '*'
    }
  }
  if body:
    res_data['body'] = json.dumps(body, cls=CustomEncoder)

  return res_data