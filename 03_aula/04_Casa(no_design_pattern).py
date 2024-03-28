class Casa:
    def __init__(self, num_quartos=None, num_banheiros=None, tem_garagem=False, tem_jardim=False):
        self.num_quartos = num_quartos
        self.num_banheiros = num_banheiros
        self.tem_garagem = tem_garagem
        self.tem_jardim = tem_jardim

    def __str__(self):
        caracteristicas = []
        if self.num_quartos:
            caracteristicas.append(f"Número de quartos:{self.num_quartos}")
        if self.num_banheiros:
            caracteristicas.append(f"Número de banheiros:{self.num_banheiros}")
        if self.tem_garagem:
            caracteristicas.append("Possui garagem")
        if self.tem_jardim:
            caracteristicas.append("Possui jardim")
        return ', '.join(caracteristicas)


# Construindo uma casa com garagem e jardim
casa = Casa(num_quartos=3, num_banheiros=2, tem_garagem=True, tem_jardim=True)
print("Características da casa:", casa)

# Construindo outra casa sem garagem e com 4 quartos
outra_casa = Casa(num_quartos=4, num_banheiros=3)
print("Características da outra casa:", outra_casa)
