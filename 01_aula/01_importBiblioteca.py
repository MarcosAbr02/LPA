# O que é um numpy: é uma biblioteca que oferece estruturas de dados não nativas do python com suporte matemáticos
# Porque numpy: oferece desempenho e ferramentas superiores à biblioteca padrão
# O numpy trabalha como a idea de vetores (arrays), conhecidos como ndarrays
# Com a diferença que ndarrays só trabalham com dados do mesmo tipo que lembram muito as listas do python.
# Outra vantagem: por trabalhar com um só tipo de dado, o ndarray tem um desempenho muito melhor se comparado com listas
import time

import numpy
import plotly.express

# # 1 -Exemplo de criação:
# lista_num = numpy.zeros(100000)
# print(f' 1- Conteúdo da Lista: {lista_num}, o tamanho: {len(lista_num)}')
# lista_num = numpy.ones(100000)
# print(f' 2- Conteúdo da Lista: {lista_num}, o tamanho: {len(lista_num)}')
# lista_num = numpy.linspace(10, 1000, 991)
# print(f' 3- Conteúdo da Lista: {lista_num}, o tamanho: {len(lista_num)}')

# 2- Comparar desempenho
# start_time = time.time()
# lista = [0] * 1000000000
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f'A criação de lista de 1 bilhão de elementos levou: {elapsed_time}')
#
# start_time = time.time()
# ndarray = numpy.zeros(1000000000)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f'A criação de um ndarray de 1 bilhão de elementos levou: {elapsed_time}')

# 3- Dá para fazer ainda melhor se definirmo o tipo de dado, exemplo: dado tipo int8 (para valores de 0 - 255)
# start_time = time.time()
# ndarray_uint8 = numpy.zeros(1000000000, dtype='uint8')
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f'A criação de um ndarray de 1 bilhão de elementos em int de 8 não sinalizado levou: {elapsed_time}')

# 4 - Podemos criar vetores, matrizes e tensores
# rng = numpy.random.default_rng()  # numpy tem sua métodos randoms inclusos
# vetor = rng.random(4)
# print(f'Array de 1 Dimensão (VETOR) randômico:\n{vetor}\n')
# matriz = rng.random([4, 4])
# print(f'Array de 2 Dimensões (MATRIZ) randômico:\n{matriz}\n')
# tensor = rng.random([4, 4, 4])
# print(f'Array de 3  Dimensões (TENSOR) randômico:\n{tensor}\n')

# 5- Posso ordenar esses vetores
# rng = numpy.random.default_rng()
# matriz = rng.random([4, 4])
# m_coluna = numpy.sort(matriz, axis=0)
# m_linha = numpy.sort(matriz, axis=1)
# m_col_lin = numpy.sort(m_linha, axis=0)
# print(f'Matriz:\n{matriz}')
# print(f'Ordenação dentro coluna:\n{m_coluna}')
# print(f'Ordenação dentro linha :\n{m_linha}')
# print(f'Ordenação dentro coluna e linha :\n{m_col_lin}')

# 6 - Agora vamos preparar alguns ndarrays para serem representados por gráficos:
# vetor_a = numpy.linspace(10, 1000, 100)
# vetor_b = numpy.linspace(10, 3000, 100)
# vetor_c = numpy.linspace(10, 8000, 100)
#
#
# print(vetor_a)
# print(vetor_b)
# print(vetor_c)
#
# # Numpy já tem métodos bem diretos de como salvar um arquivo no formato .txt
# numpy.savetxt('vetor_a.txt', vetor_a, fmt='%.2f', delimiter=';')
# numpy.savetxt('vetor_b.txt', vetor_b, fmt='%f', delimiter=';')
# numpy.savetxt('vetor_c.txt', vetor_c, fmt='%f', delimiter=';')

# 7 - Agora podemos utilizar uma das várias bibliotecas para plotar gráficos, eu escolhi a plotly

array_a = numpy.loadtxt('vetor_a.txt', dtype=numpy.float64, delimiter=';')
array_b = numpy.loadtxt('vetor_b.txt', dtype=numpy.float64, delimiter=';')
array_c = numpy.loadtxt('vetor_c.txt', dtype=numpy.float64, delimiter=';')
print(array_a)

array_abc = numpy.vstack([array_a, array_b, array_c])
print(array_abc)
array_abc = array_abc.transpose()
print(array_abc)
fig = plotly.express.line(array_abc)
fig.show()
