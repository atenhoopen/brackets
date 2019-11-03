import os
import json

from utils import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def main(event, context):
    table = dynamodb.Table('brackets')

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
