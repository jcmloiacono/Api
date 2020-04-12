import requests
import json

if __name__ == '__main__':
    url = 'http://httpbin.org/put'
    payload = { 'nombre': 'Eduardo', 'curso': 'Python', 'nivel': 'intermedio'}
    headers = { 'Conten-Type':'application/json'} # para enviar encabezados
    
    
    response = requests.put(url, json=payload, headers=headers) # aqui enviamos los argumetos al atributo data
    print(response.url)
    
    if response.status_code == 200:
        
        headers_response = response.headers 
        server = headers_response['Server']
        print (server)

''' LOS PRINCIPALES CUATRO METODOS DE HTTP

GET PARA LLAMARLO
POST PARA CREARLO
PUT PARA ACTUALIZARLO
DELETE PARA ELIMINARLO '''