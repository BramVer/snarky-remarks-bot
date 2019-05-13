from smart_getenv import getenv

from snark_bot.bot_two import SlackBot


if __name__ == "__main__":
    print("In main")
    name = getenv("SLACK_BOT_NAME", type=str)
    token = getenv("SLACK_BOT_TOKEN", type=str)
    pattern = getenv("SLACK_BOT_RESPONSE_PATTERN", type=str)

    bot = SlackBot(name, pattern, token=token)
    print("Created bot")

    bot.start()
