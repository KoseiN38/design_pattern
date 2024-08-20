from abc import ABC, abstractmethod


class Image(ABC):
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def get_metadata(self):
        pass
