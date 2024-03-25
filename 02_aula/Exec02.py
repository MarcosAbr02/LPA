class Peca:
    def __init__(self, nome: str, fabricante: str, preco: float):
        self.nome = nome
        self.fabricante = fabricante
        self.preco = preco

    def exibirPeca(self):
        print(f'Peça: {self.nome}, Fabricante: {self.fabricante}, Preço: {self.preco:.2f}')
        print()

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
                print()
                print("Insira um valor válido!")
                print()
                continue

        regPeca = Peca(nome, fabricante, preco)
        registro.append(regPeca)
        print()

    elif opcao == "2":
        if len(registro) == 0:
            print()
            print("Não há registros a serem exibidos")
            print()
            continue

        print()
        print("Lista atualizada")
        print()
        for i in range(len(registro)):
            print(f"Registro {(i + 1)}:")
            registro[i].exibirPeca()

    elif opcao == "3":
        if len(registro) == 0:
            print()
            print("Não há registros a serem exibidos")
            print()
            continue

        nomePeca = input("Nome da peça>>>")

        achou = False
        for i in range(len(registro)):

            if nomePeca == registro[i].getNome():
                print()
                registro[i].exibirPeca()
                achou = True
                break
        if not achou:
            print()
            print("Nenhuma peça com esse nome foi encontrada")
            print()

    else:
        print()
        print("Escolha uma opção!")
        print()
