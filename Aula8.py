# Listas
cidades = ['Santa Cruz do Sul', 'Erechim', 'Passo Fundo']
cidades.append('Lajeado') # Adicionar na lista na última posição
cidades.insert(4, 'Porto Alegre') # Adiciona em uma posição específica
#cidades.remove('Erechim') # Remove da Lista pelo item
#cidades[0] = 'Curitiba' # Altera o item da lista 
#cidades.pop(1) # Remove da lista pelo índice
cidades.sort() # Ordena a lista
print(cidades)
# Concatenação de Listas
numeros = [1, 2, 3, 4]
letras = ['a', 'b', 'c', 'd']
final1 = numeros * 2 # Multiplica os valores da lista
final2 = numeros = letras # Soma as duas listas
final3 = [[1, 2], [3, 4]] # Cria sublistas
print(final1)
print(final2)
print(final3[1][1])
print(final3[0][0])
# Extraindo valores de uma lista
produtos = ['arroz', 'feijão', 'laranja', 'banana', 1, 2, 3, 4]
item1, item2, item3, *outros = produtos
''' É o mesmo que:
item1 = produtos[0]
item2 = produtos[1]
item3 = produtos[2]
item4 = produtos[3]
'''
print(item1)
print(item2)
print(item3)
print(outros)
#Loop em uma lista
valores = [50, 80, 110, 150, 170]
for x in valores:
  print(f'O valor final do produto é de R$ {x}.')
cor_cliente = input('Digite a cor desejada: ')
cores = ['amarelo', 'verde', 'azul', 'vermelho']
if cor_cliente.lower() in cores:
  print('Em estoque')
else:
  print('Não temos esta cor em estoque')