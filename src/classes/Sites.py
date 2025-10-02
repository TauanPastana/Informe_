import datetime as dt

class Sites():
    def __init__(self, noticias_dict:dict, nome:str ):
        self.noticias = noticias_dict
        self.nome_site = nome
        self.quantidade = len(noticias_dict[list(self.noticias.keys())[0]])



    def imprimir_informacao(self):
        # autalizacao = dt.datetime.now()
        print(f"Noticias -- Ultima atualização às {dt.datetime.now().strftime('%H:%M:%S')} de {dt.date.today()} ")
        for noticia, link in self.noticias.items():
            print(f"{noticia}-- Link: {link} \n")
                    

    
            



    
