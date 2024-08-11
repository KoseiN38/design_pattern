import argparse
from pathlib import Path

from src.structure.proxy.process.image_view import ImageViewer
from src.utils.logger import logger
from src.utils.timer import timer


@timer
def main(image: Path | str):
    try:
        logger.info("start viewing image processor.")
        viewer = ImageViewer()
        viewer.view_image(
            str(image),
        )
    except Exception as e:
        logger.error(e)
        raise e


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image", type=str, help="Name of the user")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    # 実行引数を読み取る
    args = get_parser()

    # 画像処理プロセスを実行する
    main(
        Path("data").joinpath(args.image),
    )
