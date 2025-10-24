from classes import Sites
import requests
from bs4 import BeautifulSoup

from classes.Noticias import Noticias

class Band(Sites):
    def __init__(self):
        noticias = self.raspagem_band()
        super().__init__(noticias, 'Band')
    
    def raspagem_band(self) -> dict:
        try:
            url = 'https://www.band.com.br/noticias'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            noticias = soup.find_all('div', class_='text-box__flex')
            dict_noticias = {}
            for id, noticia in enumerate(noticias):
                if id == 11:
                    break
                dict_noticias[str(id)] = Noticias(str(id), noticia.text, noticia.a['href'] )
            return dict_noticias
        except:
            print("Erro, tente novamente!")
    
    def update_atualizacao(self):
        return self.raspagem_band()
    

