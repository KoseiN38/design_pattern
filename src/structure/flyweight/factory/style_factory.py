from src.structure.flyweight.models.paragraph_style import ParagraphStyle


class StyleFactory:
    """flyweightパターンに従った、ParagraphStyleクラスの仲介クラス.

    NOTE: ユニークなスタイルを辞書保存することで、メモリ削減を期待する.

    Returns:
        _type_: _description_
    """

    _styles = {}

    @classmethod
    def get_style(cls, font, size, color):
        key = (font, size, color)
        if key not in cls._styles:
            cls._styles[key] = ParagraphStyle(font, size, color)
        return cls._styles[key]
