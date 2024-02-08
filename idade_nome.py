import datetime
# Obter o ano atual
ano_atual = datetime.datetime.now().year
print("O ano atual é:", ano_atual)
ano_nascimento = input('Em que ano você nasceu? ')
idade = ano_atual - int(ano_nascimento)
print(idade)
nome = input('Digite o nome: ')
for letra in nome:
  print(letra)