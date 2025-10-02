import webbrowser as wb
import datetime as dt

class Sites():
    def __init__(self, noticias_dict:dict, nome:str ):
        self.noticias = noticias_dict
        self.nome_site = nome
        self.quantidade = len(noticias_dict[list(self.noticias.keys())[0]])



    def imprimir_informacao(self):
        # autalizacao = dt.datetime.now()
        print(f"Noticias -- Ultima atualização às {dt.datetime.now().strftime('%H:%M:%S')} de {dt.date.today()} ")
        for id, noticia in self.noticias.items():
            print(f"{id} - {noticia["Noticias"]} -- Link: {noticia["Link"]} \n")
                    
    def getSite(self):
        opc = int(input("Digite o ID relacionado a noticia que deseja acessar: "))
        dict_get:dict = self.noticias.get(opc)
        self.abrir_link(dict_get.get('Link'))

    def abrir_link(self, url):
        try:
            wb.open(url)
        except:
            print("Erro ao abrir o link")
        
        
    
            



    
