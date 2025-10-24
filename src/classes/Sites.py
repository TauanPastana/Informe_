import webbrowser as wb
import datetime as dt
import os
from abc import abstractmethod
from classes import Noticias
from time import sleep


class Sites():
    def __init__(self, noticias_object:dict[str,Noticias], nome:str ):
        self.noticias = noticias_object
        self.nome = nome



    def imprimir_informacao(self):
        # autalizacao = dt.datetime.now()
        print(f"Informe -- Noticias do portal {self.nome}      |Ultima atualização às {dt.datetime.now().strftime('%H:%M:%S')} de {dt.date.today().strftime('%d-%m-%Y')}|\n")
        for noticia in self.noticias.values():
            print(f"{noticia.id} - {noticia.noticia}")
        
                    
    def getSite(self):
        opc = input("\nSe deseja ler alguma dessas noticias, digite o id correspondente a mesma\nCaso ao contrário, precione qualquer tecla: ")
        if opc in self.noticias.keys():
            self.abrir_link(self.noticias.get(opc).link)
        else:
            print("Id não existe, por favor, adicione um ID existente")
            sleep(3)
            self.getSite()
            
        


        

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


    
        
        
    
            



    
