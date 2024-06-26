import requests
import numpy as np
import pandas as pd 

url = 'https://www.imdb.com/title/tt0072308/plotsummary/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}
response = requests.get(url, headers=headers)
 
# print('Status code: ', response.status_code)
# print('Text: ', response.text[:1000])

from bs4 import BeautifulSoup as bs
 
# Parse the HTML
soup = bs(response.text, 'html.parser')
 
# Extract any HTML tag
title = soup.find('div', {'class': 'ipc-html-content-inner-div'})
print(title)
