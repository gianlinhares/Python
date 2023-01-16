'''
x = 10
x = x + 5
x += 5
x -= 5
x *= 5
x /= 5
x %= 4
print (x)

velocidade = 100

if velocidade > 110:
  print('Acima da velocidade permitida')
  print('Favor reduzir a sua velocidade')
elif velocidade < 60:
  print('Favor dirigir acima de 80km/h')
else:
  print('Velocidade OK')

print('Fim')

renda_acima_5mil = True
nome_limpo = True

if renda_acima_5mil and nome_limpo:
  print('Financiamento Aprovado')
else:
  print('Financiamento Negado')

#operador ternário
idade = 14
resultado = 'Voto permitido' if idade >= 16 else 'Voto não permitido'
print(resultado)

#Diferença de representação do if
valor = 39
#if valor >= 20 and valor < 40:
if 20 <= valor < 40:
  print('Produto foi aceito')
else:
  print('Produto não foi aceito')
'''

for numero in range(5):
  print(numero)
print('')
for numero in range(1, 20, 2):
  print(numero)