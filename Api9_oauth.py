import requests

client_id = #buscar en archivo
client_secret = #buscar en archivo
code = '4366197175c636baab47' # hay que estar pendiente de actualizar porque varia 
# (averiguar como hacer para que no varie )
access_token = #buscar en archivo

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

