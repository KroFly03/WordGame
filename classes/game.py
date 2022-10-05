from classes.player import Player
from tools.utils import get_random_word


class Game:
    FILENAME = 'words.json'

    print('Введите имя игрока')
    user_name = input()

    player = Player(user_name)
    basic_word = get_random_word(FILENAME)

    print(basic_word)
    print(f'Привет {player.user_name}! \
                  \nСоставьте {basic_word.count_sub_words()} слов из слова {basic_word.word} \
                  \nСлова не должны быть короче 3 букв \
                  \nЧтобы закончить игру, угадайте все слова или напишите "stop" \
                  \nПоехали, ваше первое слово?')

    while player.count_entered_words() < basic_word.count_sub_words():
        user_input = input().lower()
        if user_input in ['stop', 'стоп']:
            break

        elif len(user_input) < 3:
            print('Слишком короткое слово')

        elif not basic_word.is_sub_words(user_input):
            print('Неверно')

        elif player.is_entered(user_input):
            print('Уже использовано')

        elif basic_word.is_sub_words(user_input):
            print('Верно')
            player.enter_word(user_input)

    print(f'Игра завершена, вы угадали {player.count_entered_words()} слов!')