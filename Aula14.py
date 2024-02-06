from datetime import datetime
# criar a classe
class Funcionarios:
  def __init__(self, nome, sobrenome, ano_nascimento):
    self.nome = nome
    self.sobrenome = sobrenome
    self.ano_nascimento = ano_nascimento

  def nome_completo(self):
    return self.nome + ' ' + self.sobrenome

  def idade_funcionario(self):
    ano_atual = datetime.now().year
    self.ano_nascimento = int(ano_atual - self.ano_nascimento)
    return self.ano_nascimento

# criar o objeto
usuario1 = Funcionarios('Gianluca', 'Linhares', 1991)
usuario2 = Funcionarios('Verônica', 'Datsch', 1990)

# print
print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario2))

print(Funcionarios.idade_funcionario(usuario1))
print(Funcionarios.idade_funcionario(usuario2))
'''
usuario1 = Funcionarios()
usuario2 = Funcionarios()

# criar os parâmetros do usuario 1
usuario1.nome = 'Gianluca'
usuario1.sobrenome = 'Linhares'
usuario1.data_nascimento = '09/01/1991'

# criar os parâmetros do usuario 2
usuario2.nome = 'Verônica'
usuario2.sobrenome = 'Datsch'
usuario2.data_nascimento = '02/08/1990'

# print
print(usuario1.nome)
print(usuario2.nome)
'''