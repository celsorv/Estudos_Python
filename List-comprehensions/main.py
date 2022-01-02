# usando List Comprehensions

numeros = list(range(10, 20))

# list comprehensions
numeros_em_dobro = [x * 2 for x in numeros]
# -------------------
'''
# modo tradicional
numeros_em_dobro = []
for x in numeros:
  numeros_em_dobro.append(x * 2)
# ----------------
'''

print(numeros)
print(numeros_em_dobro)

# list comprehensions com condicional

print('\n# Só os números pares -----\n')

numeros = list(range(10))
numeros_em_dobro = [i * 2 for i in numeros if i % 2 == 0]

print(numeros)
print(numeros_em_dobro)

# lista multidimensional

print('\n# lista multidimensional -----\n')

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix)

double_matrix = [[2 * matrix[i][j] for j in range(3)] for i in range(3)]

print(double_matrix)

# transposição de matriz

print('\n# transposição de matriz -----')

matriz = [['@@@@@@@@@', '@@@@@@@@@', '@@@@@@@@@'],
          ['#########', '#########', '#########'],
          ['$$$$$$$$$', '$$$$$$$$$', '$$$$$$$$$']]

matriz_transposta = [[matriz[j][i] for j in range(len(matriz))]
                     for i in range(len(matriz[0]))]

print('\n' + '-' * 23 + ' Matriz original')
for x in matriz:
	print(x)

print('\n' + '-' * 21 + ' Matriz transposta')
for x in matriz_transposta:
	print(x)
