from src.structure.proxy.base.base_image import Image
from src.structure.proxy.error.error import UnsupportedFileFormatError
from src.structure.proxy.models.image import RealImage
from src.structure.proxy.params.params import BE_ABLE_EXTENSTION


class ProxyImage(Image):
    """Imageのサブクラスとして、クライアントからアクセスされるRealImageクラスの中継クラス.

    NOTE: RealImageクラスへのアクセス制御し、追加の機能を拡張できる.

    Args:
        Image (_type_): _description_
    """

    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.filename.lower().endswith(BE_ABLE_EXTENSTION):
            if self.real_image is None:
                self.real_image = RealImage(self.filename)
            self.real_image.display()
        else:
            raise UnsupportedFileFormatError(
                f"Unsupported file format: {self.filename}. Only .jpg and .png are allowed."
            )

    def get_metadata(self):
        """画像統計情報をキーとして、キャッシュする.

        Returns:
            _type_: _description_
        """
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        return self.real_image.get_metadata()
