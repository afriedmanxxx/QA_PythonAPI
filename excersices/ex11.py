import requests
'''
Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_cookie
Этот метод возвращает какую-то cookie с каким-то значением. Необходимо с помощью функции print() понять что 
за cookie и с каким значением, и зафиксировать это поведение с помощью assert
Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py 
'''


def test_cookie():
    response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
    print(response.cookies.values())
    print(response.cookies.keys())
    print(response.cookies)

    assert 'HomeWork' in response.cookies, f"The key 'HomeWork' is not in {response.cookies} "

