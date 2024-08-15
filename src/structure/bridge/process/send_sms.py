from src.structure.bridge.base.base_tools import Sender
from src.structure.bridge.models.html import HTMLMessageCreator
from src.structure.bridge.models.text import TextMessageCreator


class SMSSender(Sender):
    def __init__(self, creator: TextMessageCreator | HTMLMessageCreator):
        self.creator = creator

    def send(self, content: str, recipient: str):
        self.creator.validate_recipient(recipient)
        message = self.creator.create_message(content)

        # TODO: 何かしら送信する処理を期待する
        print(f"Sending sms to {recipient}: {message}")
