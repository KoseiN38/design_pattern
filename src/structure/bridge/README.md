# 概要

抽象化と実装を分離し、それぞれを独立して拡張できるようにするものです。

ここでは、異なる形式でメッセージを送信するシステムを例として使用します。このパターンにより、メッセージの形式（テキスト、HTML）と送信方法（メール、SMS）を柔軟に組み合わせることができます。

## ダイアグラム図

```mermaid
classDiagram
    class MessageCreator {
        <<abstract>>
        +create_message(content: string)* string
        +validate_recipient(recipient: string)*
    }

    class TextMessageCreator {
        +create_message(content: string) string
        +validate_recipient(recipient: string)
    }

    class HTMLMessageCreator {
        +create_message(content: string) string
        +validate_recipient(recipient: string)
    }

    class MessageSender {
        <<abstract>>
        +send(message: string, recipient: string)*
    }

    class EmailSender {
        -creator: MessageCreator
        +send(content: string, recipient: string)
    }

    class SMSSender {
        -creator: MessageCreator
        +send(content: string, recipient: string)
    }

    MessageCreator <|-- TextMessageCreator
    MessageCreator <|-- HTMLMessageCreator
    MessageSender <|-- EmailSender
    MessageSender <|-- SMSSender
    MessageSender o-- MessageCreator
```

## 使用例

* 入力

```python
 poetry run python src/send.py
```

* 出力

```sh
```

## 共有事項
