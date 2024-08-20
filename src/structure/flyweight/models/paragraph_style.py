from src.structure.flyweight.base.base_model import BaseModel
from src.structure.flyweight.core.memory_usage import add_memory_usage


@add_memory_usage
class ParagraphStyle(BaseModel):
    def __init__(self, font, size, color):
        super().__init__()
        self._validate_string(font, "font")
        self._validate_positive_number(size, "size")
        self._validate_string(color, "color")

        self.font = font
        self.size = size
        self.color = color

    def __repr__(self):
        return f"ParagraphStyle(font='{self.font}', size={self.size}, color='{self.color}')"
