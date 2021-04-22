import json


def lambda_handler(event, context):
    data = event['data']

    return {
        "status":200,
        "body":data
    }

    #  sam local invoke -e ./events/event.json