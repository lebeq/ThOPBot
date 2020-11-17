import requests

r = requests.get('http://theoldreader.com/kittens/600/400')

print(r.url)
