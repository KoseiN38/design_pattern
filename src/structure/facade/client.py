"""ファイル操作と計算処理をfacadeパターンでまとめる.

> python src/structure/facade/client.py
  --content "hello, world"
  --is-write True
"""

import argparse
import json
from datetime import datetime
from pathlib import Path

from src.structure.facade.controller.data_process import DataProcessor
from src.structure.facade.controller.file_manege import FileManager
from src.utils.logger import logger


# Facade
class TextAnalyzerFacade:
    def __init__(self):
        self.file_manager = FileManager()
        self.data_processor = DataProcessor()

    def analyze_file(self, filename: str | Path, *, is_write: bool = False) -> str:
        try:
            content = self.file_manager.read_file(filename)

            word_count = self.data_processor.count_words(content)
            line_count = self.data_processor.count_lines(content)

            report = json.dumps(
                {
                    "filename": str(filename),
                    "word_count": word_count,
                    "line_count": line_count,
                }
            )
            logger.info(report)

            report_filename = Path("data").joinpath(
                f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            )
            if is_write:
                self.file_manager.write_file(str(report_filename), report)

            return f"Analysis complete. Report saved as '{report_filename}'."
        except Exception as e:
            logger.error(e)
            raise e


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--file", type=str, default="test_file.txt", help="Name of the user"
    )
    parser.add_argument("-c", "--content", type=str, help="Age of the user")
    parser.add_argument(
        "-w", "--is-write", type=bool, default=False, help="Age of the user"
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    # 実行引数の読み取り
    args = get_parser()
    logger.info(
        f"req params: file={args.file}, content={args.content}, is_write={args.is_write}"
    )

    facade = TextAnalyzerFacade()

    # テスト用のファイルを作成
    test_filename = Path("data").joinpath(args.file)
    FileManager.write_file(test_filename, args.content)

    # シンプルなインターフェースから実行する
    result = facade.analyze_file(test_filename, is_write=args.is_write)
    logger.info(result)
