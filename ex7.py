import requests

payload = ['GET', 'POST', 'PUT', 'DELETE']

# 1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(response.text)
response = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(response.text)
# Wrong method provided

# 2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params={"method": "HEAD"})
print(response.text)
# Wrong method provided

# 3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params={"method": "GET"})
print(response.text)
# {"success":"!"}

# 4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений
#  параметра method. Например с GET-запросом передает значения параметра method равное
#  ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее.
for i in payload:
    print(f"Method is: {i}")
    response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params={"method": i})
    print(f"get call: {response.text}")

    response = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type', data={"method": i})
    print(f"post call: {response.text}")

    response = requests.put('https://playground.learnqa.ru/ajax/api/compare_query_type', data={"method": i})
    print(f"put call: {response.text}")

    response = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type', data={"method": i})
    print(f"delete call: {response.text}")


