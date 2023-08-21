import json

from selenium import webdriver
from selenium.webdriver.common.by import By


import time

from hello.models import Player


def add_player_to_db(new_player):
    new_info = str(new_player["info"][0]) + new_player["info"][1]
    p = Player(last_name=new_player["last_name"], first_name=new_player["first_name"], info=new_player["info"], utr=new_player["utr"])
    p.save()


def getUtr(name, driver):
    time.sleep(1)

    searchBar = driver.find_element(By.XPATH, '//*[@id="myutr-app-wrapper"]/div[3]/nav/div[1]/div[2]/div/div[1]/div[1]/input')
    searchBar.send_keys(name)
    time.sleep(1)
    # click on "see all" or "search"
    driver.find_element(By.XPATH,
                        '//*[@id="myutr-app-wrapper"]/div[3]/nav/div[1]/div[2]/div/div[1]/div[2]/div/div/div[1]/a').click()
    time.sleep(1)

    #   @class='show-ellipsis d-block'
    cityElements = driver.find_elements(By.XPATH, "//*[@class='show-ellipsis d-block']")

    for i in range(0, len(cityElements)//2):
        ii = str(i + 1)
        xp = '//*[@id="myutr-app-body"]/div[1]/div[3]/div[2]/a[' + ii + ']/div/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]'
        print(cityElements[i*2].text, ' - ' , driver.find_element(By.XPATH, xp).text)

    # Delete name in the search bar to reset
    driver.find_element(By.XPATH, '//*[@id="myutr-app-wrapper"]/div[3]/nav/div[1]/div[2]/div/div[1]/div[1]/span[3]').click()

# info = [UTR, info_string]
def getFirstUtrScore(name, driver):
    info = [] # [0] is UTR (for sorting), and [1] is rest of the info
    try:
        time.sleep(1)

        searchBar = driver.find_element(By.XPATH, '//*[@id="myutr-app-wrapper"]/div[3]/nav/div[1]/div[2]/div/div[1]/div[1]/input')
        searchBar.send_keys(name)
        time.sleep(1)
        # click on "see all" or "search"
        driver.find_element(By.XPATH,
                            '//*[@id="myutr-app-wrapper"]/div[3]/nav/div[1]/div[2]/div/div[1]/div[2]/div/div/div[1]/a').click()
        time.sleep(1)

        #   @class='show-ellipsis d-block'
        cityElements = driver.find_elements(By.XPATH, "//*[@class='show-ellipsis d-block']")

        for i in range(0, 1):
            ii = str(i + 1)
            xp = '//*[@id="myutr-app-body"]/div[1]/div[3]/div[2]/a[' + ii + ']/div/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]'
            try:
                UTR = float(driver.find_element(By.XPATH, xp).text)
            except:
                UTR = 0
            print(name, ': ', cityElements[i*2].text, ' - ', driver.find_element(By.XPATH, xp).text)
            info_string = name + ': ' + cityElements[i*2].text + ' - ' + driver.find_element(By.XPATH, xp).text
            # separation_index = info_string.rfind('-')
            # info[0] = float(info_string[separation_index+3:])
            info = [UTR, info_string]


    except:
        info = [0.00, name]
        print(name, ': CANNOT FIND UTR INFO')

    # Delete name in the search bar to reset
    driver.find_element(By.XPATH, '//*[@id="myutr-app-wrapper"]/div[3]/nav/div[1]/div[2]/div/div[1]/div[1]/span[3]').click()
    return info

def runUniversalTennis(entry_list):
    PATH = "C:\Program Files (x86)\chromedriver.exe"

    driver = webdriver.Chrome()

    driver.get("https://app.universaltennis.com/login")

    # driver.implicitly_wait(0.5)
    # Log in form and click submit.
    driver.find_element(By.ID, "emailInput").send_keys("olivermliu1@gmail.com")
    driver.find_element(By.ID, "passwordInput").send_keys("D3GAyOEr5Vui")
    driver.find_element(By.XPATH, '//*[@id="myutr-app-body"]/div/div/div/div/div/div[2]/form/div[3]/button').click()

    driver.implicitly_wait(15)

    info_list = []
    for entry in entry_list:
        new_player = {
            "last_name": entry.split(', ')[0],
            "first_name": entry.split(', ')[1]
        }
        try:
            utr_res = getFirstUtrScore(entry, driver)
            new_player["utr"] = utr_res[0]
            new_player["info"] = utr_res[1]
            info_list.append(new_player)
            add_player_to_db(new_player)
        except:
            new_player["utr"] = 0.00
            new_player["info"] = ["Unable to Find UTR Profile"]
            info_list.append(new_player)
            add_player_to_db(new_player)
            print('CANNOT FIND UTR INFO: ', entry)
        print(new_player)
    print(info_list)
    # info_list.sort(reverse=True)
    # counter = 1
    # for info in info_list:
    #     print(counter, ') ', info[0] , ' - ', info[1])
    #     counter += 1

    return json.dumps(info_list)
