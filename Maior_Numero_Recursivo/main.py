#
# Retornar o maior elemento de uma lista usando recursão
#

import time, random


# modo iteração
def maior_it(lista):

    maior = -1

    for i in range(len(lista)):
        if maior == -1 or lista[i]>lista[maior]:
            maior = i

    if maior == -1:
        return -1

    return lista[maior]


# modo recursivo
def maior_rec_det(lista, n):

    if n == 1:
        #print(str(n) + ': maior(' + str(n) + ') ==> ' + str(lista[0]))
        return lista[0]

    #print(str(n) + ': max(maior(lista, ' + str(n - 1) + '), lista[' + str(n - 1) + ']')
    return max(maior_rec_det(lista, n - 1), lista[n - 1])


# modo recursivo usando memoização
def maior_rec(lista, n, m = dict()):

    if n == 1:
        return lista[0]

    if m.get(n - 1) == None:
        m[n - 1] = maior_rec(lista, n - 1)

    return max(m[n - 1], lista[n - 1])


lista = random.sample(range(100), 100)

tempo_i = time.time()
print('\nresultado:', maior_it(lista))
print('Iterative: {} seconds'.format(time.time() - tempo_i))

tempo_i = time.time()
print('\nresultado:', maior_rec(lista, len(lista)))
print('Memoization: {} seconds'.format(time.time() - tempo_i))

tempo_i = time.time()
print('\nresultado:', maior_rec_det(lista, len(lista)))
print('Recursive: {} seconds'.format(time.time() - tempo_i))
