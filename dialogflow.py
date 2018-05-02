import os.path
import sys
import uuid
import json
import pprint
import apiai

CLIENT_ACCESS_TOKEN = '7036afe66a3846f7bbd1fbf8f13052c0'

def ask(query):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'ko'  # optional, default value equal 'en'

    request.session_id = uuid.uuid4().hex

    request.query = query

    response = request.getresponse().read()

    try:
        reply = (True, json.loads(response)['result']['fulfillment']['messages'][0]['speech'])
    except:
        reply = (False, "잘 모르겠어요")

    return reply
