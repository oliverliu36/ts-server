import json

from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def getPlayers(page):
    # headless, which means the browser won't pop up from the screen!
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    # driver = webdriver.Chrome()
    driver.get(page)

    time.sleep(3) # Wait for webpage to load

    # get each row (some rows are not player info. We filter those out)
    rows = driver.find_elements(By.XPATH, '//tr')
    #the text in each row
    rows_text = []
    for row in rows:
        try:
            rows_text.append(row.text)
        except:
            print('invalid row')


    players = []
    for text in rows_text: # some rows don't indicate a "player" so we pass
        try:
            ind = text.index("Men's Open Singles")
            players.append(text[:ind-1])
        except:
            pass
    print(players)
    print(len(players))
    return json.dumps(players)
    # return players
# url = 'https://playtennis.usta.com/Competitions/texasamuniversity/Tournaments/players/04E68AD1-68B6-4771-943D-212AAAD15B81'
# getPlayers(url)
