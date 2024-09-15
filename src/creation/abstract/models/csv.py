import pandas as pd

from src.creation.abstract.base.document import Document
from src.creation.abstract.error.error import FileNotFoundError
from src.utils.logger import logger


class CSVDocument(Document):
    def open(self):
        try:
            if self.filename.exists():
                self.content = pd.read_csv(self.filename)
                logger.info(f"Opened CSV file: {self.filename}")
                logger.info(self.content)
            else:
                raise FileNotFoundError(
                    f"File {str(self.filename)} not found. Creating new file.",
                )
        except Exception as e:
            logger.error(e)
            raise e

    def save(self, *, encoding: str = "utf-8", index: bool = False):
        self.content.to_csv(self.filename, encoding=encoding, index=index)
        logger.debug(f"Saved CSV file: {str(self.filename)}.")
