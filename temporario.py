import json
import boto3
from custom_encoder import CustomEncoder
# client = boto3.client('dynamodb')
dynamodbTableName = 'clone-jobs1v'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(dynamodbTableName)

def lambda_handler(event, context):
  httpMethod = event["httpMethod"]



  # litar banco de dados
  if  httpMethod == "GET":
    res_statuscode = 200
    data = table.scan()
    res_data = data['Items']

    while 'LastEvaluatedKey' in data:
      data = table.scan(ExclusiveStartKey=data['LastEvaluatedKey'])

      res_data.extend(data['Items'])

    response = response_builder(res_statuscode, res_data)  
  
  
  # gravar no banco de dados
  elif httpMethod == "PUT":
    res_statuscode = 200
    res_body = "SUCCESS ! Item criated . . ."
    data = table.put_item(
      Item = {
        'id': 5,
        'name': 'Teste',
        'logado': 'doideira!'
      }
    )

    response = response_builder(res_statuscode, res_body)
  
  return response

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