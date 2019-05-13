from typing import Optional

from slack import WebClient, RTMClient


class SlackBot(object):
    def __init__(
        self,
        name: str,
        pattern: str,
        delay: int = 1,
        command: Optional[str] = None,
        **kwargs
    ):
        self.name = name
        self.pattern = pattern

        self.delay = delay
        self.command = command or "do"

        self.slack_id = None
        self.rtm_client = RTMClient(**kwargs)
        self.web_client = WebClient(**kwargs)

    def start(self):
        print("starting bot")
        self.rtm_client.start()

    @RTMClient.run_on(event="message")
    def parse_direct_mention(self, **kwargs) -> tuple:
        print("Enter event func")
        data = kwargs.get("data")
        print(data)

        if self.pattern in data.get("text"):
            channel_id = data.get("channel")
            thread_ts = data.get("ts")

            response = self.slack_client.chat_postMessage(
                channel=channel_id, text="Oi, ya nerd!", thread_ts=thread_ts
            )
            print(response)
