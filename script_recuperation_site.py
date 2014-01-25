
from bs4 import BeautifulSoup
import urllib.request
import webbrowser

print('Salut')

page=urllib.request.urlopen('http://python.org')


soup = BeautifulSoup(page)
print(soup.prettify())



