from src.structure.flyweight.base.base_model import BaseModel
from src.structure.flyweight.models.paragraph_style import ParagraphStyle


class Paragraph(BaseModel):
    def __init__(self, text: str, style: ParagraphStyle):
        super().__init__()
        self._validate_string(text, "text")
        self._validate_instance(style, ParagraphStyle, "style")

        self.text = text
        self.style = style

    def __repr__(self):
        return f"Paragraph(text='{self.text}', style={self.style})"
