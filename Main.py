from Classes import Folha, G1, CNN
folha = G1()
print(folha.quantidade)

def menu(self):
        while True:
            print("Bem vindo ao Informe\n")
            print(
                "Selecione uma opção:\n"
                "  1 - Exibir as últimas notícias da Folha de São Paulo\n"
                "  2 - Exibir as últimas notícias do G1\n"
                "  3 - Exibir as últimas notícias da CNN\n"
                "  0 - Sair\n"
            )

            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                site1 = Folha()
                site1.imprimir_informacao()
            elif opcao == "2":
                site = G1()
                site.imprimir_informacao()
            elif opcao == "3":
                site2 = CNN()
                site2.imprimir_informacao()
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

















