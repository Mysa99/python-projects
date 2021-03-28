import requests
import os
import json
import time

print('NOTE: Only the current version is specified atm.')
print('What version are you going to be on? \n1. latest\n2. Galactus\n')
ask = input('>> ')

if ask == '1':
    print('Loaded latest versions keychain.') 
#lif ask == '2':
#   print('Loaded travis (12.61)')
elif ask == '2':
    print('Loaded Galactus (14.60)')
    galactus = '1'
else:
    print('Unspecified number. (Enter a number between 1-1)')
    time.sleep(2)
    exit()

print('\nGrabbing keychain...')

if ask == '1':
    response = requests.get('https://api.nitestats.com/v1/epic/keychain')
elif ask == '2':
    response = requests.get('https://pastebin.com/raw/nimMBCVe')
    print('Grabbed galactus keychain!!!')
else:
    response = requests.get('https://api.nitestats.com/v1/epic/keychain')

x = response.json()

json_object = json.dumps(x, indent = 4)

with open('keychain.json', 'w') as f:
    json.dump(x, f, indent=4)

time.sleep(1)
print('\nDone!')
time.sleep(4)
