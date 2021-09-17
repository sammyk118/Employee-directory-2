import requests

def load_rand():
    response = requests.get("https://randomuser.me/api/?results=10&inc=gender,name&format=json&noinfo&nat=us")
    return response.json()