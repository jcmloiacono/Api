import requests

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon/1/'
    response = requests.get(url)
    print (response)
    
    if response.status_code == 200:
        response_json = response.json()
        name = response_json['name']
        print (name)