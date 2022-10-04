class Player:
    def __init__(self, user_name):
        self.user_name = user_name
        self.entered_words = []

    def __repr__(self):
        entered_words = ', '.join(self.entered_words)
        return f"Введенные слова пользователем {self.user_name}: {entered_words}"

    def count_entered_words(self):
        """Вывод количества правильно введенных пользователем слов"""
        return len(self.entered_words)

    def enter_word(self, word):
        """Добавление слова в список введенных пользователем подслов"""
        self.entered_words.append(word)

    def is_entered(self, word):
        """Проверка на наличие данного слова в списке введенных пользователем подслов"""
        return word in self.entered_words
