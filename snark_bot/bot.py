import re
import time
from typing import Optional

from slack import RTMClient


class SlackBot(object):
    def __init__(
        self,
        name: str,
        regex: str,
        delay: int = 1,
        command: Optional[str] = None,
        **kwargs,
    ):
        self.name = name
        self.regex = regex

        self.delay = delay
        self.command = command or "do"

        self.slack_id = None
        self.slack_client = RTMClient(**kwargs)

        self._authenticate()

    def _authenticate(self):
        def _is_slack_config_okay() -> bool:
            return self.slack_client.rtm_connect(with_team_state=False)

        if _is_slack_config_okay():
            self.slack_id = self.slack_client.api_call("auth.test")["user_id"]
            print(f"Bot {self.name} is up and running.")
        else:
            print(f"Bot {self.name} connect connect to Slack.")

    def start(self):
        while True:
            messages = self.slack_client.rtm_read()

            command, channel = self.parse_commands(messages)
            if command:
                self.handle_command(command, channel)

            time.sleep(self.delay)

    def parse_commands(self, slack_events: list) -> tuple:
        for event in slack_events:
            if event["type"] == "message" and "subtype" not in event:
                user_id, message = self.parse_direct_mention(event["text"])
                if user_id == self.slack_id:
                    return message, event["channel"]

        return None, None

    def parse_direct_mention(self, message_text) -> tuple:
        matches = re.search(self.regex, message_text)

        # First group == username, second group == message
        if not matches:
            return None, None

        return (matches.group(1), matches.group(2).strip())

    def handle_command(self, command, channel):
        default_response = "Note sure what you mean."
        response = None

        if command.startswith("dink"):
            response = "Sure man heyo"

        self.slack_client.api_call(
            "chat.postMessage", channel=channel, text=response or default_response
        )
