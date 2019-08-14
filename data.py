from bs4 import BeautifulSoup
import numpy as np
import requests
from selenium import webdriver

#driver = webdriver.Chrome()
#driver.get('https://www.espn.com/college-football/scoreboard')
#html = driver.page_source
#soup = BeautifulSoup(html)

page = open('Webpages\scoreboard.html', encoding = 'utf8').read()
soup = BeautifulSoup(page,'lxml')
for tag in soup.find_all('a')
print(sheesh)

#print(gamecast)
#games = soup.find_all('div',{'class':'game'})
#print(game) 
#for game in games:
    #for team in game.find_all('a'):
        #print(team.get('href'))
