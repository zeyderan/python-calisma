import requests
import json
# hata yoka response 200 döner
result = requests.get('https://jsonplaceholder.typicode.com/todos')

print(type(result)) #<class 'requests.models.Response'>

result = result.text # string döner

print(type(result)) # <class 'str'>

result = json.loads(result) # jsondan dictionary dönüşümü yapar




