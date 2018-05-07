# coding: utf-8
import requests, json
key = 'sua chave'
q = 'Prezados, boa tarde, gerem uma chave para a API.'
target = 'en'

url = 'https://translation.googleapis.com/language/translate/v2'
params = {'key':key, 'q':q, 'target':target}

response = requests.get(url, params=params)
'''
print(response.json())
{'data': {'translations': [{'detectedSourceLanguage': 'pt',
    'translatedText': 'Dear, good afternoon, generate a key to the API..'}]}}
'''

json = response.json()
print(json['data']['translations'][0]['translatedText'])




