import requests
import json

def pokemon(url='http://pokeapi.co/api/v2/pokemon-form', offset=0):
    args ={'offset' : offset} if offset else {}
    
    response =requests.get(url, params=args)
    
    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results', [])
        
        if results:
            name = ''
            for i in results:
                name += i['name']+ " "
        print (name)
        next = input("¿Continuar Listando? S/N")
        if next == 's':
            pokemon(offset=offset+20)

if __name__ == '__main__':
    url = 'http://pokeapi.co/api/v2/pokemon-form'
    pokemon()

