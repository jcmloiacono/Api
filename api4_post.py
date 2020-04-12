import requests
import json

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = { 'nombre': 'Eduardo', 'curso': 'Python', 'nivel': 'intermedio'}
    
    response = requests.post(url, json=payload) # aqui enviamos los argumetos al atributo data
    print(response.url)
    
    if response.status_code == 200:
        
        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(response.content)