import requests
'''
С помощью конструкции response.history необходимо узнать, 
сколько редиректов происходит от изначальной точки назначения до итоговой. И какой URL итоговый.
Ответ опубликуйте в виде ссылки на коммит со скриптом, а также укажите 
количество редиректов и конечный URL.
'''

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
print(response.status_code)
response_urls = [response.history[i].url for i in range(len(response.history))]
print(response_urls)
print(f" The amount of redirects is {len(response_urls)} and the final URL is: {response_urls[-1]}")

