from datetime import date

class Conversivel:

  @staticmethod
  def menor_para_maior(taxa, periodo):
    return ((1 + taxa / 100) ** periodo - 1) * 100

  @staticmethod
  def maior_para_menor(taxa, periodo):
    return ((1 + taxa / 100) ** (1 / periodo) - 1) * 100

class TaxaAno(Conversivel):

  @staticmethod
  def para_mes(taxa):
    return Conversivel.maior_para_menor(taxa, 12)

  def para_dia(taxa):
    return Conversivel.maior_para_menor(taxa, 360)

class TaxaMes(Conversivel):

  @staticmethod
  def para_ano(taxa):
    return Conversivel.menor_para_maior(taxa, 12)

  @staticmethod
  def para_dia(taxa):
    return Conversivel.maior_para_menor(taxa, 30)
    
class TaxaDia(Conversivel):

  @staticmethod
  def para_mes(taxa):
    return Conversivel.menor_para_maior(taxa, 30)

  @staticmethod
  def para_ano(taxa):
    return Conversivel.menor_para_maior(taxa, 360)

class JuroComposto:

  @staticmethod
  def juros(taxa, periodo, principal):
    montante = principal * ((1 + taxa / 100) ** periodo)
    return montante - principal

# MAIN

taxa_anual = TaxaDia.para_ano(.054)
print(taxa_anual)
