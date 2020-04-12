import requests

client_id = '19945aad9d82142454dc'
client_secret = 'c3e86150c5d33382a8973a878c872844d025a4f9'
code = '4366197175c636baab47' # hay que estar pendiente de actualizar porque varia 
# (averiguar como hacer para que no varie )
access_token = '05e62c00ce37fb517c0867a17829687f61e292c5'

# https://github.com/login/oauth/authorize?client_id=19945aad9d82142454dc&scope=respo   ## se copia desde github
#https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/


if __name__ == '__main__':
    url = 'https://github.com/login/oauth/access_token'
    payload = {'client_id': client_id, 'client_secret': client_secret, 'code':code}
    headers = {'Accept' : 'application/json'}
    
    response= requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        response_json = response.json()
        
        access_token = response_json["access_token"]
        print (access_token)

