from abc import ABC, abstractmethod


class Sender(ABC):
    @abstractmethod
    def send(self, message: str, recipient: str):
        pass
