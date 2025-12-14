
import datetime as dt
from abc import abstractmethod
from classes import Noticias
from time import sleep



class Sites():
    def __init__(self, noticias_object:dict[str, Noticias], nome:str ): # type: ignore
        self.noticias = noticias_object
        self.nome = nome



    def imprimir_informacao(self):
        # autalizacao = dt.datetime.now()
        print(f"Informe -- Noticias do portal {self.nome}      |Ultima atualização às {dt.datetime.now().strftime('%H:%M:%S')} de {dt.date.today().strftime('%d-%m-%Y')}|\n")
        for id, noticia in self.noticias.items():
            print(f"{id} - {noticia.noticia}")
        
                    
    def getSite(self):
        opc = input("\nSe deseja ler alguma dessas noticias, digite o id correspondente a mesma\nCaso ao contrário, precione qualquer tecla: ")
        if opc in self.noticias.keys():
            self.noticias.get(opc).abrir_link()
        else:
            sleep(2)
            return None
        # Se o usuário digitou algo numérico (parece um id) mas não existe -> avisar e perguntar novamente

        # Se o usuário pressionou qualquer outra tecla (ou apenas Enter), volta ao menu (não faz nada)
        
    
    

            
            
        


        

    
    
    @abstractmethod
    def update_atualizacao(self):
        pass


    
        
        
    
            



    
