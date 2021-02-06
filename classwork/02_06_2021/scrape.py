import requests
from requests import Response

url: str = "http://www.webscrapingfordatascience.com/basichttp/"
r: Response = requests.get(url)

print(r.text)

