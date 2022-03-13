import pytest

'''
В рамках этой задачи с помощью pytest необходимо написать тест, который просит ввести 
в консоли любую фразу короче 15 символов. А затем с помощью assert проверяет, 
что фраза действительно короче 15 символов.
Чтобы в переменную получить значение, введенное из консоли, необходимо написать вот такой код:
phrase = input("Set a phrase: ")
Внимание, чтобы pytest не игнорировал команду ввода с клавиатуры, запускать тест нужно с 
ключиком "-s": python -m pytest -s my_test.py 
'''
phrase = input("Set a phrase: ")


def test_phrase_is_15_or_less(phrase=phrase):
    assert len(phrase) < 15, f"Phrase: {phrase}  - is too long and " \
                             f"has {len(phrase)} characters."



