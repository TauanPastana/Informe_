import datetime as dt

class Sites():
    def __init__(self, noticias_dict:dict ):
        self.noticias = noticias_dict
        self.nome_site = list(self.noticias.keys())[0]
        self.quantidade = len(noticias_dict[list(self.noticias.keys())[0]])



    def imprimir_informacao(self):
        # autalizacao = dt.datetime.now()
        print(f"Noticias -- Ultima atualização às {dt.datetime.now().strftime('%H:%M:%S')} de {dt.date.today()} ")
        for noticia in self.noticias.values():
            contagem= 0
            for detalhe, link in noticia.items():
                contagem+=1
                if contagem > 10:
                    break
                else:
                    print(f"{self.nome_site}: {detalhe}-- Link: {link} \n")

    
            



    
