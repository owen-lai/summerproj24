import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer as ss
from concurrent.futures import ThreadPoolExecutor

df = pd.read_csv('movies.csv')

moviesIds = df['tconst'].tolist()

# print(moviesIds[:5]) 

urls = ["https://www.imdb.com/title/" + s + "/plotsummary/" for s in moviesIds]

# print(urls[:5]) 
# url = 'https://www.imdb.com/title/tt0072308/plotsummary/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}
only_sum_tags = ss('div', {'class': 'ipc-html-content-inner-div'})
# for i in urls[:5]:
#     response = requests.get(i, headers=headers)
 
# # print('Status code: ', response.status_code)
# # print('Text: ', response.text[:1000])
 
# # Parse the HTML
#     soup = bs(response.text, 'lxml', parse_only=only_sum_tags)
    
# # Extract any HTML tag
#     title = soup.find('div', {'class': 'ipc-html-content-inner-div'})
#     summaries.append(title)
#     #print(title)

def scrape(url):
    response = requests.get(url, headers=headers)
    soup = bs(response.text, 'lxml', parse_only=only_sum_tags)
    title = soup.find('div', {'class': 'ipc-html-content-inner-div'})
    return {url: title}

with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(scrape, urls))

combined_results = {}
for result in results:
    combined_results.update(result)

for url, data in combined_results.items()[:5]:
    print(f'{url}: {data}')
