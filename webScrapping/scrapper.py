import requests
from bs4 import BeautifulSoup as bs

url = "https://www.basketball-reference.com/leagues/NBA_stats_per_game.html"
response =  requests.get(url)
print('coi')
