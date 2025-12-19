import requests

response = requests.get('https://playground.learnqa.ru/api/long_redirect')
first = response.history[0]
two = response.history[1]
three = response.history[2]

all = response.history


print(first.url)
print(two.url)
print(three.url)
print(response.url)
print(all)