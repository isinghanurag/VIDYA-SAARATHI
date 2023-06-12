# creators-lab
Creators Lab Slack App 

# Environment Variables
export SLACK_DEFAULT_CHANNEL="test"
export SLACK_APP_TOKEN="xapp-1-A034YH0S6JU-3144844098581-2a803704ad6a08cb2e9c7be0c0fcb10ac8bf169aa53fddce2fd70e96f693fbd6"
export SLACK_BOT_TOKEN="xoxb-3153831080657-3141928069589-eb93vRDjFodWnvFaC8vCNpZ9"
export SLACK_DB_PATH="db"
export SLACK_MESSAGES_PATH="messages"

![image](https://media.github.hpe.com/user/18962/files/bb0e7d06-bf7c-408d-97d2-45bdb2ead030)
=======

# Creator's Verse Bot

## Bot Design

Creator's Verse Bot is an app designed off a python plugin called slack_bolt. This plugin helps to build an interactive slack app on the workspace with latest platform features. The bot is designed to give interactive responses to user in the particular Slack workspace. It helps them to track career and fitness goals.  ![CreatorsVerseHelp](https://media.github.hpe.com/user/39188/files/84334587-2004-4b9b-9edf-64627d284968)

## How to Setup

Below are the steps to set-up creator's verse bot in linux environment. Clone the git repository

```
git clone git@github.hpe.com:vrashi-p-r/creators-lab.git
cd creators-lab
pip3 install -r requirements.txt

```

Install slack_bolt on the system. This should automatically install "slack-sdk" also along with it, if not install it manually using "pip3 install slack-sdk"

```
pip3 install slack_bolt

```

Now, from the home directory of system, open ".local/lib/python3.8/site-packages/slack_sdk/web/base_client.py" file in an editor and make changes like below 1. Add the below lines right before "class BaseClient:" starts ``` import ssl

```
vctx = ssl.create_default_context()
vctx.check_hostname = False
vctx.verify_mode = ssl.CERT_NONE
```
In def __ init __(), replace "self.ssl = ssl" by "self.ssl = vctx" like below
   self.token = None if token is None else token.strip()
   self.base_url = base_url
   self.timeout = timeout
   self.ssl = vctx
   self.proxy = proxy
   self.headers = headers or {}
   self.headers["User-Agent"] = get_user_agent(
   user_agent_prefix, user_agent_suffix
   )
Start the Bot
1 .Export all Environment Variables
1 .python3 <>.py
