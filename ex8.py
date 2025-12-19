import requests
import json
import time


response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
tokeninja = json.loads(response.text)['token']
timeninja = json.loads(response.text)['seconds']
print(f"Жди {timeninja} секунд")


response2 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params={'token': tokeninja})
statusninja = json.loads(response2.text)['status']

if statusninja == "Job is NOT ready":
    time.sleep(timeninja)

else:
    print("гейская ошибка")

response3 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params={'token': tokeninja})
statusninja2 = json.loads(response3.text)['status']
resultninja = json.loads(response3.text)['result']

if statusninja2 == "Job is ready" and resultninja in response3.text:
    print("Всё красиво")
else:
    print("гейская ошибка2")