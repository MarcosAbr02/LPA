class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info_veiculo(self) -> str:
        return f"Veículo: {self.marca} {self.modelo}"


class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        Veiculo.__init__(self, marca, modelo)
        self.cor = cor

    def exibir_info_carro(self) -> str:
        return f"Carro: {self.marca} {self.modelo}{self.cor}"


class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def exibir_info_moto(self):
        return f"Moto: {self.marca} {self.modelo}, Cilindrada: {self.cilindrada}cc"


# MAIN

carro = Carro(marca="Toyota", modelo="Corolla", cor="Azul")
moto = Moto(marca="Honda", modelo="CBR600RR", cilindrada=600)

print(carro.exibir_info_veiculo())
print(moto.exibir_info_veiculo())
print(carro.exibir_info_carro())
print(moto.exibir_info_moto())