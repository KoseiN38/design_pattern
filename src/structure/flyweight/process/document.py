from src.structure.flyweight.core.memory_usage import add_memory_usage
from src.structure.flyweight.factory.style_factory import StyleFactory
from src.structure.flyweight.models.paragraph import Paragraph


@add_memory_usage
class Document:
    def __init__(self):
        self.paragraphs = []

    def add_paragraph(self, text, font, size, color):
        style = StyleFactory.get_style(font, size, color)
        self.paragraphs.append(Paragraph(text, style))

    def __repr__(self):
        return "\n".join(str(p) for p in self.paragraphs)
