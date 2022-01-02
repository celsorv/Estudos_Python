import random
import time

#
#  BUBBLE SORT
#
def bubble_sort(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

#
# INSERTION SORT
#
def insertion_sort(lista):
    for i in range(1, len(x)):
        z = x[i]
        j = i - 1
        while j >= 0 and z < x[j]:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = z

#
# QUICK SORT
#
def quick_sort(vetor, ini, fim):

    meio = (ini + fim) // 2
    pivo = vetor[meio]
    i = ini
    j = fim

    while i < j:

        while vetor[i] < pivo: i += 1
        while vetor[j] > pivo: j -= 1

        if i <= j:
            vetor[i], vetor[j] = vetor[j], vetor[i]  # swap

        i += 1
        j -= 1

    if j > ini: quick_sort(vetor, ini, j)
    if i < fim: quick_sort(vetor, i, fim)

#
#  MERGE SORT
#
def merge_sort(vetor, ini, fim):
    if ini < fim:
        meio = (ini + fim) // 2
        merge_sort(vetor, ini, meio)
        merge_sort(vetor, meio + 1, fim)
        intercala(vetor, ini, meio, fim)

def intercala(vetor, ini, meio, fim):
    esq = vetor[ini : meio + 1]
    dir = vetor[meio + 1 : fim + 1]
    esq.append(999)     # sentinela
    dir.append(999)     # sentinela
    i = j = 0
    for k in range(ini, fim + 1):
        if esq[i] <= dir[j]:
            vetor[k] = esq[i]
            i += 1
        else:
            vetor[k] = dir[j]
            j += 1

#
#  HEAP SORT
#
def heap_sort(vetor):

    size = len(vetor)

    # Constrói uma heap máxima (maxheap)
    for i in range(size // 2 - 1, -1, -1):
        heapfica(vetor, size, i)

    # Extrai elementos um por um
    for i in range(size - 1, 0, -1):
        vetor[i], vetor[0] = vetor[0], vetor[i] # swap
        heapfica(vetor, i, 0)

def heapfica(vetor, n, k):

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 2 * k + 1 : filho esquerdo do nó k
    # 2 * k + 2 : filho direito do nó k
    # (k-1) / 2 : pai do nó k
    # n / 2     : onde começam os nós folha
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    maior = k   # Inicialmente assume pai como o maior
    esq = 2 * k + 1
    dir = 2 * k + 2

    # Filho esquerdo existe e é maior que o pai
    if esq < n and vetor[k] < vetor[esq]:
        maior = esq

    # Filho direito existe e é maior que o pai
    if dir < n and vetor[maior] < vetor[dir]:
        maior = dir

    # Maior filho assume como pai
    if maior != k:
        vetor[k], vetor[maior] = vetor[maior], vetor[k] # swap

        # Heapfica partindo da posição do maior encontrado
        heapfica(vetor, n, maior)

###

n = 1000

x = random.sample(range(0, n), n)
tempo_i = time.time()
x.sort()
tempo_f = time.time()
print('Python Sort   : {}'.format(tempo_f - tempo_i))

x = random.sample(range(0, n), n)
tempo_i = time.time()
bubble_sort(x)
tempo_f = time.time()
print('Bubble Sort   : {}'.format(tempo_f - tempo_i))

x = random.sample(range(0, n), n)
tempo_i = time.time()
quick_sort(x, 0, len(x) - 1)
tempo_f = time.time()
print('Quick Sort    : {}'.format(tempo_f - tempo_i))

x = random.sample(range(0, n), n)
tempo_i = time.time()
heap_sort(x)
tempo_f = time.time()
print('Heap Sort     : {}'.format(tempo_f - tempo_i))

x = random.sample(range(0, n), n)
tempo_i = time.time()
insertion_sort(x)
tempo_f = time.time()
print('Insertion Sort: {}'.format(tempo_f - tempo_i))

x = random.sample(range(0, n), n)
tempo_i = time.time()
merge_sort(x, 0, len(x) - 1)
tempo_f = time.time()
print('Merge Sort    : {}'.format(tempo_f - tempo_i))

