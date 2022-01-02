#
# Obtém as palavras reais do texto (sem os sinais de pontuação)
#

'Modo otimizado com o método translate()'

def palavras_otm(filename):


  palavras = []
  trans = str.maketrans('.,;?!:()[]{}"', 13*' ')

  hFile = open(filename, 'r', encoding = 'UTF-8')
  
  for line in hFile:
    palavras = palavras + line.translate(trans).split()

  hFile.close()

  return palavras


def palavras(filename):

    hFile = open(filename, 'r', encoding = 'UTF-8')

    palavras = []

    for line in hFile:
        for x in line.split():
            if x != '\n':
                palavras.append(remove_pontuacao(x))
            
    hFile.close()

    return palavras

def remove_pontuacao(palavra):

    simbolos = '.,;?!:()[]\{\}"'

    while palavra[0] in simbolos:
        palavra = palavra[1:]

    while palavra[len(palavra)-1] in simbolos:
        palavra = palavra[:len(palavra)-1]

    return palavra



print('\n' + '-'*30)

for x in palavras_otm('teste_palavras.txt'):
    print(x)
    
print('-'*30)
