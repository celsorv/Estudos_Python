"""

Matricula                      Funcionario                       Data    Hora  B Justf
--------------------------------------------------------------------------------------
000222     ANNELISE SOUZA DE COIMBRA                          06/01/2022 07:00 1 00000
0001196    Funcionário não encontrado                                      :   0 00000
--------------------------------------------------------------------------------------

Objetivo:
  Ler todos os arquivos log (.txt) existentes na pasta atual, gravando o con-
  teúdo destes em um único arquivo denominado 'saida.txt'.
  As linhas cuja coluna B (posição 79) não seja um dígito ou seja '0' serão descartadas.

"""

from os import listdir
from os.path import isfile, join

path = '.'

files = [f for f in listdir(path) if isfile(join(path, f)) and f[ len(f) - 3 : ] == 'txt']

with open('saida.txt', 'w') as outfile:
    for fname in files:
        with open(fname) as infile:
            for line in infile:
                if line[79] != '0' and line[79].isdigit():
                    outfile.write(line)

