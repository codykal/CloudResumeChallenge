import json
import boto3
from decimal import Decimal

# import requests

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)

client = boto3.resource("dynamodb")
table = client.Table("cloud-resume-challenge")

def lambda_handler(event, context):
    response = table.get_item(
        Key={"ID": "Visitors"})
    count = response["Item"]["visitor_count"]
    print(count)
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        'body': json.dumps({"count": count}, cls=JSONEncoder)
        
    }
