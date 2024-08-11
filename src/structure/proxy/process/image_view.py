from src.structure.proxy.error.error import UnsupportedFileFormatError
from src.structure.proxy.factory.image_proxy import ProxyImage
from src.utils.logger import logger


class ImageViewer:
    def __init__(self):
        self.image_cache = {}

    def view_image(self, filename):
        try:
            proxy_image = ProxyImage(filename)
            metadata = proxy_image.get_metadata()
            if metadata not in self.image_cache:
                self.image_cache[metadata] = proxy_image
            self.image_cache[metadata].display()
        except UnsupportedFileFormatError as e:
            logger.error(f"Error: {e}")
            raise e
