from sys import getsizeof # utilizado no Generator Expressions abaixo
'''
Lambda Functions
  É uma função (pequena) sem nome
  Pode ter vários argumentos, mas somente uma expressão
  Muito utilizada dentro de outras funções
  Código mais 'Clean'
'''

#def somar(x):
#  return x + 10
# print(somar(2))

#somar10 = lambda x: x + 10
#print(somar10(2))

def somar(x):
  func2 = lambda x: x + 10
  return func2(x) * 4

print(somar(2))

'''
Map Function
  Muito utilizado com listas
  Aplicar uma função a um Iterable, por item (list, tuple, dicionário, etc)

lista1 = [1, 2, 3, 4]
def multi(x):
  return x * 2
lista2 = map(multi, lista1)
lista2 = map(lambda x: x * 2, lista1)
print(list(lista2))

valores = [10, 12, 34, 44, 57]
def remover20(x):
  return x > 20
print(list(filter(remover20, valores)))
'''
print(list(map(lambda x: x * 2, [1, 2, 3, 4])))
print(list(filter(lambda x: x > 20, [10, 12, 34, 44, 57])))

'''
List Comprehension
  Mais simples de escrever
  Utilizado quando você precisa criar uma nova lista a partir de uma existente [expressao fot iten in itens]

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
frutas2 = [iten for iten in frutas1 if 'i' in iten]
for iten in frutas1:
  if 'n' in iten:
    frutas2.append(iten)

valores = []
for x in range(6):
  valores.append(x * 10)
print(valores)
'''
print([iten for iten in ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi'] if 'i' in iten])
print([x * 10 for x in range(6)])

'''
Generator Expressions
  Uma forma mais rápida para listas, dicionários e etc
  Menos memória alocada
  Valores em bytes
'''
#lista normalmente usada
numeros = [x * 10 for x in range(1000000)]
print(type(numeros))
#print(numeros)
print(getsizeof(numeros))
print('---------')
# generator expression : só altera o colchete [] para parênteses ()
numeros = (x * 10 for x in range(1000000))
print(type(numeros))
#print(list(numeros))
print(getsizeof(numeros))