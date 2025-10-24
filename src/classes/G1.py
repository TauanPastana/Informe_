from classes import Sites
import requests
from bs4 import BeautifulSoup
from classes.Noticias import Noticias
class G1(Sites):
    def __init__(self ):
        noticias = self.raspagem_g1()
        super().__init__(noticias, "G1")
    
    def raspagem_g1(self) -> dict:
        try:
            url = "https://g1.globo.com/ultimas-noticias/"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            noticias = soup.find_all('a', class_='feed-post-link gui-color-primary gui-color-hover')

            dict_noticias = {}
            for id, noticia in enumerate(noticias):
                dict_noticias[str(id)] = Noticias(str(id), noticia.text, noticia.get('href'))
            return dict_noticias
        except:
            print("Erro, tente novamente!")

    def update_atualizacao(self):
        self.noticias = self.raspagem_g1()

        


