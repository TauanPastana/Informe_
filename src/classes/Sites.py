import webbrowser as wb
import datetime as dt
import os
from abc import ABC, abstractmethod


class Sites():
    def __init__(self, noticias_dict:dict, nome:str ):
        self.noticias = noticias_dict
        self.nome_site = nome



    def imprimir_informacao(self):
        # autalizacao = dt.datetime.now()
        print(f"Noticias -- Ultima atualização às {dt.datetime.now().strftime('%H:%M:%S')} de {dt.date.today().strftime('%d-%m-%Y')}")
        for id, noticia in self.noticias.items():
            print(f"{id} - {noticia["Noticias"].strip()}\n")
                    
    def getSite(self):
        opc = input("Se deseja ler alguma dessas noticias, digite o id correspondente a mesma\nCaso ao contrário, precione qualquer tecla: ")
        chaves = list(self.noticias.keys())
        if opc in chaves:
            dict_get:dict = self.noticias.get(opc)
            self.abrir_link(dict_get.get('Link'))

        

    def abrir_link(self, url):
        try:
            Sites.clear_terminal()
            wb.open(url)
        except:
            print("Erro ao abrir o link")
    @staticmethod
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @abstractmethod
    def update_atualizacao(self):
        pass


    
        
        
    
            



    
