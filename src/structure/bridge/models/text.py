import re

from src.structure.bridge.base.base_create import MessageCreator


class TextMessageCreator(MessageCreator):
    pattern = r"^\+?1?\d{9,15}$"

    def create_message(self, content: str) -> str:
        return content

    def validate_recipient(self, recipient: str):
        """電話番号のバリデーション."""
        if not re.match(TextMessageCreator.pattern, recipient):
            raise ValueError(f"Invalid phone number: {recipient}")
