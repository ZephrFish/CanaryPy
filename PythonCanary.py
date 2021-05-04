import requests

    data = {
        'auth_token': 'AUTHTOKEN',
        'memo': 'MESSAGEHERE',
        'kind': 'http'
        }
    
    response = requests.post('https://YOURDOMAIN.canary.tools/api/v1/canarytoken/create', data=data)
