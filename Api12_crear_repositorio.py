import requests

# en este momento seguro no funcionara porque Github cambia el access token, hay que obtener el nuevo acess token

if __name__ == '__main__':
    client_id = '19945aad9d82142454dc'
    client_secret = 'c3e86150c5d33382a8973a878c872844d025a4f9'

    code = '4366197175c636baab47' 
    access_token = '05e62c00ce37fb517c0867a17829687f61e292c5'
    
    url = 'http://api.github.com/user/repos'
    payload = {'name': 'git_api_cf_comunidad'}
    headers = {'Accept': 'application/json', 'Authorization':'token'+ access_token}
    
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print (response.json())
    else:
        print(response.content)