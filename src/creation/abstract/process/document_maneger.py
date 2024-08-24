from src.creation.abstract.base.document import Document
from src.creation.abstract.error.error import DocumentNotFoundError
from src.creation.abstract.models.csv import CSVDocument
from src.utils.logger import logger


class DocumentManager:
    def __init__(self):
        self.documents = {}

    def add_document(self, document: Document):
        self.documents[document.filename] = document

    def remove_document(self, filename):
        if filename in self.documents:
            del self.documents[filename]
            logger.info(f"Removed document: {filename}")
        else:
            logger.error(f"Document not found: {filename}")

    def open_all(self):
        if len(self.documents) == 0:
            raise DocumentNotFoundError(
                "Target Document object is not found.",
            )

        for doc in self.documents.values():
            doc.open()

    def save_all(self):
        if len(self.documents) == 0:
            raise DocumentNotFoundError(
                "Target Document object is not found.",
            )

        for doc in self.documents.values():
            if isinstance(doc, CSVDocument):
                doc.save(encoding="utf-8", index=False)
            else:
                doc.save()
