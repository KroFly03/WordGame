from classes.game import Game

FILENAME = 'words.json'

print('Введите имя игрока')
user_name = input()

game = Game(user_name, FILENAME)

#print(game)

game.show_greetings()

while game.count_entered_words() < game.count_sub_words():
    user_input = input()
    if game.is_stopped(user_input):
        break

    if game.check_word(user_input):
        game.enter_word(user_input)

# Вывод результатов
print(f'Игра завершена, вы угадали {game.count_sub_words()} слов!')
