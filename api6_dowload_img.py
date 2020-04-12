import requests
import json

if __name__ == '__main__':
    url = 'http://i.imgur.com/n9z3sLg.jpg'
    response = requests.get(url, stream = True) # realiza la peticion al servidor y lo deja abierto
    with open('image.jpg', 'wb') as file:
        for i in response.iter_content(): # Descarga el contenido poco a poco
            file.write(i)
    
    response.close
  
    
    