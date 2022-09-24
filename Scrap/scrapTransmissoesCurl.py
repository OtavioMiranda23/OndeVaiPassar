import requests

class Scrap_Transmissoes_Curl:
    def __init__(self):
        self.canaisTransmissores = []
        self.dictTimesTransmissoes = {}
        
    def extraiTransmissao(self, linkDinamico):
        try:
            for link in linkDinamico:
                self.canaisTransmissores = []
                self.headers = {
                'authority': 'webws.365scores.com',
                'accept': '*/*',
                'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'no-cache',
                'origin': 'https://www.365scores.com',
                'pragma': 'no-cache',
                'referer': 'https://www.365scores.com/',
                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            }
                self.response = requests.get(link, headers=self.headers)
                self.jsonFile = self.response.json()
                
                timeDaCasa = self.jsonFile['game']['homeCompetitor']['name']
                timeDeFora = self.jsonFile['game']['awayCompetitor']['name']
                confronto = timeDaCasa + ' x ' + timeDeFora
                arrayTransmissoes = self.jsonFile['game']['tvNetworks']

                for celula in arrayTransmissoes:
                    self.canaisTransmissores.append(celula['name'])

                self.dictTimesTransmissoes.update({
                    confronto: self.canaisTransmissores
                    })

            return self.dictTimesTransmissoes
        except KeyError as e:
            print('Jogo sem transmissao')
            return self.dictTimesTransmissoes