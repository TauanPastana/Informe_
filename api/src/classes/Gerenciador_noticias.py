from ast import match_case
from classes import G1, CNN, Band, Sites, Metropole
from random import shuffle, choice
from.utils import clear_terminal

class Gerenciador_noticias():
    def __init__(self):
        self.g1 = G1()
        self.cnn = CNN()
        self.band = Band()
        self.metropole = Metropole()
        self.total_news = []
        self.quantidade = 0
        
    
    def imprimir_todos(self):
        self.mesclar_noticias()
        id_noticias = []
        for noticia in self.total_news:
            id_noticias.append(noticia.id)
            print(f"{noticia.id} - {noticia.noticia}")
        opc = input("Digite o id correspondente da noticia que deseja ver: ")
        if opc in id_noticias:
            self.total_news.get(opc).abrir_link()
        else:
            print("Id não correspondente")
    
    def mesclar_noticias(self):
        self.total_news.clear()
        all_news = []
        all_news.extend(self.band.noticias)
        all_news.extend(self.cnn.noticias)
        all_news.extend(self.g1.noticias)
        all_news.extend(self.metropole.noticias)
        
        shuffle(all_news)
        self.total_news = all_news
                
    def imprimir_site(self, site):
        match site:
            case 'g1':
                self.exibir_site(self.g1)
            case 'cnn':
                self.exibir_site(self.cnn)
            case 'band':
                self.exibir_site(self.band)
            case 'metropole':
                self.exibir_site(self.metropole)
            case 'all':
                self.imprimir_todos()

    def exibir_site(self, site:Sites):
        site.imprimir_informacao()
        site.getSite()
        


    

    
    def criar_id(self):
        self.quantidade+=1
        return self.quantidade
    def sites_get(self) -> list[Sites]: 
        return [self.g1, self.cnn, self.band, self.metropole]



        