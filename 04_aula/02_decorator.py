# # ---------------------------------------------------------------------------------------------------------------------
# Tema 2 part1
# Definindo o decorator
# def meu_decorator(funcao):
#     def wrapper():
#         print("A função será executada agora.")
#         funcao()
#         print("A função foi executada.")
#
#     return wrapper
#
#
# # Aplicando o decorator usando o símbolo @
# @meu_decorator
# def minha_funcao():
#     print("Esta é a função original.")
#
#
# # Chamando a função decorada
# minha_funcao()
# # ---------------------------------------------------------------------------------------------------------------------
# #
# # ---------------------------------------------------------------------------------------------------------------------
# Tema 2 part2
import time


# Definindo o decorator para medir o tempo de execução
def medir_tempo(funcao):
    def wrapper(*args, **kwargs):
        print("carregando...")
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f"A função '{funcao.__name__}' demorou {fim - inicio:.6f} segundos para ser executada.")
        return resultado

    return wrapper


# Aplicando o decorator usando o símbolo @
@medir_tempo
def exemplo_funcao(tempo_espera):
    time.sleep(tempo_espera)
    print("A função foi executada.")


@medir_tempo
def exemplo_funcao2(tempo_espera):
    time.sleep(tempo_espera)
    print("A função foi executada.")


# Chamando a função decorada
exemplo_funcao(2)
exemplo_funcao2(4)

# # ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
# Tema 2 part3
# Definindo o decorator de classe
# class Carro:
#     def __init__(self, classe_decorada):
#         self.classe_decorada = classe_decorada
#
#     def __call__(self, *args, **kwargs):
#         # Instancia a classe original
#         instancia_classe = self.classe_decorada(*args, **kwargs)
#         # Adiciona o atributo extra
#         instancia_classe.num_rodas = 4
#         return instancia_classe
#
#
# # Aplicando o decorator de classe usando o símbolo @
# @Carro
# class Automovel:
#     def __init__(self, modelo):
#         self.modelo = modelo
#
#
# # Criando uma instância da classe decorada
# new_auto = Automovel('Gol')
#
# # Chamando o método da classe e exibindo o atributo extra
# print(new_auto.modelo)
# print(new_auto.num_rodas)
# ---------------------------------------------------------------------------------------------------------------------
