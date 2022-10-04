from classes.player import Player
from classes.basic_word import BasicWord
from tools.utils import get_random_word


class Game(Player, BasicWord):

    def __init__(self, player, filename):
        self.player = Player(player)
        self.basic_word = get_random_word(filename)

    def __repr__(self):
        return f'Пользователь: {self.player} Слово: {self.basic_word}'

    def check_word(self, user_word):
        """Валидация введенного пользователем слова"""
        if len(user_word) < 3:
            print('Слишком короткое слово')
            return False

        if not self.basic_word.is_sub_words(user_word):
            print('Неверно')
            return False

        if self.player.is_entered(user_word):
            print('Уже использовано')
            return False

        if self.basic_word.sub_words.is_sub_words(user_word):
            print('Верно')
            return True

        return False

    def is_stopped(self, user_input):
        """Проверка на законченность цикла"""
        return user_input in ['stop', 'стоп']

    def show_greetings(self):
        print(f'Привет {self.player.user_name}! \
              \nСоставьте {self.basic_word.count_sub_words()} слов из слова {self.basic_word.show_word()} \
              \nСлова не должны быть короче 3 букв \
              \nЧтобы закончить игру, угадайте все слова или напишите "stop" \
              \nПоехали, ваше первое слово?')
