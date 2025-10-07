from classes import Folha, G1, CNN, Uol

class Menu():
    def __init__(self):
        self.folha = Folha()
        self.g1 = G1()
        self.cnn = CNN()
        self.uol = Uol()

    
    def menu(self):
        while True:

            print("Bem-vindo ao Informe. O portal que reúne todas as últimas informações dos maiores portais de notícias do Brasil.")
            print(
                "Selecione uma opção:\n"
                "  1 - Exibir as últimas notícias da Folha de São Paulo\n"
                "  2 - Exibir as últimas notícias do G1\n"
                "  3 - Exibir as últimas notícias da CNN\n"
                "  4 - Exibir as últimas notícias do UOL\n"
                "  0 - Sair\n"
            )

            opcao = input("Digite a opção desejada: ")
            

            if opcao == "1":
                self.folha.update_atualizacao()
                self.folha.imprimir_informacao()
                self.folha.getSite()
            elif opcao == "2":
                self.g1.update_atualizacao()
                self.g1.imprimir_informacao()
                self.g1.getSite()
            elif opcao == "3":
                self.cnn.update_atualizacao
                self.cnn.imprimir_informacao()
                self.cnn.getSite()
            elif opcao == "4":
                self.uol.update_atualizacao()
                self.uol.imprimir_informacao()
                self.uol.getSite()
                
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")