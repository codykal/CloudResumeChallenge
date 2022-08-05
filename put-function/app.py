import json
import boto3


# import requests
client = boto3.resource("dynamodb")
table = client.Table("cloud-resume-challenge")

Key = {"ID": "Visitors"}

def lambda_handler(event, context):

    response = table.get_item(
        Key={"ID": "Visitors"})
    count = response["Item"]["visitor_count"]
    
    new_count = int(count)+1
    response = table.update_item(
        Key={'ID': 'Visitors'},
        UpdateExpression='SET visitor_count = :c',
        ExpressionAttributeValues={':c': new_count},
        ReturnValues='UPDATED_NEW'
    )


    return {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Headers': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'}
    }

