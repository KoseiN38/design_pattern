import json
import os
from pathlib import Path


# Complex subsystem classes
class FileManager:
    @staticmethod
    def read_file(filename: str | Path) -> str:
        if not os.path.exists(filename):
            return ""
        with open(filename, "r") as file:
            return file.read()

    @staticmethod
    def write_file(filename: str, content: str) -> None:
        with open(filename, "w") as file:
            json.dump(content, file, indent=4)
