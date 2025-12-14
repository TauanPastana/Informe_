
from time import sleep
from .utils import clear_terminal
from.Gerenciador_noticias import Gerenciador_noticias

class Menu():
    def __init__(self):
        self.manager = Gerenciador_noticias()

    
    def menu(self):
        mapping = {
            "1": 'g1',
            "2": 'cnn',
            "3": 'band',
            "4": 'metropole',
            "5": 'all'
        }
        while True:
            print("Bem-vindo ao Informe. O portal que reúne todas as últimas informações dos maiores portais de notícias do Brasil.")
            print(
            "Selecione uma opção:\n"
            "  1 - Exibir as últimas notícias do G1\n"
            "  2 - Exibir as últimas notícias da CNN\n"
            "  3 - Exibir as últimas notícias da Band\n"
            "  4 - Exibir as últimas notícias da Metrópole\n"
            "  5 - Visualizar todas as notícias\n"
            "  0 - Sair\n"
            )

            opcao = input("Digite a opção desejada: ")
            clear_terminal()

            if opcao == "0":
                print("Saindo...")
                break


            site = mapping.get(opcao)
            if site:
                self.manager.imprimir_site(site)
            else:
                print("Opção inválida. Tente novamente.")
                sleep(3)
                clear_terminal()
