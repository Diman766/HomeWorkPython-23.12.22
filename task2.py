import requests
from bs4 import BeautifulSoup

url = ''
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
mass = soup.find_all(class_='')
print(mass)
string = str(soup.find_all(class_=''))
print(string[string.find('>')+1:string.find('</div>'):].replace(',','.'))