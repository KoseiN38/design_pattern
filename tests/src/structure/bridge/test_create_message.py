import pytest

from src.structure.bridge.models.html import HTMLMessageCreator
from src.structure.bridge.models.text import TextMessageCreator


# 正常系テスト
@pytest.mark.parametrize("content", ["Text", ""])
def test_html_creator_create_message(content):
    html_creator = HTMLMessageCreator()
    message = html_creator.create_message(f"<p>{content}</p>")
    assert f"<html><body><p>{content}</p></body></html>" in message


@pytest.mark.parametrize("content", ["Text message", ""])
def test_text_creator_create_message(content):
    text_creator = TextMessageCreator()
    message = text_creator.create_message(content)
    assert content == message


# 異常系テスト
@pytest.mark.parametrize(
    "invalid_email",
    [
        "invalid_email",
        "user@domain",
        "user@.com",
        "@domain.com",
    ],
)
def test_html_creator_validate_recipient_invalid_email(invalid_email):
    html_creator = HTMLMessageCreator()
    with pytest.raises(ValueError):
        html_creator.validate_recipient(invalid_email)


@pytest.mark.parametrize("invalid_email", [123, None])
def test_html_creator_validate_recipient_invalid_email_to_typeerror(invalid_email):
    html_creator = HTMLMessageCreator()
    with pytest.raises(TypeError):
        html_creator.validate_recipient(invalid_email)


@pytest.mark.parametrize(
    "invalid_phone",
    [
        "123",
        "abcdefghij",
        "+1234",
        "1234567890abcd",
    ],
)
def test_text_creator_validate_recipient_invalid_phone(invalid_phone):
    text_creator = TextMessageCreator()
    with pytest.raises(ValueError):
        text_creator.validate_recipient(invalid_phone)


@pytest.mark.parametrize("invalid_phone", [123, None])
def test_text_creator_validate_recipient_invalid_phone_to_typeerror(invalid_phone):
    text_creator = TextMessageCreator()
    with pytest.raises(TypeError):
        text_creator.validate_recipient(invalid_phone)
