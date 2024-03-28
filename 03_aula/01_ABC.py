from abc import ABC, abstractmethod

# Esta classe não será instanciada, porém, as subclasses podem e serão instanciadas
class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self) -> str:
        return "Au Au"

class Gato(Animal):
    def fazer_som(self):
        return "Miau"