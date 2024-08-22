import sys
import requests
import textwrap
from bs4 import BeautifulSoup

numArgs = len(sys.argv)
itemNum = input("Input item #: ")

r = requests.get(f'https://scp-wiki.wikidot.com/scp-{itemNum}/')
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find('div', id='page-content')
lines = s.find_all('p')

line = []
w = textwrap.TextWrapper(width=150, break_on_hyphens=True, initial_indent='\n')

for line in lines:
    print(w.fill(line.text))