import argparse
import os

import pandas as pd

from src.structure.flyweight.factory.style_factory import StyleFactory
from src.structure.flyweight.process.document import Document
from src.utils.logger import logger
from src.utils.timer import timer


@timer
def main(df: pd.DataFrame):
    try:
        document = Document()
        for _, row in df.iterrows():
            document.add_paragraph(
                row["text"],
                row["font"],
                row["size"],
                row["color"],
            )

        logger.info(
            f"ドキュメント全体のメモリ使用量: {document.get_memory_usage()}バイト"
        )
        logger.info(f"一意のスタイル数: {len(StyleFactory._styles)}")

    except Exception as e:
        logger.error(e)
        raise e


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--text", type=str, default="hello, world.", help="Name of the user"
    )
    parser.add_argument(
        "-f", "--font", default="Arial", type=str, help="Age of the user"
    )
    parser.add_argument("-s", "--size", default=10, type=int, help="Age of the user")
    parser.add_argument(
        "-c", "--color", default="red", type=str, help="Age of the user"
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    # 実行引数を読み取る
    args = get_parser()

    # 処理するデータを作成する
    _df = pd.DataFrame(
        {
            "text": [args.text],
            "font": [args.font],
            "size": [args.size],
            "color": [args.color],
        },
    )
    if os.path.exists("data/DB_text_editor.csv"):
        df = pd.read_csv("data/DB_text_editor.csv")
        df = pd.concat(
            [
                df,
                _df,
            ]
        )
    else:
        df = _df.copy()

    # 文書編集システムをエミュレートする
    main(df)

    # データを更新する
    df.to_csv("data/DB_text_editor.csv")
    logger.info("update to DB_text_editor.csv.")
