from scrapLinksJogos import Scrap_Link
from scrapTransmissoes import Scrap_Transmissao
import time


class Main():

    linkParaJogosBrasileirao = 'https://www.365scores.com/pt-br/football/brazil/brasileirao-serie-a/league/113'
    linkParaJogosCopaBr = 'https://www.365scores.com/pt-br/football/brazil/copa-do-brasil/league/115'
    linkParaJogosLibertadores = 'https://www.365scores.com/pt-br/football/south-america/libertadores/league/102'
    linkParaJogosBrasileiraoSerieB = 'https://www.365scores.com/pt-br/football/brazil/serie-b/league/116'
    linkParaJogosSulamericana = 'https://www.365scores.com/pt-br/football/south-america/copa-sudamericana/league/389'

    listaDoisLinks = []
    verificadorEncontrouLink = False
    while verificadorEncontrouLink == False:
        try:
            listaLinks = Scrap_Link().Montar_Link(linkParaJogosLibertadores)
            listaDoisLinks.append(listaLinks[0])
            listaDoisLinks.append(listaLinks[1])

            print(listaDoisLinks)
            verificadorEncontrouLink = True
            transmissoesSaida = Scrap_Transmissao().ExtrairTransmissao(listaDoisLinks)
        except IndexError as e:
            print('Erro de index =>', e)
            time.sleep(5)


if __name__ == '__main__':
    Main()
