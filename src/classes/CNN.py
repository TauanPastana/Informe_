from classes import Sites
import requests
from bs4 import BeautifulSoup
class CNN(Sites):
    def __init__(self ):
        noticias = self.raspagem_cnn()
        super().__init__(noticias, "CNN")
    
    def raspagem_cnn(self) -> dict:
        url = "https://www.cnnbrasil.com.br/ultimas-noticias/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        Noticias = soup.find_all('div', class_="flex flex-col gap-4")
        # dict_noticias = { noticia.h2.text: noticia.a['href']  for noticia in Noticias}
        dict_noticias = {}
        for id, noticia in enumerate(Noticias):
            dict_noticias[id] = {noticia.text: noticia.a['href']}
        return dict_noticias