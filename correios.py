#!/bin/python
import requests
import sys

trackingCode=str(sys.argv[1])

url = "https://api.linketrack.com/track/json?user=teste&token=1abcd00b2731640e886fb41a8a9671ad1434c599dbaa0a0de9a5aa619f29a83f&codigo=" + trackingCode
payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

jason = response.json()

events = jason['eventos']


for i in events:
    print(i['local'])
    print(i['data'])
    print(i['hora'])
    print("Status: ", i['status'])
    if i['subStatus'] != []:
        print("Substatus: ", i['subStatus'])
    print(' ')

if jason['servico']:
    print('Serviço:',jason['servico'])
