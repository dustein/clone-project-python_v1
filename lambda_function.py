import boto3
import json
import logging
from custom_encoder import CustomEncoder

logger = logging.getLogger()
logger.setLevel(logging.INFO)
#DynamoDB
dynamodbTableName = 'clone-jobs'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(dynamodbTableName)
# metodos
getMethod = 'GET'
postMethod = 'POST'
patchMethod = 'PATCH'
deleteMethod = 'DELETE'
# Os paths da API
inicialPath = '/inicial'
jobsPath = '/jobs'

def lambda_handler(event, context):
  logger.info(event)
  httpMethod = event['httpMethod']
  path = event['path']

  if httpMethod == getMethod and path == inicialPath:
    response = buildResponse(200)
  elif httpMethod == getMethod and path == jobsPath:
    response = getAllJobs(event['queryStringParameters']['jobID'])
  elif httpMethod == postMethod and path == jobsPath:
    response = createJob(json.loads(event['body']))
  elif httpMethod == deleteMethod and path == jobsPath:
    requestBody = json.loads(event['body'])
    response = modifyJob(requestBody['jobID'], requestBody['updateKey'], requestBody['updateValue'])
  elif httpMethod == deleteMethod and path == jobsPath:
    requestBody = json.loads(event['body'])
    response = deleteJob(requestBody['jobID'])
  else:
    response = buildResponse(404, 'Not Found!')
  
  return response

def getAllJobs():
  
  try:
    response = table.get_item(
      Key = {'jobID': jobID}
    )
    if 'Item' in response:
      return buildResponse(200, response['Item'])
    return buildResponse(404, {"message":"jobID %s not found" % jobID})
  except:
    logger.exception("")
def buildResponse(statusCode, body=None):
  response = {
    'statusCode': statusCode,
    'headers': {
      'Content-Type':'application/json',
      'Acess-Control-Allow-Origin': '*' #para acessar a API em hospedagem de fora CORS
    }
  }
  if body is not None:
    response['body'] = json.dumps(body, cls=CustomEncoder)


