import random
import json
import os
from classes.basic_word import BasicWord


def load_data(filename):
    """Загрузка данных"""
    path = os.path.join('resources', 'data', filename)
    with open(path, mode='r', encoding='utf-8') as words:
        data = json.loads(words.read())

    return data


def get_random_word(filename):
    """Получение случайного слова"""
    data = load_data(filename)

    word = random.choice(data)

    basic_word = BasicWord(word['word'], word['subwords'])

    return basic_word
