from Classes import Sites
import requests
from bs4 import BeautifulSoup
class CNN(Sites):
    def __init__(self ):
        noticias = self.raspagem_cnn()
        super().__init__(noticias)
    
    def raspagem_cnn(self) -> dict:
        url = "https://www.cnnbrasil.com.br/ultimas-noticias/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        Noticias = soup.find_all( class_="text-gray-950 hover:underline")
        dict_noticias = {"CNN ": { noticia.h2.text: noticia.a['href']  for noticia in Noticias}}
        return dict_noticias