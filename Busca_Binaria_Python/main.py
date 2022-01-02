import time

#
#  Busca binária recursiva
#
def busca_binaria_rec(vetor, alvo, ini, fim):

    if fim < ini:
        return -1

    meio = (ini + fim) // 2

    if alvo == vetor[meio]:
        return meio

    if alvo < vetor[meio]:
        return busca_binaria_rec(vetor, alvo, ini, meio - 1)

    return busca_binaria_rec(vetor, alvo, meio + 1, fim)

#
# Busca binária iterativa
#
def busca_binaria_ite(vetor, alvo):

    ini = 0
    fim = len(vetor) - 1

    while ini <= fim:

        meio = (ini + fim) // 2

        if alvo == vetor[meio]:
            return meio
        else:
            if alvo < vetor[meio]:
                fim = meio - 1
            else:
                ini = meio + 1

    return -1

x = range(1000000000000000000)

print('Vetor com %d entradas...' % len(x))

tempo_i = time.time()
n = busca_binaria_ite(x, 99985)
tempo_f = time.time()
print('Iterativa: posição {} (tempo de {})'.format(n, tempo_f - tempo_i))

tempo_i = time.time()
n = busca_binaria_rec(x, 999873483739999990, 0, len(x))
tempo_f = time.time()
print('Recursiva: posição {} (tempo de {})'.format(n, tempo_f - tempo_i))
