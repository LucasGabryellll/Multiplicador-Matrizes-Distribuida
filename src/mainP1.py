from turtle import st
import time

quantLinhas = 0
quantColunas = 0

s = 0

# Função para realizar a multiplicação das matrizes
def mult_matriz(A, B):
  global s

  num_linhas_A, num_colunas_A = len(A), len(A[0])
  num_linhas_B, num_colunas_B = len(B), len(B[0])

  contagem_Inicial = time.time()
  assert num_colunas_A == num_linhas_B

  C = []
  for linha in range(num_linhas_A):
    C.append([])
    for coluna in range(num_colunas_B):
      C[linha].append(0)
      for k in range(num_colunas_A):
        C[linha][coluna] += A[linha][k] * B[k][coluna]
 
  contagem_Final = time.time()
  with open('src/matrizesResultados/resultado{}.txt'.format(quantLinhas), 'w') as arquivo:
    for valor in C:
      arquivo.write(str(valor).lstrip())

  s = contagem_Final - contagem_Inicial

  return C

# Função que vai subdividir as matrizes
def sub_list(lista, n):
  for i in range(0, len(lista), n):
    yield lista[i:i + n]

# Função para abrir o arquivo da matri
def open_arquivo(link):
  m1 = []
  global s

  global quantLinhas, quantColunas
  with open(link, 'r') as matriz:
    for valor in matriz:
      chars = '\n'
      intValor = valor.translate(str.maketrans('', '', chars))

      for itemInt in intValor.split():
        m1.append(float(itemInt.strip()))

  tam_sub_list = int(m1[0])

  quantLinhas = int(m1[0])
  quantColunas = int(m1[1])

  del m1[0], m1[0]
  listaDivida = list(sub_list(m1, tam_sub_list))

  return listaDivida

A = open_arquivo('src/matrizes/10.txt')
B = open_arquivo('src/matrizes/10.txt')
mult_matriz(A, B)

print('1. Variação do programa(P1...P5): ')

print('2. Número de linhas da matriz: ', quantLinhas)
print('3. Número de colunas da matriz: ', quantColunas)
print(f'4. Tempo de processamento: {s} segundos')

