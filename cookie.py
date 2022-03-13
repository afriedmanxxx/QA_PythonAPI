import requests

# Cookie is used for a few things, ex: authorization. Remember user info, track action on website.
# Reguest can get and send kookies from backend

payload = {"login": "secret_login", "password": "secret_pass"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

cookie_value = response1.cookies.get("auth_cookie")
cookies = {}
if cookie_value is not None:
    cookies.update({"auth_cookie": cookie_value})

print(response1.text), print(response1.status_code)
print(dict(response1.cookies))
print(response1.headers)

response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
print(response2.text)
