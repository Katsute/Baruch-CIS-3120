import requests
from requests import Response

url: str = "https://en.wikipedia.org/wiki/Pet"
r: Response = requests.get(url)
html: str = r.text

pets: list[str] = ["cats", "dogs", "snakes", "fish", "bird", "monkey", "iguana"]

for pet in pets:
    pet: str
    print(f"{pet} : {html.count(pet)} mentions")

