import requests

response = requests.get("http://playground.learnqa.ru/api/get_text")
print(response.text)
