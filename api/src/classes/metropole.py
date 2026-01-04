import requests
from bs4 import BeautifulSoup
from datetime import datetime
from django.utils import timezone


def raspagemMetropole(url: str) -> dict | None:
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
        titulo_tag = soup.find("h1", class_="Text__TextBase-sc-1d75gww-0 TcJvw")
        titulo = titulo_tag.get_text(strip=True) if titulo_tag else ""
        if not titulo:
            return None
        noticias["titulo"] = titulo

        # --- descrição (opcional) ---
        desc_tag = soup.find(
            "h2",
            class_="Text__TextBase-sc-1d75gww-0 eOYeiH noticiaCabecalho__subtitulo",
        )
        noticias["descricao"] = desc_tag.get_text(strip=True) if desc_tag else ""

        # --- imagem (opcional) ---
        fig = soup.find(
            "figure",
            class_="ImgDestaqueNoticiaWrapper__Imagem-sc-1frrxvx-2 ebzoXV",
        )
        img_tag = fig.find("img", fetchpriority="high") if fig else None
        noticias["imagem"] = (img_tag.get("src") or "").strip() if img_tag else ""

        # --- data (obrigatória) ---
        time_tag = soup.find(
            "time",
            class_="HeaderNoticiaWrapper__DataPublicacao-sc-4exe2y-3 dAMWSS",
        )
        if not time_tag:
            return None

        data_iso = time_tag.get("datetime")
        if not data_iso:
            return None

        try:
            dt = datetime.fromisoformat(data_iso)
        except ValueError:
            dt = datetime.fromisoformat(data_iso.replace("Z", "+00:00"))

        # Django: garantir datetime aware se necessário
        if timezone.is_naive(dt):
            dt = timezone.make_aware(dt)

        noticias["publicado_em"] = dt
        return noticias

    except (requests.exceptions.RequestException, ValueError, AttributeError, TypeError):
        return None




def links() -> list[str] | None:
    url = "https://www.metropoles.com/ultimas-noticias"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        blocos = soup.find_all(
            "div",
            class_="Grid__Col-sc-owmjhw-2 kuBfYv bloco-noticia__grid-figura",
        )
        if not blocos:
            return None

        urls: list[str] = []
        for bloco in blocos:
            a_tag = bloco.find("a")
            href = (a_tag.get("href") or "").strip() if a_tag else ""
            if href:
                urls.append(href)

        return urls if urls else None

    except (requests.exceptions.RequestException, AttributeError, TypeError):
        return None


def noticiasMetropoles() -> list[dict] | None:
    try:
        urls = links()
        if not urls:
            return None

        noticias: list[dict] = []

        for url in urls:
            dict_noticias = raspagemMetropole(url)
            if dict_noticias is None:
                continue
            noticias.append(dict_noticias)

        return noticias if noticias else None

    except Exception:
        return None
    
