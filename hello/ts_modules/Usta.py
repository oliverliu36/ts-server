import json
import os


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time



def getPlayers(page):
    # Uncomment For Deploy VV
    service = Service(executable_path=os.environ.get("CHROMEDRIVER_PATH"))

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    # options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

    # Uncomment For Deploy VV
    driver = webdriver.Chrome(service=service, options=options)

    # Comment out for deploy VV
    # driver = webdriver.Chrome()
    driver.get(page)

    time.sleep(3) # Wait for webpage to load
    # ^^^ SET UP WEBDRIVER ^^^ ------------------------------------------------------------------------------------

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
