from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Scrap_Link:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--incognito')
        # self.options.add_argument('--headless')
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        self.options.add_argument(f'user-agent={self.user_agent}')
        self.driver = webdriver.Chrome(
            "/Users/otaviomaior/Documents/chromedriver", chrome_options=self.options)
        self.wait = WebDriverWait(self.driver, 15)
        self.links = []

    def Montar_Link(self, linkParaListaDeJogos):

        self.driver.get(
            linkParaListaDeJogos)

        fecha_cookie = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.ID, 'didomi-notice-agree-button')))
        fecha_cookie.click()

        time.sleep(2)

        seletorJogo = self.driver.find_elements(
            by=By.CLASS_NAME, value=("game-card_game_card_link__3Y9HN "))

        for jogo in seletorJogo:
            linkCadaJogo = jogo.get_attribute("href")
            self.links.append(linkCadaJogo)

        self.driver.close()
        print(self.links)
        return self.links
