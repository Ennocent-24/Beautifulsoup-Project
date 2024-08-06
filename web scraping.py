#!usr/bin/env python3
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.nelsonmandelabay.gov.za/news').text
print(html_text)
