from turtle import st

quantLinhas = 0
quantColunas = 0

# Função para realizar a multiplicação das matrizes
def mult_matriz(A, B):
  num_linhas_A, num_colunas_A = len(A), len(A[0])
  num_linhas_B, num_colunas_B = len(B), len(B[0])
  assert num_colunas_A == num_linhas_B

  C = []
  for linha in range(num_linhas_A):
    C.append([])
    for coluna in range(num_colunas_B):
      C[linha].append(0)
      for k in range(num_colunas_A):
        C[linha][coluna] += A[linha][k] * B[k][coluna]

  return C

# Função que vai subdividir as matrizes
def sub_list(lista, n):
  for i in range(0, len(lista), n):
    yield lista[i:i + n]

# Função para abrir o arquivo da matriz
def open_arquivo(link):
  m1 = []
  global quantLinhas, quantColunas
  with open(link, 'r') as matriz:
    for valor in matriz:
      chars = '\n'
      intValor = valor.translate(str.maketrans('', '', chars))

      
      for itemInt in intValor.split():
        m1.append(int(itemInt.strip()))
      
      #m1.append(intValor.split())
  tam_sub_list = m1[0]
  
  quantLinhas = m1[0]
  quantColunas = m1[1]

  del m1[0], m1[0]
  listaDivida = list(sub_list(m1, tam_sub_list))
  return listaDivida
  
  #return m1

A = open_arquivo('matrizes/4_int.txt')
B = open_arquivo('matrizes/4_int.txt')

print('1. Variação do programa(P1...P5): ')
print('2. Número de Cores: ')
print('3. Número de computadores Remotos: ')
print('4. Número de linhas da matriz: ', quantLinhas)
print('5. Número de colunas da matriz: ', quantColunas)
print('6. Tempo de processamento: ')
print('7. Linha em branco: ')
print('8. Matriz de Resposta: ', mult_matriz(A, B))

