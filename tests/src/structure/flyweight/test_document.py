import pytest

from src.structure.flyweight.factory.style_factory import StyleFactory
from src.structure.flyweight.process.document import Document


@pytest.fixture(autouse=True)
def clear_style_factory():
    """各テスト前後でクリアにする."""
    StyleFactory._styles.clear()
    yield
    StyleFactory._styles.clear()


def test_document_style_reuse():
    """正常系テスト.

    任意のスタイルを追加して、ユニークなスタイルのみが保存されていることを確認する.
    """
    document = Document()

    # 異なるスタイルを追加
    document.add_paragraph("Paragraph 1", "Arial", 12, "black")
    document.add_paragraph("Paragraph 2", "Times New Roman", 14, "red")
    document.add_paragraph("Paragraph 3", "Calibri", 10, "blue")

    # 重複するスタイルを追加
    document.add_paragraph("Paragraph 4", "Arial", 12, "black")  # 重複
    document.add_paragraph("Paragraph 5", "Times New Roman", 14, "red")  # 重複

    # 新しいスタイルを追加
    document.add_paragraph("Paragraph 6", "Helvetica", 16, "green")

    # 期待される結果:
    # - ドキュメントには6つの段落がある
    # - StyleFactoryには4つのユニークなスタイルがある（重複は再利用される）

    assert len(document.paragraphs) == 6
    assert len(StyleFactory._styles) == 4


def test_document_extensive_style_reuse():
    """正常系テスト.

    重複するスタイルを5回追加して、ユニークなスタイル数と重複を除いたスタイル数が保存されていることを確認する.
    """
    document = Document()
    styles = [
        ("Arial", 12, "black"),
        ("Times New Roman", 14, "red"),
        ("Calibri", 10, "blue"),
        ("Helvetica", 16, "green"),
    ]

    # 各スタイルを5回ずつ使用
    for _ in range(5):
        for font, size, color in styles:
            document.add_paragraph(f"Paragraph with {font}", font, size, color)

    # 期待される結果:
    # - ドキュメントには20の段落がある
    # - StyleFactoryには4つのユニークなスタイルがある

    assert len(document.paragraphs) == 20
    assert len(StyleFactory._styles) == 4
