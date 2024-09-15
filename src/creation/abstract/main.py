"""文書読み取りシステムを実行する

> poetry run python src/creation/abstract/main.py -f '["product.csv", "test_file.txt"]'
"""

import argparse
import ast
from typing import List

from src.creation.abstract.error.error import RequestParameterError
from src.creation.abstract.models.csv import CSVDocument
from src.creation.abstract.models.txt import TextDocument
from src.creation.abstract.params.params import DATA_DIR
from src.creation.abstract.process.document_maneger import DocumentManager
from src.utils.logger import logger
from src.utils.timer import timer
from src.utils.trace import trace


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--files", type=str, default=[], help="parser to filename"
    )
    args = parser.parse_args()
    file_list = ast.literal_eval(args.files)
    return file_list


def validate_extention(extention: str):
    if extention not in ["csv", "txt"]:
        raise RequestParameterError(
            f"{extention} extention must be ['.csv', '.txt'].",
        )


@timer
@trace
def main(files: List[str]):
    try:
        dm = DocumentManager()

        for _file in files:
            file = DATA_DIR.joinpath(_file)
            # 拡張子のバリデーション
            extention = str(file).split("/")[-1].split(".")[-1]
            validate_extention(extention)

            # 対応するモデルを定義して、プロセスへ読み込ませる
            if extention == "csv":
                document = CSVDocument(file)
            else:
                document = TextDocument(file)
            dm.add_document(document)

        # 処理実行
        dm.open_all()

    except Exception as e:
        logger.error(e)
        raise e


if __name__ == "__main__":
    file_list = get_parser()
    main(file_list)
