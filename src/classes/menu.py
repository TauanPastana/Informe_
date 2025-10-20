from classes import G1, CNN, Band, Sites

class Menu():
    def __init__(self):
        self.g1 = G1()
        self.cnn = CNN()
        self.band = Band()
        
 
    def _exibir_site(self, site):
        site.update_atualizacao()
        site.imprimir_informacao()
        site.getSite()
        Sites.clear_terminal()

    def menu(self):
        mapping = {"1": self.g1, "2": self.cnn, "3": self.band}
        while True:
            print("Bem-vindo ao Informe. O portal que reúne todas as últimas informações dos maiores portais de notícias do Brasil.")
            print(
                "Selecione uma opção:\n"
                "  1 - Exibir as últimas notícias do G1\n"
                "  2 - Exibir as últimas notícias da CNN\n"
                "  3 - Exibir as últimas notícias da Band\n"
                "  0 - Sair\n"
            )

            opcao = input("Digite a opção desejada: ")

            if opcao == "0":
                print("Saindo...")
                break

            site = mapping.get(opcao)
            if site:
                self._exibir_site(site)

            else:
                print("Opção inválida. Tente novamente.")
