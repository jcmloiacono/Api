import requests

client_id = #buscar en archivo
client_secret = #buscar en archivo

code = #buscar en archivo
access_token = #buscar en archivo

# https://github.com/login/oauth/authorize?client_id=19945aad9d82142454dc&scope=respo   ## se copia desde github
#https://developer.github.com/v3/repos/#get


if __name__ == '__main__':
    url = 'http://api.github.com/user/repos'
    headers ={'Authorization': 'token 05e62c00ce37fb517c0867a17829687f61e292c5'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        payload =response.json()
        
        for i in payload:
            name = i ['name']
            print(name)
    else:
        print(response.content)