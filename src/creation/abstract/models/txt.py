from src.creation.abstract.base.document import Document
from src.creation.abstract.error.error import FileNotFoundError
from src.utils.logger import logger


class TextDocument(Document):
    def open(self):
        try:
            if self.filename.exists():
                with open(self.filename, "r") as file:
                    self.content = file.read()
                logger.info(f"Opened text file: {self.filename}")
                logger.info(self.content)
            else:
                raise FileNotFoundError(
                    f"File {str(self.filename)} not found. Creating new file.",
                )
        except Exception as e:
            logger.error(e)
            raise e

    def save(self):
        with open(self.filename, "w") as file:
            file.write(self.content)
        logger.debug(f"Saved text file: {self.filename}")
