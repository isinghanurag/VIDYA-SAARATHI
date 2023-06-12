import requests
import logging
import json
import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

access_token = os.environ["SLACK_BOT_TOKEN"] 
slackUrl = "https://slack.com/api/chat.postMessage"


def postMessageToSlack(channel, jsonFile):
    with open(jsonFile) as f:
        jsonData = json.load(f)
    jsonData['channel'] = channel
    result = requests.post(slackUrl,
                      headers={'Content-Type':'application/json',
                               'Authorization': 'Bearer {}'.format(access_token)
                                },
                        data=json.dumps(jsonData),
                        verify=False, 
                        allow_redirects=False
                        )

def getItemfromObject(obj, key):
    if key in obj: return obj[key]
    for k, v in obj.items():
        if isinstance(v,dict):
            return getItemfromObject(v, key)

class MessageParser:
    
    def __init__(self, message):
        if 'type' in message:
            self._type = message['type']
        if 'user' in message:
            self._user = message['user']
        if 'state' in message:
            self._state = message['state']
        if 'actions' in message:
            self._actions = message['actions'][0]

    def getUserID(self):
        return self._user['id']

    def getNextAction(self):
        return self._actions['value']

    def getActionID(self):
        return self._actions['action_id']

    def dump(self):
        logging.info(json.dumps(self._type, indent=2))
        logging.info(json.dumps(self._user, indent=2))
        logging.info(json.dumps(self._state, indent=2))
        logging.info(json.dumps(self._actions, indent=2))
