class Functionary:
    def __init__(self, in_nome: str, in_cargo: str, in_salario: int):
        self.nome: str = in_nome
        self.cargo: str = in_cargo
        self.salario: int = in_salario

    def MostraReg(self):
        print(f'O nome do funcionário é {self.nome}')
        print(f'O cargo do {self.nome} é {self.cargo}')
        print(f'O salário do {self.cargo} {self.nome} é ${self.salario}')
        print()  # pular uma linha


# Início do Main
# o corpo principal do programa onde começa a ser rodado
# Instanciando os objetos baseados na classe Funcionario() com os parâmetros
func1 = Functionary(in_nome='Antônio', in_cargo='Gerente', in_salario=5000)
func2 = Functionary(in_nome='Maria', in_cargo='Diretora', in_salario=25000)
func3 = Functionary(in_nome='Pedro', in_cargo='Redator', in_salario=4000)
func4 = Functionary(in_nome='Zilda', in_cargo='Supervisora', in_salario=7500)

# Chamando o método MostraReg() para cada funcionário 'func' instanciado
func1.MostraReg()
func2.MostraReg()
func3.MostraReg()
func4.MostraReg()