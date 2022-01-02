#
# Simulando duas filas bancárias: prioritária e normal
#
# A cada 2 pessoas que saem da fila prioritária 
# (+60 anos), uma sai da fila normal.
#
#

import random

class Fila():

    def __init__(self):
        self.data = []

    def insert(self, x):
        self.data.append(x)

    def remove(self):
        if len(self.data) > 0:
            return self.data.pop(0)

    def top(self):
        if len(self.data) > 0:
            return self.data[0]

    def empty(self):
        return len(self.data) == 0

fila_normal = Fila()
fila_priori = Fila()
qtde_prioritario = 0

nomes = '''
Paula Julia Marcos Antonio Giovana Aline Alison Áurea Fátima 
Jaqueline Roberval Rubens Amilton Alessandra Hortência Heitor 
Fabiana Joice Gilmar Juvenal Olavo Odete Orlando Aline Nice
'''.split()

for i in range(25):
    y = random.randint(15, 95)
    if y < 60:
        fila_normal.insert([nomes[i], y])
    else:
        fila_priori.insert([nomes[i], y])

print('\nFILA DE ATENDIMENTO:\n')

while not (fila_priori.empty() and fila_normal.empty()):

    pessoa = None
    prioritario = False

    if qtde_prioritario < 2 or fila_normal.empty():
        if not fila_priori.empty():
            pessoa = fila_priori.remove()
            qtde_prioritario += 1
            prioritario = True

    if pessoa == None:
        pessoa = fila_normal.remove()
        qtde_prioritario = 0

    print((pessoa[0] + ' (' + str(pessoa[1]) + ' anos)').ljust(20), '*PRIORITY*' if prioritario else '')

