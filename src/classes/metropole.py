from classes import Sites
import requests
from bs4 import BeautifulSoup

class Metropole(Sites):
    def __init__(self):
        noticia = self.raspagem_metropole()
        super().__init__(noticia, 'Metrópole')

    def raspagem_metropole(self):
        url = "https://www.metropoles.com/ultimas-noticias"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        resultados = soup.find_all('h5', class_=['gPeQDL'])
        head = soup.select('h2.hUlAQB')
        dict_noticias = {}
        for id, noticia in enumerate(resultados):
            if id == 0:
                dict_noticias[str(id)] = {"Noticias": head[0].text, "Link": head[0].a['href']}
            dict_noticias[str(id)] = {"Noticias": noticia.text, "Link": noticia.a['href']}
        return dict_noticias
    
    def update_atualizacao(self):
        self.noticias = self.raspagem_metropole()
    
