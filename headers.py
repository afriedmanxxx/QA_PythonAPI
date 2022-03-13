import requests

headers = {"some_header": "123"}
response =requests.get("https://playground.learnqa.ru/ajax/api/show_all_headers", headers=headers)

print(response.text)  # getting request headers
print(response.headers)  # getting response headers


