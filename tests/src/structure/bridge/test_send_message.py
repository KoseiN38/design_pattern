import pytest

from src.structure.bridge.models.html import HTMLMessageCreator
from src.structure.bridge.models.text import TextMessageCreator
from src.structure.bridge.process.send_email import EmailSender
from src.structure.bridge.process.send_sms import SMSSender


# 正常系テスト
@pytest.mark.parametrize("content", ["Text", ""])
def test_email_sender_send(content):
    html_creator = HTMLMessageCreator()
    email_sender = EmailSender(html_creator)
    assert email_sender.send(f"<p>{content}</p>", "test@example.com") is None


@pytest.mark.parametrize("content", ["Text", ""])
def test_sms_sender_send(content):
    text_creator = TextMessageCreator()
    sms_sender = SMSSender(text_creator)
    assert sms_sender.send(content, "+12345678901") is None


# 異常系テスト
def test_email_sender_integration():
    html_creator = HTMLMessageCreator()
    email_sender = EmailSender(html_creator)

    # 正常系
    assert email_sender.send("<p>Test</p>", "test@example.com") is None

    # 異常系
    with pytest.raises(ValueError):
        email_sender.send("<p>Test</p>", "invalid_email")

    # 異常系
    with pytest.raises(TypeError):
        email_sender.send("<p>Test</p>", None)


def test_sms_sender_integration():
    text_creator = TextMessageCreator()
    sms_sender = SMSSender(text_creator)

    # 正常系
    assert sms_sender.send("Test message", "+12345678901") is None

    # 異常系
    with pytest.raises(ValueError):
        sms_sender.send("Test message", "invalid_phone")

    # 異常系
    with pytest.raises(TypeError):
        sms_sender.send("Test message", None)
