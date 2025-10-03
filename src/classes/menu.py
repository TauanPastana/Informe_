from classes import Folha, G1, CNN
class Menu():
    @staticmethod
    def menu():
        while True:
            print("Bem-vindo ao Informe. O portal que reúne todas as últimas informações dos maiores portais de notícias do Brasil.")
            print(
                "Selecione uma opção:\n"
                "  1 - Exibir as últimas notícias da Folha de São Paulo\n"
                "  2 - Exibir as últimas notícias do G1\n"
                "  3 - Exibir as últimas notícias da CNN\n"
                "  0 - Sair\n"
            )

            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                folha = Folha()
                folha.imprimir_informacao()
                folha.getSite()
            elif opcao == "2":
                g1 = G1()
                g1.imprimir_informacao()
                g1.getSite()
            elif opcao == "3":
                cnn = CNN()
                cnn.imprimir_informacao()
                cnn.getSite()
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")