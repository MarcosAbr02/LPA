import time


def medir_tempo(function):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = function(*args, **kwargs)
        fim = time.time()
        duracao = fim - inicio
        print(f"a função levou {duracao:.10f} segundos")
        return resultado

    return wrapper


@medir_tempo
def retorna_lista_par_sem_comprehension(max_value):
    lista_pares = []
    for num in range(max_value):
        if num % 2 == 0:
            lista_pares.append(num)
    return lista_pares


@medir_tempo
def retorna_lista_par_com_comprehension(max_value):
    lista_pares = [num for num in range(max_value) if num % 2 == 0]
    return lista_pares


retorna_lista_par_sem_comprehension(100)
retorna_lista_par_com_comprehension(100)

# Estrutura fica diferente caso queira adicionar else
print("Teste de list comprehension:")
lista_pares_quadrado = [num if num % 2 == 0 else 'impar' for num in range(10)]
for element in lista_pares_quadrado:
    print(element)

