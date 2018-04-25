import requests

url = 'https://jsonplaceholder.typicode.com/todos/'
dados = {
    "userId": 1,
    "title": 'Prepare class notes',
    "completed": False
}

response = requests.post(url, data = dados)
print(response.json())

response = requests.delete(url + '/210')
# 404
print(response)

