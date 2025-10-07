from classes import Sites
import requests
from bs4 import BeautifulSoup
class Uol(Sites):
    def __init__(self):
        noticias = self.raspagem_uol()
        super().__init__(noticias, "UOL")

    def raspagem_uol(self) -> dict:
        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}
        url = "https://noticias.uol.com.br/ultimas/"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        noticias = soup.find_all('div', class_="thumbnails-wrapper")
        dict_noticias = {}
        for id, noticia in enumerate(noticias):
            dict_noticias[str(id)] = {"Noticias": noticia.text, "Link": noticia.a['href']}
        return dict_noticias
    def update_atualizacao(self):
        self.noticias = self.raspagem_uol()