import json
# import base64


def lambda_handler(event, context):
    """
      Lambda handler function
      param: event: The event object for the lambda function.
      param: context: The context object
      return: THe labels foun in the image passed in the event object.
    """
    try:
        # Because this lambda is invoked by Api Gateway, then
        # we need to get the payload { "image": "encoded.." } from event['body']
        body = json.loads(event['body'])
        # Determine image source
        if 'image' in body:
            # Decode the image
            image_bytes = body['image'].encode('utf-8')

            # do processing

            resp = [{'Response1': 'Response string 1'}]
            return lambda_response(resp, True)
    except Exception as e:
        print(e)
        return lambda_response(None, False)


def lambda_response(response, success):
    if success:
        print('success')
        return {
            "statusCode": 200,
            "body": json.dumps(response),
        }
    else:
        print('error')
        return {
            "statusCode": 422,
            "body": json.dumps({'error': 'there was an error processing the image, check the log'})
        }
