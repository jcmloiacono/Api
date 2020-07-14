import requests

# en este momento seguro no funcionara porque Github cambia el access token, hay que obtener el nuevo acess token

if __name__ == '__main__':
    client_id = #buscar en archivo
    client_secret = #buscar en archivo

    code = #buscar en archivo
    access_token = #buscar en archivo
    
    url = 'http://api.github.com/user/repos'
    payload = {'name': 'git_api_cf_comunidad'}
    headers = {'Accept': 'application/json', 'Authorization':'token'+ access_token}
    
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print (response.json())
    else:
        print(response.content)