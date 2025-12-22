import requests

from bs4 import BeautifulSoup
from datetime import datetime

def links() -> list:
    url = 'https://www.cnnbrasil.com.br/ultimas-noticias/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    urls = soup.find('ul', class_='lg:mt-2').find_all('a', class_='flex shrink-0 items-center')
    urls = [url.get('href') for url in urls]
    return urls


def raspagemCNN(url) -> dict | None:

    noticias = {
        "titulo": "",
        "descricao": "",
        "imagem": "",
        "publicado_em": None,
        "url": url,
    }

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        # --- título (obrigatório) ---
        titulo_tag = soup.find("h1", class_="font-bold text-3xl lg:text-4xl")
        if not titulo_tag or not titulo_tag.get_text(strip=True):
            return None
        noticias["titulo"] = titulo_tag.get_text(strip=True)

        # --- data (obrigatória) ---
        time_tag = soup.find("time", class_="text-sm font-normal text-neutral-400")
        if not time_tag:
            return None

        data_iso = time_tag.get("datetime")
        if not data_iso:
            return None

        # Python 3.11+ aceita "Z" direto; fallback para versões anteriores
        try:
            dt = datetime.fromisoformat(data_iso)
        except ValueError:
            dt = datetime.fromisoformat(data_iso.replace("Z", "+00:00"))

        noticias["publicado_em"] = dt

        # --- descrição (opcional) ---
        desc_tag = soup.find("h2", class_="text-lg font-normal group-[.isActiveSource]:text-xl")
        noticias["descricao"] = desc_tag.get_text(strip=True) if desc_tag else ""

        # --- imagem (opcional) ---
        img_tag = soup.select_one(
            "picture.flex.object-cover.overflow-clip.w-full.aspect-video img.flex.size-full.object-cover"
        ) or soup.find("img", class_="flex size-full object-cover")

        noticias["imagem"] = (img_tag.get("src") or "").strip() if img_tag else ""

        return noticias

    except (requests.exceptions.RequestException, ValueError, AttributeError):
        return None
    


def noticias_CNN() -> list:
    urls = links()
    noticias = []

    for url in urls:
        dict_noticias = raspagemCNN(url)
        if dict_noticias == None:
            continue
        noticias.append(dict_noticias)
    return noticias

