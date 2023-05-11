from linebot import LineBotApi
from linebot.models import TextMessage, TextSendMessage

from config import LINE_CHANNEL_ACCESS_TOKEN

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)


def handle_message(event) -> None:
    """Event - User sent message

    Args:
        event (LINE Event Object): Refer to https://developers.line.biz/en/reference/messaging-api/#message-event
    """
    reply_token = event.reply_token

    # Text message
    if isinstance(event.message, TextMessage):
        # Get user sent message
        user_message = event.message.text

        # Reply with same message
        messages = TextSendMessage(text=user_message)
        line_bot_api.reply_message(reply_token=reply_token, messages=messages)
