from classes import G1, CNN, Band

class Menu():
    def __init__(self):
        self.g1 = G1()
        self.cnn = CNN()
        self.band = Band()
        
    def menu(self):
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
            
            if opcao == "1":
                self.g1.update_atualizacao()
                self.g1.imprimir_informacao()
                self.g1.getSite()
            elif opcao == "2":
                self.cnn.update_atualizacao()
                self.cnn.imprimir_informacao()
                self.cnn.getSite()
            elif opcao == "3":
                self.band.update_atualizacao()
                self.band.imprimir_informacao()
                self.band.getSite()
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
