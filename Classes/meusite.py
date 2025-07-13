import datetime as dt

class Sites(object):
    def __init__(self, noticias_dict:dict ):
        self.noticias = noticias_dict
        self.nome_site = list(self.noticias.keys())[0]


    def imprimir_informacao(self):
        # autalizacao = dt.datetime.now()
        print(f"Noticias -- Ultima atualização às {dt.datetime.now().strftime('%H:%M:%S')} de {dt.date.today()} ")
        for noticia in self.noticias.values():
            for detalhe, link in noticia.items():
                print(f"{self.nome_site}: {detalhe}-- Link: {link} \n")
                # print("-"*(len(detalhe)+len(link)))
            



    
