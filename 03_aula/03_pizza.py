class Pizza:
    def prepare(self):
        pass

    def bake(self):
        pass

    def cut(self):
        pass

    pass

    def box(self):
        pass


class MargheritaPizza:
    def prepare(self):
        print("Preparando Margherita Pizza....")

    def bake(self):
        print("Assando Margherita Pizza...")

    def cut(self):
        print("Cortando Margherita Pizza...")

    def box(self):
        print("Embalando Margherita Pizza....")


class PepperoniPizza:
    def prepare(self):
        print("Preparando Pepperoni Pizza....")

    def bake(self):
        print("Assando Pepperoni Pizza...")

    def cut(self):
        print("Cortando Pepperoni Pizza...")

    def box(self):
        print("Embalando Pepperoni Pizza....")


class PizzaFactory:
    def create_pizza(self, pizza_type: str):
        if pizza_type == "margherita":
            return MargheritaPizza()
        elif pizza_type == "pepperoni":
            return PepperoniPizza()
        else:
            raise ValueError("Tipo de pizza desconhecido")


factory = PizzaFactory()

pizza1 = factory.create_pizza("margherita")
pizza1.prepare()
pizza1.bake()
pizza1.cut()
pizza1.box()

print("-" * 40)

pizza2 = factory.create_pizza("pepperoni")
pizza2.prepare()
pizza2.bake()
pizza2.cut()
pizza2.box()
