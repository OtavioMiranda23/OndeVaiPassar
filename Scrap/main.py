from scrapLinksJogos import Scrap_Link
from scrapTransmissoes import Scrap_Transmissao
import time
from jsonConverter import Json_Converter
from construtorDeCurl import Contrutor_De_Curl
from scrapTransmissoesCurl import Scrap_Transmissoes_Curl

class Main():

    linkParaJogosBrasileirao = 'https://www.365scores.com/pt-br/football/brazil/brasileirao-serie-a/league/113'
    linkParaJogosCopaBr = 'https://www.365scores.com/pt-br/football/brazil/copa-do-brasil/league/115'
    linkParaJogosLibertadores = 'https://www.365scores.com/pt-br/football/south-america/libertadores/league/102'
    linkParaJogosBrasileiraoSerieB = 'https://www.365scores.com/pt-br/football/brazil/serie-b/league/116'
    linkParaJogosSulamericana = 'https://www.365scores.com/pt-br/football/south-america/copa-sudamericana/league/389'

    linksJogos = Scrap_Link().Montar_Link(linkParaJogosBrasileiraoSerieB)
    
    linkParcial = []
    i = 0
    while i < 5:
        linkParcial.append(linksJogos[i])
        i += 1


    linkCurl = Contrutor_De_Curl().extraiIds(linksJogos)

    transmissoesCurl = Scrap_Transmissoes_Curl().extraiTransmissao(linkCurl)

    print('Transmissoes pescadas => ', transmissoesCurl)

    Json_Converter('jsonScrap', 'Json_Transmissoes', transmissoesCurl).EscreveJsonFile()

    

    # listaDoisLinks = []
    # i = 0
    # verificadorEncontrouLink = False
    # while verificadorEncontrouLink == False & i < 8:
    #     try:
    #         listaLinks = Scrap_Link().Montar_Link(linkParaJogosCopaBr)
    #         listaDoisLinks.append(listaLinks[0])
    #         listaDoisLinks.append(listaLinks[1])

    #         print(listaDoisLinks)
    #         verificadorEncontrouLink = True
    #         transmissoesSaida = Scrap_Transmissao().ExtrairTransmissao(listaDoisLinks)

    #     except IndexError as e:
    #         print('Erro de index nos links iniciais =>', e)
    #         time.sleep(5)
    #         i += 1

    #     transmissoesJson = Json_Converter(
    #         'jsonScrap', 'Json_Transmissoes', transmissoesSaida)
    #     transmissoesJson.EscreveJsonFile()


if __name__ == '__main__':
    Main()
