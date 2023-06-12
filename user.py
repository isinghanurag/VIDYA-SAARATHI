from pathlib import Path
import json
import os
import logging
from message import postMessageToSlack,MessageParser

db_dir = os.environ["SLACK_DB_PATH"] + '/';
msg_dir = os.environ["SLACK_MESSAGES_PATH"] + '/';

class User :
    
    def __init__(self, user_id):
        self.user_id = user_id
        self.db_file = db_dir + user_id + '.json' 

    def _createDBFile(self) :
        with open(self.db_file, 'w') as f:
            data = {'user_id' : self.user_id}
            f.write(json.dumps(data, indent=2))

    def _updateDBFile(self) :
        with open(self.db_file, 'w') as f:
            f.write(json.dumps(self.__dict__, indent=2))

    def updateDB(self):
        self._updateDBFile()

    def updateStatus(self, status) :
        self.status = status

    def updateNextAction(self, action) :
        self.next_action = action

    def updateLastAction(self, action) :
        self.last_action = action

    def addUserToDB(self):
        path = Path(self.db_file)
        if path.is_file():
            # TODO error checks
            return;
        self._createDBFile()

    def loadUserData(self):
        with open(self.db_file) as f:
            jsonData = json.load(f)
        self.__dict__.update(jsonData)

    def PostNextAction(self):
        postMessageToSlack(self.user_id, msg_dir + self.next_action+'.json') 
        
    def dump(self):
        logging.info(json.dumps(self.__dict__, indent=2))
