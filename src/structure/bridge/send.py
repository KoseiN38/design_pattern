from src.structure.bridge.models.html import HTMLMessageCreator
from src.structure.bridge.models.text import TextMessageCreator
from src.structure.bridge.process.send_email import EmailSender
from src.structure.bridge.process.send_sms import SMSSender
from src.utils.logger import logger


def main():
    html_creator = HTMLMessageCreator()
    text_creator = TextMessageCreator()

    email_sender = EmailSender(html_creator)
    sms_sender = SMSSender(text_creator)

    try:
        email_sender.send(
            content="<b>これはHTMLメールです</b>",
            recipient="user@sample.com",
        )
        sms_sender.send(
            content="これはテキストSMSです",
            recipient="+123456789",
        )

    except Exception as e:
        logger.error(e)
        raise e


if __name__ == "__main__":
    main()
