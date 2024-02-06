import boto3
import json
import logging

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
inicial = '/inicial'
jobs = '/jobs'

def lambda_handler(event, context):
  logger.info(event)
  httpMethod = event['httpMethod']
  path = event['path']

  
