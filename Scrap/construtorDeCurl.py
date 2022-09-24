class Contrutor_De_Curl:
    def __init__(self):
        self.listaDeLinksDinamicos = []
    def extraiIds(self, listaDeLinks):
        for link in listaDeLinks:
            linkSeparado = link.split('/')
            ultimaChave = linkSeparado[-1]
            ultimaChaveSeparada = ultimaChave.split('#')

            matchupId = ultimaChaveSeparada[0]
            gameId = ultimaChaveSeparada[1]

            tamanhoGameId = len(gameId)
            gameId = gameId[3: tamanhoGameId]

            linksDinamico = f"https://webws.365scores.com/web/game/?appTypeId=5&langId=31&timezoneName=Etc/GMT+3&userCountryId=21&gameId={gameId}&matchupId={matchupId}"
            self.listaDeLinksDinamicos.append(linksDinamico)
        return self.listaDeLinksDinamicos
