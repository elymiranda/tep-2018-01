import requests

key = 'sua outra chave'
localizacao = "Avenida frei serafim"
url = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (localizacao, key)
response = requests.get(url)
json = response.json()
print (json)
latitude = json['results'][0]['geometry']['location']['lat']
longitude = json['results'][0]['geometry']['location']['lng']

print('Latitude: %f  - Longitude: %f' % (latitude, longitude ))