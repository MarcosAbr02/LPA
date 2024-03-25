class Aluno:
    def __init__(self, nome: str, idade: int, curso: str):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def mostrarInfo(self):
        print(f"Nome: {self.nome}, idade: {self.idade}, curso: {self.curso}\n")

    def setDate(self, nome: str, idade: int, curso: str):
        self.nome = nome
        self.idade = idade
        self.curso = curso


registro = []
while True:
    opcao = input("Selecione uma opção: " +
                  "\n1 - Cadastrar aluno" +
                  "\n2 - Exibir alunos" +
                  "\n3 - Alterar registro" +
                  "\n4 - Fechar programa" +
                  "\n>>>")

    if opcao == "1":
        nome = input("Nome>>>")
        idade = 0
        while True:
            try:
                idade = int(input("Idade>>>"))
                break
            except ValueError:
                print("Insira um valor válido!")
                continue

        curso = input("Curso>>>")

        regAluno = Aluno(nome, idade, curso)
        registro.append(regAluno)
        print("\nAluno registrado:\n")
        regAluno.mostrarInfo()

    if opcao == "2":
        if not registro:
            print("Não há alunos a serem exibidos")
            continue
        print("\nLista atualizada\n")
        for i in range(len(registro)):
            print(f"Registro {(i + 1)}:")
            registro[i].mostrarInfo()

    if opcao == "3":
        if not registro:
            print("Não há alunos a serem exibidos")
            continue
        print("\nLista atualizada\n")
        for i in range(len(registro)):
            print(f"Registro {(i + 1)}:")
            registro[i].mostrarInfo()

        print("Qual registro deseja alterar?")
        opc = 0
        try:
            opc = int(input(">>>"))
        except ValueError:
            print("Nenhuma opção escolhida, retornando ao menu\n")
            continue

        if opc <= 0 or opc > len(registro):
            print("Nenhuma opção escolhida, retornando ao menu\n")
            continue

        novoRegistro = registro[opc - 1]
        novoRegistro.mostrarInfo()

        nome = input("Novo nome>>>")
        idade = 0
        while True:
            try:
                idade = int(input("Nova idade>>>"))
                break
            except ValueError:
                print("Insira um valor válido!")
                continue

        curso = input("Novo curso>>>")

        novoRegistro.setDate(nome, idade, curso)
        print("\nRegistro atualizado:")
        novoRegistro.mostrarInfo()

    if opcao == "4":
        break
