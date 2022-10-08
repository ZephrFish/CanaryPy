import requests

DOMAIN = ''

data = {
        'auth_token': 'AUTHTOKEN',
        'memo': 'MESSAGEHERE',
        'kind': 'http'
        }
headers = {
    'User-Agent': 'NotMalware'
}
    
response = requests.post(f'https://{DOMAIN}.canary.tools/api/v1/canarytoken/create', data=data, headers=headers)
print(response)
