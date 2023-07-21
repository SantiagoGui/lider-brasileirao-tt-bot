from selenium import webdriver
from selenium.webdriver.common.by import By

def takeLeader():
    browser = webdriver.Chrome()
    browser.get('https://ge.globo.com/futebol/brasileirao-serie-a/')

    leader = browser.find_elements(By.TAG_NAME, 'td')
    points = browser.find_elements(By.XPATH, '//*[@id="classificacao__wrapper"]/article/section[1]/div/table[2]/tbody/tr[1]/td[1]')

    textLeader = (leader[1].text)
    textPoints = (points[0].text)

    finalText =  ("Segue o lider da rodada, o gradioso " + textLeader + " que tem agora " + textPoints + " pontos 🔥 🚀 💪")
    return finalText

takeLeader()