# --------------------------------------------------------
# Cruza arquivos Main Clarion e gera relação de procedures
# --------------------------------------------------------
#

import re

def Merge(dict1, dict2):
  return {**dict1, **dict2}

modules_list = [{}, {}]
source_files = ['fecha.clw', 'pfech.clw']
out_filename = './report.txt'

# -------------------------------------------------
#  Obtém nomes de procedures e módulos (input file)
# -------------------------------------------------
#
for index, filename in enumerate(source_files):

  module_found = None

  with open(filename) as infile:
    for line in infile:

      if not module_found:
        result = re.search(r"MODULE\('(.+)'\)", line)
        module_found = result.group(1) if result else None
        continue

      result = re.search(r"(\w+).*", line)
      procedure_name = result.group(1)

      modules_list[index][procedure_name] = module_found

      module_found = None

# -------------------------------------------------
#  Cria relação de procedures/módulos (output file)
# -------------------------------------------------
#
with open(out_filename, 'w') as outfile:

  # Cabeçalho
  #
  str = 'Procedure Name'.ljust(31) + source_files[0].ljust(16) + source_files[1].ljust(15)
  outfile.write(str + '\n')
  str = '-' * 30 + ' ' + '-' * 15 + ' ' + '-' * 15
  outfile.write(str + '\n')

  for procedure_name in Merge(modules_list[0], modules_list[1]).keys():
    
    str = procedure_name.ljust(30)
    
    is_found = modules_list[0].get(procedure_name)
    str += ' ' + (is_found if is_found else '--//--').ljust(15)

    is_found = modules_list[1].get(procedure_name)
    str += ' ' + (is_found if is_found else '--//--').ljust(15)

    outfile.write(str + '\n')
