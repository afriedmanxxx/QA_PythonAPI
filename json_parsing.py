import json

string_as_json_format = '{"answer": "Hello, Urser"}'
obj = json.loads(string_as_json_format)

key = "answer"

if key in obj:
    print(obj[key])
else:
    print(f"No such key {key} is found in Json.")
