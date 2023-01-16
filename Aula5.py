'''
for letra in 'Google':
  print(letra)

palavra = 'Google'

print('')
for letra in palavra:
  print(f'{letra} está dentro da palavra {palavra}')

compra_confirmada = true
dados_compra = 'Compra com valor de R$12.50 e entrega confirmada'
for enviar in range(3):
  if compra_confirmada:
    print(dados_compra)
    print('Detalhes enviados para o seu e-mail')
    break
else:
  print('Falha na compra')
for caixa in range(1,6):
  print(f'Caixa {caixa}')
  for produto in range(5):
    print(f'{caixa}: Produto {produto}')
palavra = 'FANTASTICO'
for espaco in palavra:
  print(f'{espaco} ', end='')    

linhas = 3
colunas = 10
simbolo = '@'

for l in range(linhas):
  for c in range(colunas):
    print(simbolo, end='')
  print()
valor = 100
dia = 1
while valor > 20:
  print(f'No dia {dia} o produto vai ser vendido por R$ {valor}')
  dia += 1
  valor -= 5
'''
valor = int(input('Digite o valor do seu produto: '))
while valor > 20:
  valor = (valor * 0.1) + valor
  print(f'O valor final do seu produto será de R$ {valor}')
  valor = int(input('Digite o valor do seu produto: '))