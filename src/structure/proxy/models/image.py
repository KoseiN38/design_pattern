import time

from PIL import Image as PILImage

from src.structure.proxy.base.base_image import Image
from src.utils.logger import logger


class RealImage(Image):
    """画像の表示やメタデータを出力するクラス.

    ただし、クライアントから直接リクエストすることを想定しない.

    Args:
        Image (_type_): _description_
    """

    def __init__(self, filename):
        self.filename = filename
        self.image = None
        self.load_image_from_disk()

    def load_image_from_disk(self):
        logger.info(f"Loading {self.filename} from disk...")
        time.sleep(1)  # シミュレートされたロード時間
        try:
            self.image = PILImage.open(self.filename)
            logger.info(f"{self.filename} loaded.")
        except IOError:
            logger.error(f"Error: Unable to load {self.filename}.")
            raise

    def display(self):
        if self.image:
            width, height = self.image.size
            logger.info(f"Displaying {self.filename}")
            logger.info(f"Width: {width}px")
            logger.info(f"Height: {height}px")
            logger.info(f"Format: {self.image.format}")
            logger.info(f"Mode: {self.image.mode}")
            if hasattr(self.image, "info") and "dpi" in self.image.info:
                logger.info(
                    f"Resolution: {self.image.info['dpi'][0]}x{self.image.info['dpi'][1]} DPI"
                )
        else:
            logger.error(f"Error: Image {self.filename} is not loaded.")

    def get_metadata(self):
        if self.image:
            width, height = self.image.size
            return (self.filename, width, height)
        return (self.filename, None, None)
