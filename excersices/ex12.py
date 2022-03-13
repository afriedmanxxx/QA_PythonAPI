import requests
'''
Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_header
Этот метод возвращает headers с каким-то значением. Необходимо с помощью функции print() понять что за headers 
и с каким значением, и зафиксировать это поведение с помощью assert
Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py 
'''


def test_header_keys():
    response = requests.get("https://playground.learnqa.ru/api/homework_header")
    print(response.headers)
    assert 'Date' in response.headers, f"Expected header 'Date' is not found in {response.headers}"
    assert 'Content-Type' in response.headers, f"Expected header 'Content-Type' is not found in {response.headers}"
    assert 'Content-Length' in response.headers, f"Expected header 'Content-Length' is not found in {response.headers}"
    assert 'Connection' in response.headers, f"Expected header 'Connection' is not found in {response.headers}"
    assert 'Server' in response.headers, f"Expected header 'Server' is not found in {response.headers}"
