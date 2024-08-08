class DataProcessor:
    @staticmethod
    def count_words(text: str) -> int:
        return len(text.split())

    @staticmethod
    def count_lines(text: str) -> int:
        return len(text.splitlines())
