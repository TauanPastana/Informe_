import requests
from bs4 import BeautifulSoup
from datetime import datetime
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from datetime import datetime

def raspagem_G1(url):
    noticias = {"titulo": "", "descricao": "", "imagem": "", "publicado_em": None, "url": url}
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()  # levanta erro em 4xx/5xx
    except RequestException:
        return None

    try:
        soup = BeautifulSoup(response.content, "html.parser")

    
        data = soup.find("p", class_="content-publication-data__updated")
        if data:
            time_el = data.find("time", itemprop="datePublished")
            if time_el and time_el.get("datetime"):
                try:
                    noticias["publicado_em"] = datetime.fromisoformat(time_el.get("datetime"))
                except ValueError:
                    return None
        else:
            return None
        
        titulo_el = soup.find("h1", class_="content-head__title")
        if not titulo_el:
            return None

        titulo_text = titulo_el.get_text(strip=True)
        if not titulo_text:
            return None

        # valida o texto extraído (não o dict ainda vazio)
        titulo_text = titulo_text.strip()
        if not titulo_text:
            return None

        noticias["titulo"] = titulo_text


            # descrição pode não existir
        desc_el = soup.find("div", class_="medium-centered subtitle")
        noticias["descricao"] = desc_el.get_text(strip=True) if desc_el else ""


        figure = soup.find("figure", class_="content-media-figure")
        if figure:
            amp_img = figure.find("amp-img")
            if amp_img and amp_img.get("src"):
                noticias["imagem"] = amp_img.get("src")

        return noticias

    except Exception:
        return None

def noticias_G1() -> list:
    url_g1 = "https://g1.globo.com/ultimas-noticias/"
    response = requests.get(url_g1)
    soup = BeautifulSoup(response.content, 'html.parser')
    noticias = soup.find_all('a', class_='feed-post-link gui-color-primary gui-color-hover')
    urls = [url.get('href') for url in noticias]
    lista_noticias =[]

    for url in urls:
        noticia = raspagem_G1(url)
        if noticia is None:
            continue
        lista_noticias.append(noticia)

        
    
    return lista_noticias

dict_noticias = noticias_G1()
for url in dict_noticias:
    print(url['url'], "\n", url['publicado_em'])









        


