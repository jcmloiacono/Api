import requests

if __name__ == "__main__":
    url = 'https://api.github.com/user'

    session = requests.session()
    session.auth= (#'xxxxxx@gmail.com','claveXXX')
    
    response = session.get(url)
    if response.ok:
        response = session.get('https://github.com/jcmloiacono')
        if response.ok:
            print (response.content)
            print(response.cookies)
    else:
        print("no esta llendo bien", response.content)
