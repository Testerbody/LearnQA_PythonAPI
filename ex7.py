import requests



response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")

response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "HEAD"})

response3 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "POST"} )

response4 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})

response5 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "PUT"})

response6 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "DELETE"})

print(response.text)
print(response.status_code)
print(response2.text)
print(response2.status_code)
print(response3.text)
print(response3.status_code)
print(response4.text)
print(response4.status_code)
print(response5.text)
print(response5.status_code)
print(response6.text)
print(response6.status_code)