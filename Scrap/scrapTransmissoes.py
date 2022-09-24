import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Scrap_Transmissao:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--incognito')
        # self.options.add_argument('--headless')
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        self.options.add_argument(f'user-agent={self.user_agent}')
        self.driver = webdriver.Chrome(
            "/Users/otaviomaior/Documents/chromedriver", chrome_options=self.options)
        # self.driver.maximize_window()

        # self.wait = WebDriverWait(self.driver, 10)
        self.dictTransmissoes = {}
        self.verificadorEncontrouTransimissao = False

    def ExtrairTransmissao(self, links):
        i = 0
        while self.verificadorEncontrouTransimissao == False & i < 5:
            try:

                for link in links:
                    self.arrayTransmissoes = []
                    self.driver.get(link)
                    time.sleep(5)
                    # self.driver.execute_script(
                    #     "window.scrollTo(0, document.body.scrollHeight);")
                    # time.sleep(5)
                    containerTransmissoes = self.driver.find_elements(
                        by=By.CLASS_NAME, value="game-info-module-tv-network-container")
                    selecaoEquipes = self.driver.find_elements(
                        by=By.CLASS_NAME, value="breadcrumbs_last_item__2JZpf")

                    for transmissao in containerTransmissoes:
                        time.sleep(3)

                        transmissoes = transmissao.get_attribute("textContent")
                        transmissoes.encode('utf-8')
                        self.arrayTransmissoes.append(transmissoes)

                    equipes = selecaoEquipes[0].get_attribute("textContent")
                    equipes.encode('utf-8')
                    # print('Lista de transmissoes =>', self.arrayTransmissoes)
                    self.dictTransmissoes.update(
                        {equipes: self.arrayTransmissoes})
                    # print("Dicionario =>", self.dictTransmissoes)
                    # if link != links[-1]:

                # textoTransmissoes = containerTransmissoes[0].get_attribute("textContent")
                self.driver.close()
                print(self.dictTransmissoes)
                self.verificadorEncontrouTransimissao = True
                return self.dictTransmissoes
            except IndexError as e:
                print('Erro de index na transmissao =>', e)
                i += 1
