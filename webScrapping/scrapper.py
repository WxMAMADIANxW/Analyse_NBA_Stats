import requests

def getsite(url):
    
    response = requests.get(url)
    return response.status_code
    

if __name__ == '__main__':
    url = "https://www.basketball-reference.com/leagues/NBA_stats_per_game.html"
    print(getsite(url))