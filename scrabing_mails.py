import requests
import json

url = 'https://katalog.trojmiasto.pl/_ajax/obfuscator/?decode'

with open('quotes.json', 'r') as f:
    quotes_dist = json.load(f)

output = open("mails.txt", "a")
for quote in quotes_dist:
    if quote['data-hash']:
        hashData = quote['data-hash'][0]
        if hashData is not None:
            payload = { 'hash': hashData, 'type':'katalog'}
            response = requests.post(url,data=payload)
            content = json.loads(response.text)
            if content['success'] == True:
                write = {'title': quote['title'], 'mail': content['phrase']}
                output.write(json.dumps(write))
                output.write('\n')

output.close()

    
# myobj = { 'hash': 'YToyOntpOjA7czo0NDoibmlTN0FybytWRU8yNzA2aUtBdGx5UnVUS3ZnVS9SSlRFbWZvemNuWmxWTT0iO2k6MTtzOjE2OiJw1XZOtqRz2ZUN2kqVF9PQIjt9', 'type': 'katalog' }

# x = requests.post(url, data = myobj)
#
# print(x.text)
