import os
import json
from dotenv import load_dotenv


def lambda_handler(event, context):
    """Lambda function to protect the api

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

    context: object, required
        Lambda Context runtime methods and attributes

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict
    """

    try:
        print(event)
        is_authorized = event['headers']['authorization'] == os.getenv(
            'AUTHORIZATION_SECRET_TOKEN')
        print(is_authorized)
        if is_authorized:
            print("true")
            return authorized(True)
        else:
            print("false")
            return authorized(False)

    except Exception as e:
        print(e)
        return authorized(False)


def authorized(is_authorized):
    return {"isAuthorized": is_authorized}
