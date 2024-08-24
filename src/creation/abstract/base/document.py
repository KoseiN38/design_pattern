from abc import ABC, abstractmethod
from pathlib import Path


class Document(ABC):
    """文書処理システムの抽象基底クラス."""

    def __init__(self, filename: str | Path):
        self.filename = filename

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def save(self):
        pass
