import requests

meow2 = "https://api.chucknorris.io/jokes/random"
meow3 = requests.get(meow2).json()
print(meow3["value"])