class ContaBancaria:
    def __init__(self, saldo: float, titular: str):
        self.saldo = saldo
        self.titular = titular

    def exibirConta(self):
        print(f"Titular: {self.titular}, saldo: {self.saldo:.2f}\n")

    def depositar(self, valor: float):
        self.saldo += valor

    def sacar(self, valor: float):
        if valor > self.saldo:
            print("Não foi possível realizar o saque, pois o valor informado é maior que o saldo disponível na conta.\n")
        else:
            self.saldo -= valor
            print("Saque realizado com sucesso!\n")
            self.exibirConta()


contaExiste = False
conta = None
while True:
    opcao = input("O que deseja fazer?" +
                  "\n1 - Criar conta" +
                  "\n2 - Depositar" +
                  "\n3 - Sacar" +
                  "\n4 - Sair\n>>> ")

    if opcao == "1":
        if contaExiste:
            print("Parece que uma conta já foi criada neste dispositivo!\n")
            continue

        saldo = 0
        while True:
            try:
                saldo = float(input("Saldo inicial da conta>>> "))
                break
            except ValueError:
                print("Insira um valor coerente.")
                continue

        titular = input("Titular>>> ")

        conta = ContaBancaria(saldo, titular)
        contaExiste = True
        print("Conta criada com sucesso!\n")

    if opcao == "2":
        if not contaExiste:
            print("Não é possível fazer um depósito, pois a conta ainda não foi criada.\n")
            continue

        valor = 0
        while True:
            try:
                valor = float(input("Valor de Depósito>>> "))
                break
            except ValueError:
                print("Insira um valor coerente.")

        conta.depositar(valor)
        print(f"Depósito de R${valor:.2f} realizado com sucesso!\n")
        conta.exibirConta()

    if opcao == "3":
        if not contaExiste:
            print("Não é possível fazer um saque, pois a conta ainda não foi criada.\n")
            continue

        valor = 0
        while True:
            try:
                valor = float(input("Valor de Saque>>> "))
                break
            except ValueError:
                print("Insira um valor coerente.")

        conta.sacar(valor)

    if opcao == "4":
        break