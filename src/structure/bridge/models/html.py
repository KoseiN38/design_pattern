import re

from src.structure.bridge.base.base_create import MessageCreator


class HTMLMessageCreator(MessageCreator):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    def create_message(self, content: str) -> str:
        return f"<html><body>{content}</body></html>"

    def validate_recipient(self, recipient):
        """メールアドレスのバリデーション."""
        if not re.match(HTMLMessageCreator.pattern, recipient):
            raise ValueError(f"Invalid email address: {recipient}")
