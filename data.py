from bs4 import BeautifulSoup
import numpy as np
import requests

r = requests.get('https://www.espn.com/college-football/scoreboard')
soup = BeautifulSoup(r.text,'lxml')
divs = soup.find_all('div')
for div in divs:
    print(div.find_all('section'))

#print(gamecast)
#games = soup.find_all('div',{'class':'game'})
#print(game) 
#for game in games:
    #for team in game.find_all('a'):
        #print(team.get('href'))
