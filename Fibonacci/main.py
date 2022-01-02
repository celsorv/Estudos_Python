#
# n-ésimo termo da sequência de Fibonacci
# Recursão versus Iteração
#

import time

# Memoização - técnica para melhorar o desempenho de funções recursivas


# modo recursivo
def fib_rec(n):
  if n < 2:
    return n
  return fib_rec(n - 1) + fib_rec(n - 2)

# modo recursivo com memoização
def m_fib_rec(n, m = dict()):

  if n < 2:
    return n

  if m.get(n) == None:
    m[n] = m_fib_rec(n - 1) + m_fib_rec(n - 2)

  return m[n]


# modo iterativo
def fib_it(n):
  res = n
  a, b = 0, 1
  for k in range(2, n + 1):
    res = a + b
    a, b = b, res
  return res

print('Teste de desempenho:\n')

n = 35

tempo_i = time.time()
print(fib_it(n))
print('Iterative: {} seconds'.format(time.time() - tempo_i))

tempo_i = time.time()
print(m_fib_rec(n))
print('Memoization: {} seconds'.format(time.time() - tempo_i))

tempo_i = time.time()
print(fib_rec(n))
print('Recursive: {} seconds'.format(time.time() - tempo_i))