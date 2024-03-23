class Funcionario:
    def __init__(self, nome: str, cargo: str, salario: float):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def exibirFuncionario(self):
        print(f'O nome do funcionário é {self.nome}')
        print(f'O cargo do {self.nome} é {self.cargo}')
        print(f'O salário do {self.cargo} {self.nome} é ${self.salario:.2f}')
        print()


registro = []
while True:
    opcao = input("Selecionar uma ação: " +
                  "\r\n1 - Adicionar funcionário" +
                  "\r\n2 - Mostrar os registros existentes" +
                  "\r\n3 - Sair"
                  "\r\n>>>>")

    if opcao == "1":
        nome = input("Inserir nome do funcionário: >>")
        cargo = input("Inserir o cargo do funcionário: >>")
        salario = 0

        while True:
            try:
                salario = int(input("inserir o salário do funcionário: >>"))
                break
            except ValueError:
                print("Inserir apenas números")
                continue
        regFunc = Funcionario(nome, cargo, salario)
        registro.append(regFunc)

        for i in range(len(registro)):
            print()
            print("Lista atualizada")
            print()
            print(f"Funcionário {(i + 1)}#")
            registro[i].exibirFuncionario()
    elif opcao == "2":
        if len(registro) == 0:
            print("Não há elementos para serem exibidos!")
            continue
        for i in range(len(registro)):
            print()
            print("Lista atualizada")
            print()
            print(f"Funcionário {(i + 1)}#")
            registro[i].exibirFuncionario()
    elif opcao == "3":
        print("Encerrando sistema")
        break
    else:
        print("Opção inválida, tente novamente!")
