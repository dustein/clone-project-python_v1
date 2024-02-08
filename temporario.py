import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
  httpMethod = event["httpMethod"]
  # litar banco de dados
  if  httpMethod == "GET":
    data = client.scan(TableName = 'clone-jobs1v')
    response = {
      'statusCode': 200,
      'body': json.dumps(data),
      'headers': {
        'Content-Type':'application/json',
        'Acess-Control-Allow-Origin': '*'
      }
    }
  
  # gravar no banco de dados
  elif httpMethod == "PUT":

    data = client.put_item(
      TableName = 'clone-jobs1v',
      Item = {
        'id':{'N':'6'},
        'name':{'S':'Duda'},
        'logado':{'S':'claro!'}
      }
    )
    response = {
      'statusCode' : 200,
      'body': "Item criado com sucesso!!!!",
      'headers': {
        'Content-Type':'application/json',
        'Acess-Control-Allow-Origin': '*'
      }
    }
  
  return response