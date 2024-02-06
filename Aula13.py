# Erros
  # Excelentes para testes
  # Não param o programa
  # Mensagem customizada quando encontra o erro

try:
  letras = ['a', 'b', 'c']
  print(letras[3])
except IndexError:
  print('Index fora da faixa')
print(letras)
print('')

try:
  valor = int(input('Digite o valor do seu produto: '))
  print(valor)
except ValueError:
  print('Favor digitar um valor em números')
finally:
  print('Código ok')
'''
else:
  print('Usuário digitou um valor correto')
  resultado = valor * 2
  print(resultado)
'''  
print('Mais código abaixo')