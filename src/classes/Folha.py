import requests
from bs4 import BeautifulSoup
from classes import Sites

class Folha(Sites):
    def __init__(self):
        dados = self.raspagem_folha()
        super().__init__(dados, "Folha de São Paulo")

    def raspagem_folha(self):
        url = "https://www1.folha.uol.com.br/ultimas-noticias/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        noticias = soup.find_all(class_='c-headline__content')
        dict_noticias = { noticia.h2.text: noticia.a['href']  for noticia in noticias}
        return dict_noticias