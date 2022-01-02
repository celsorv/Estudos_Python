class Nodo:

    def __init__(self, chave = None, esquerda = None, direita = None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % \
               (self.esquerda and self.esquerda.chave, self.chave,
                self.direita and self.direita.chave)

def insere(raiz, nodo):

    # Insere nodo na raiz
    if raiz is None:
        raiz = nodo
        return

    # Insere nodo na subárvore direita
    if nodo.chave > raiz.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere(raiz.direita, nodo)
        return

    # Insere nodo na subárvore esquerda
    if raiz.esquerda is None:
        raiz.esquerda = nodo
    else:
        insere(raiz.esquerda, nodo)

def busca(raiz, chave):

    # Chave inexiste na árvore
    if raiz is None:
        return None

    # Chave está na raiz
    if raiz.chave == chave:
        return raiz

    # Se existir, chave está na subárvore direita
    if chave > raiz.chave:
        return busca(raiz.direita, chave)

    # Se existir, chave está na subárvore esquerda
    return busca(raiz.esquerda, chave)

def minimo(raiz):
    nodo = raiz
    while nodo.esquerda is not None:
        nodo = nodo.esquerda
    return nodo.chave

def maximo(raiz):
    nodo = raiz
    while nodo.direita is not None:
        nodo = nodo.direita
    return nodo.chave

def identicas(a, b):

    # Ambas as árvores são vazias
    if a is None and b is None:
        return True

    # As árvores não são vazias, compara-as
    if not (a is None or b is None):
        return ((a.chave == b.chave) and
                identicas(a.esquerda, b.esquerda) and
                identicas(a.direita, b.direita))

    # Apenas uma das árvores é vazia
    return False

def altura(raiz):
    if raiz is None:
        return 0
    return max(altura(raiz.esquerda), altura(raiz.direita))

def is_balanceada(raiz):

    # Árvore binária vazia é balanceada
    if raiz is None:
        return True

    altura_esq = altura(raiz.esquerda)
    altura_dir = altura(raiz.direita)

    # Alturas diferem em mais de uma unidade
    if abs(altura_esq - altura_dir) > 1:
        return False

    return is_balanceada(raiz.esquerda) and is_balanceada(raiz.direita)

def pre_ordem(raiz):
    if not raiz:
        return

    # Visita nodo corrente.
    print(raiz.chave)

    # Visita filho da esquerda.
    pre_ordem(raiz.esquerda)

    # Visita filho da direita.
    pre_ordem(raiz.direita)

def em_ordem(raiz):
    if not raiz:
        return

    # Visita filho da esquerda.
    em_ordem(raiz.esquerda)

    # Visita nodo corrente.
    print(raiz.chave)

    # Visita filho da direita.
    em_ordem(raiz.direita)

def pos_ordem(raiz):
    if not raiz:
        return

    # Visita filho da esquerda.
    pos_ordem(raiz.esquerda)

    # Visita filho da direita.
    pos_ordem(raiz.direita)

    # Visita nodo corrente.
    print(raiz.chave)

# main

raiz = Nodo('A')

for k in ['B', 'C', 'D', 'E', 'F', 'G']:
    insere(raiz, Nodo(k))

for k in ['Y','G','A','F','C','W']:
    if busca(raiz, k):
        print('Chave "{}" encontrada'.format(k))
    else:
        print('Chave "{}" inexistente'.format(k))

#em_ordem(raiz)
