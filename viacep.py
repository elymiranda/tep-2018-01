# -*- coding: utf-8 -*-
import requests

cep = '64218100'
url = "https://viacep.com.br/ws/{cep}/json/"
url = url.format(cep=cep)

response = requests.get(url).json()
# print(response)

print(" Logradouro: %s \n Bairro: %s \n Localidade: %s \n UF: %s" %
      (response['logradouro'], response['bairro'], response['localidade'], response['uf']))