class BasicWord:
    def __init__(self, word, sub_words):
        self.word = word
        self.sub_words = sub_words

    def __repr__(self):
        sub_words = ', '.join(self.sub_words)
        return f"Слово {self.word}: {sub_words}"

    def is_sub_words(self, word):
        """Проверка на наличие слова в списке подслов"""
        return word in self.sub_words

    def count_sub_words(self):
        """Вывод количества подслов определенного слова"""
        return len(self.sub_words)
