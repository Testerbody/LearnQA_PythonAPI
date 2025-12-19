import requests

response = requests.post("http://playground.learnqa.ru/api/check_type2", data={"text": "Hello, User"})
print(response.status_code
      )