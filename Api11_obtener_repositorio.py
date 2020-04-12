import requests

client_id = '19945aad9d82142454dc'
client_secret = 'c3e86150c5d33382a8973a878c872844d025a4f9'

code = '4366197175c636baab47' 
access_token = '05e62c00ce37fb517c0867a17829687f61e292c5'

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