# snarky-remarks-bot
Quick Slack bot implementation to choose a random response from a list upon a given trigger message.

## What is this
This is a quick implementation of a Slack Bot that looks for a pattern in a message.  
When it finds an occurence, it will comment a random response taken from a predefined text file and start a/comment on the thread.

It uses the Real Time Messaging Client from the [slack library](https://github.com/slackapi/python-slackclient) to process every message in the channels it's been added to,  
and then responds in a thread when a message contains a match to the pattern.

## Why
Why not? 🤔🤔

## Setup
1. Provide a list of responses (separated by new-lines) in a text file somewhere the bot has access.

    `echo "Yawn.... Oh, were you speaking?" >> ~/.config/snarky_responses.txt`

2. Register a new app in your Slack workspace to get access to the OAuth token
[The official docs](https://api.slack.com/apps?new_app=1) have more information regarding the setupprocess.

2. Create a `.env` file with the proper configuration values

    `cp .env.default snark_bot/.env`
    `vim snark_bot/.env`

3. Call the module from Python

    `python -m snark_bot`


