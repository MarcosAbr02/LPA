class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Método de exibição da classe Veiculo:
    def exibir_info_veiculo(self):
        return f"Veículo: {self.marca} {self.modelo}"


# Classe Carro
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        Veiculo.__init__(self, marca, modelo)
        self.cor = cor

    # Método de exibição da classe Carro:
    def exibir_info_carro(self) -> str:
        return f"Carro: {self.marca} {self.modelo} {self.cor}"


# objeto 'carro' instanciado, herdando as
# as características da classe Veiculo
carro = Carro(marca="Toyota", modelo="Corolla", cor="Azul")
# método de impressão dos atributos que está em Veículo
# Saída -> Veículo: Toyota Corolla
print(carro.exibir_info_veiculo())
# método de impressão dos atributos que está na classe Carro
# Saída -> Carro: Toyota Corolla Azul
print(carro.exibir_info_carro())
