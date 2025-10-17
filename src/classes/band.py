from classes import Sites
import requests
from bs4 import BeautifulSoup

class Band(Sites):
    def __init__(self):
        noticias = self.raspagem_band()
        super().__init__(noticias, 'Band')
    
    def raspagem_band(self) -> dict:
        url = 'https://www.band.com.br/noticias'
        url = 'https://www.band.com.br/noticias'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        noticias = soup.find_all('div', class_='text-box__flex')
        dict_noticias = {}
        for id, noticia in enumerate(noticias):
            if id == 11:
                break
            dict_noticias[str(id)] = {"Noticias": noticia.text, "Link": noticia.a['href']} 
        return dict_noticias

