import time

#Memoização - técnica para melhorar o desempenho de funções recursivas

def m_fatorial2(n, m = dict()):

    if n == 0:
        return 1
    else:
        if type(n) != type(1) or n < 0:
            return -1

        if m.get(n) == None:
          m[n] = n * m_fatorial2(n-1, m)

        return m[n]

def m_fatorial(n, check = True, m = dict()):
    
    if n == 0:
        return 1
    else:
        if check and (type(n) != type(1) or n < 0):
            return -1

        if m.get(n) == None:
          m[n] = n * m_fatorial(n-1, False, m)

        return m[n]

# Mesmas funções sem a memoização

def fatorial2(n):

    if n == 0:
        return 1
    else:
        if type(n) != type(1) or n < 0:
            return -1

        return n * fatorial2(n-1)


def fatorial(n, check = True):
    
    if n == 0:
        return 1
    else:
        if check and (type(n) != type(1) or n < 0):
            return -1

        return n * fatorial(n-1, False)

tempo2 = []
tempo1 = []

for i in range(10):
    ini = time.time()
    fatorial(900)
    fim = time.time()
    tempo2.append(fim-ini)

for i in range(10):
    ini = time.time()
    m_fatorial(900)
    fim = time.time()
    tempo1.append(fim-ini)

for x in range(10):
    print('tempo2: {:.20f}, tempo1: {:.20f}'.format(tempo2[x], tempo1[x]))
