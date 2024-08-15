from abc import ABC, abstractmethod


class MessageCreator(ABC):
    @abstractmethod
    def create_message(self, content: str) -> str:
        pass

    @abstractmethod
    def validate_recipient(self, recipient: str):
        pass
