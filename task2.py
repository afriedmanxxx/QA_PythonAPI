import requests

#В проекте создать скрипт, который отправляет GET-запрос по адресу: https://playground.learnqa.ru/api/get_text
#Затем с помощью функции print вывести содержимое текста в ответе на запрос.
# Когда скрипт будет готов - давайте его закоммитим в наш репозиторий.
#Результатом должна быть ссылка на коммит.

link = "https://playground.learnqa.ru/api/hello"
payload = {"name": "User"}
response = requests.get(link, params=payload)
print(response.text)
