class Peca:
    def __init__(self, nome: str, fabricante: str, preco: float):
        self.nome = nome
        self.fabricante = fabricante
        self.preco = preco

    def exibirPeca(self):
        print(f'Peça: {self.nome}, Fabricante: {self.fabricante}, Preço: {self.preco:.2f}\n')

    def getNome(self):
        return self.nome


registro = []

while True:
    opcao = input("Selecione uma ação: " +
                  "\n1 - Cadastrar peça" +
                  "\n2 - Exibir peças" +
                  "\n3 - Visualizar registro por nome" +
                  "\n4 - Encerrar o programa" +
                  ">>>")

    if opcao == "1":
        nome = input("Nome da peça>>>")
        fabricante = input("Fabricante>>>")
        preco = 0
        while True:
            try:
                preco = float(input("Valor da peça:"))
                break
            except ValueError:
                print("\nInsira um valor válido!\n")
                continue

        regPeca = Peca(nome, fabricante, preco)
        registro.append(regPeca)
        print()

    elif opcao == "2":
        if not registro:
            print("\nNão há registros a serem exibidos\n")
            continue

        print("\nLista atualizada\n")
        for i in range(len(registro)):
            print(f"Registro {(i + 1)}:")
            registro[i].exibirPeca()

    elif opcao == "3":
        if not registro:
            print("\nNão há registros a serem exibidos\n")
            continue

        nomePeca = input("Nome da peça>>>")

        achou = False
        for peca in registro:

            if nomePeca == peca.getNome():
                print()
                peca.exibirPeca()
                achou = True
                break
        if not achou:
            print("\nNenhuma peça com esse nome foi encontrada\n")

    elif opcao == "4":
        break

    else:
        print("\nEscolha uma opção!\n")
