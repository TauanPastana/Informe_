from .utils import clear_terminal
import webbrowser as wb
class Noticias():
    def __init__(self, id:str, noticia:str, link:str):
        self.id = id
        self.noticia = noticia
        self.link =  link
    def abrir_link(self):
        try:
            clear_terminal()
            wb.open(self.link)
        except:
            print("Erro ao abrir o link")

    