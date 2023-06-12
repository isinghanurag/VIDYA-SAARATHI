import os
import json
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from message import postMessageToSlack,MessageParser
from user import User

import logging

# logger in a global context
# requires importing logging
logging.basicConfig(level=logging.DEBUG)

default_slack_channel = os.environ["SLACK_DEFAULT_CHANNEL"]
# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"], ssl_check_enabled=True)

@app.action("enroll")
def handle_some_action(ack, body, logger):
    ack()
    msg = MessageParser(body)
    usrId = msg.getUserID()
    user = User(usrId)
    user.addUserToDB()
    user.loadUserData()
    user.updateStatus(msg.getActionID())
    user.updateNextAction(msg.getNextAction())
    user.updateLastAction(msg.getActionID())
    user.updateDB()
    user.PostNextAction()

@app.action("technical_career_path")
def handle_some_action(ack, body, logger):
    ack()
    msg = MessageParser(body)
    usrId = msg.getUserID()
    user = User(usrId)
    user.loadUserData()
    user.updateNextAction(msg.getNextAction())
    user.updateLastAction(msg.getActionID())
    user.updateDB()
    user.PostNextAction()

@app.action("submit_short_term_goals")
def handle_some_action(ack, body, logger):
    ack()
    msg = MessageParser(body)
    usrId = msg.getUserID()
    user = User(usrId)
    user.loadUserData()
    user.updateNextAction(msg.getNextAction())
    user.updateLastAction(msg.getActionID())
    user.updateDB()
    user.PostNextAction()

@app.action("submit_long_term_goals")
def handle_some_action(ack, body, logger):
    ack()
    msg = MessageParser(body)
    usrId = msg.getUserID()
    user = User(usrId)
    user.loadUserData()
    user.updateNextAction(msg.getNextAction())
    user.updateLastAction(msg.getActionID())
    user.updateDB()
    user.PostNextAction()

@app.action("skills_submit")
def handle_some_action(ack, body, logger):
    ack()
    msg = MessageParser(body)
    usrId = msg.getUserID()
    user = User(usrId)
    user.loadUserData()
    user.updateNextAction(msg.getNextAction())
    user.updateLastAction(msg.getActionID())
    user.updateDB()
    user.PostNextAction()

@app.action("delta_skills_submit")
def handle_some_action(ack, body, logger):
    ack()
    msg = MessageParser(body)
    usrId = msg.getUserID()
    user = User(usrId)
    user.loadUserData()
    user.updateNextAction(msg.getNextAction())
    user.updateLastAction(msg.getActionID())
    user.updateDB()
    user.PostNextAction()

@app.action("dashboard")
def handle_some_action(ack, body, logger):
    ack()
    msg = MessageParser(body)
    usrId = msg.getUserID()
    user = User(usrId)
    user.loadUserData()
    user.updateNextAction(msg.getNextAction())
    user.updateLastAction(msg.getActionID())
    user.updateDB()
    user.PostNextAction()

@app.action("priorities")
def handle_some_action(ack, body, logger):
    ack()

@app.action("my-fitness-plan")
def handle_some_action(ack, body, logger):
    ack()
    msg = MessageParser(body)
    usrId = msg.getUserID()
    user = User(usrId)
    user.loadUserData()
    user.updateNextAction(msg.getNextAction())
    user.updateLastAction(msg.getActionID())
    user.updateDB()
    user.PostNextAction()

@app.action("health-submit")
def handle_some_action(ack, body, logger):
    ack()
    msg = MessageParser(body)
    usrId = msg.getUserID()
    user = User(usrId)
    user.loadUserData()
    user.updateNextAction(msg.getNextAction())
    user.updateLastAction(msg.getActionID())
    user.updateDB()
    user.PostNextAction()

@app.action("gwc_submit")
def handle_some_action(ack, body, logger):
    ack()
    msg = MessageParser(body)
    usrId = msg.getUserID()
    user = User(usrId)
    user.loadUserData()
    user.updateNextAction(msg.getNextAction())
    user.updateLastAction(msg.getActionID())
    user.updateDB()
    user.PostNextAction()


@app.action("my-success-plan")
def handle_some_action(ack, body, logger):
    ack()
    msg = MessageParser(body)
    usrId = msg.getUserID()
    user = User(usrId)
    user.loadUserData()
    user.updateNextAction(msg.getNextAction())
    user.updateLastAction(msg.getActionID())
    user.updateDB()
    user.PostNextAction()

@app.action("home")
def handle_some_action(ack, body, logger):
    ack()
    msg = MessageParser(body)
    usrId = msg.getUserID()
    user = User(usrId)
    user.loadUserData()
    user.updateNextAction(msg.getNextAction())
    user.updateLastAction(msg.getActionID())
    user.updateDB()
    user.PostNextAction()

@app.action("management_career_path")
def handle_some_action(ack, body, logger):
    ack()

@app.action("career_guidance")
def handle_some_action(ack, body, logger):
    ack()
    logger.info("droping " + "career_guidance" + "event")

@app.action("know_more")
def handle_some_action(ack, body, logger):
    ack()
    logger.info("droping " + "know_more" + "event")


@app.action("no_thanks")
def handle_some_action(ack, body, logger):
    ack()
    logger.info("droping " + "no_thanks" + "event")

@app.action("checkboxes-action")
def handle_some_action(ack, body, logger):
    ack()
    logger.info("droping " + "checkboxes-action" + "event")

if __name__ == "__main__":

    postMessageToSlack(default_slack_channel, './messages/welcome_survey.json')
    # Send Initial Survey to a public channel to enroll

    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()



