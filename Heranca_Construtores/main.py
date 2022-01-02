from datetime import date

class Funcionario:

    def __init__(self, nome='', admissao=date.today(), salario=0):
        self.nome = nome
        self.admissao = admissao
        self.salario = salario

    def setNome(self, nome):
        self.nome = nome;

    def setAdmissao(self, admissao):
        self.admissao = admissao;

    def setSalario(self, salario):
        self.salario = salario

    def get(self):
        return self.nome, self.admissao.strftime('%d/%m/%Y'), self.salario

    def __repr__(self):
        return '({},{},{})'.format(self.nome, self.admissao.strftime('%d/%m/%Y'), self.salario)

class Gerente(Funcionario):

    def __init__(self, nome='', admissao=date.today(), salario=0, bonus=0):
        Funcionario.__init__(self, nome, admissao, salario)
        self.bonus = bonus

    def __salario_bonificado(self):
        return self.salario * (1 + self.bonus / 100)

    def get(self):
        return self.nome, self.admissao.strftime('%d/%m/%Y'), Gerente.__salario_bonificado(self)

    def __repr__(self):
        return '({},{},{})'.format(self.nome, self.admissao.strftime('%d/%m/%Y'), Gerente.__salario_bonificado(self))


luiza = Gerente('Luiza', date.fromisoformat('2019-12-04'), 1000.00, 20.0)
paulo = Funcionario('Paulo', date.fromisoformat('2018-03-28'), 1000.00)

print()
print('%s admitido(a) em %s com salário de R$ %.2f' % luiza.get())
print('%s admitido(a) em %s com salário de R$ %.2f' % paulo.get())

