from Classes import Sites
import requests
from bs4 import BeautifulSoup
class G1(Sites):
    def __init__(self ):
        noticias = self.raspagem_g1()
        super().__init__(noticias)
    
    def raspagem_g1(self) -> dict:
        url = "https://g1.globo.com/ultimas-noticias/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        noticias = soup.find_all('a', class_='feed-post-link gui-color-primary gui-color-hover')
        dict_noticias = {"G1":
                    {noticia.text: noticia.get('href') for noticia in noticias}
                    }
        return dict_noticias

