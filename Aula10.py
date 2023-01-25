from array import array

# Tuples
  # Armazenar mais de uma informação em variáveis
  # Manter a sequência dos dados em uma variável
  # Não podem ser alterados (Immutable)

cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

# print(type(cores_list)) # pode ser alterada
# print(type(cores_tuple)) # é fixa

# Array
  # Similar a Listas
  # Melhor performance

letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

'''
print(letras)
print(numeros_i)
print(numeros_f)
print()
'''
letras = array('u', ['a', 'b', 'c', 'd']) # u = strings
numeros_i = array('i', [10, 20, 30, 40]) # i = num inteiro
numeros_f = array('f', [1.2, 2.2, 3.2]) # vlr flutuante
'''
print(letras)
print(numeros_i)
print(numeros_f)
'''

# Sets
  # Similar a listas
  # Evita itens duplicados
  # Não utiliza index

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]
'''
print(list1)
print(list2)
print()
'''
num1 = set(list1)
num2 = set(list2)
'''
print(num1 | num2) # union = junta as 2 listas, retirando os repetidos
print(num1 - num2) # difference = mostra as diferenças da lista 2 com a lista 1 (os que se repetem na lista 2 não vão ser mostrados no resultado) 
print(num1 ^ num2) # symetric Difference = retira todos os duplicados nas 2 listas (mostra os valores das duas listas, sem os valores que se repetem)
print(num1 & num2) # And = mostra o que é duplicado em ambas as listas
print(len(num1))
'''

list1 = [1, 2, 3, 4, 5, 6]
s1 = {1, 2, 3, 4, 5, 6, 1, 2}
s1.add(7)
s1.add(4)
s1.update({7, 8, 9, 10})
s1.remove(10) # gera erro se remover no set e não existir
s1.discard(9) # não gera erro ao remover do set e não existir
'''
print(list1)
print(s1)
print(type(list1))
print(type(s1))
'''

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.symmetric_difference(set3)#intersection(set2)#difference(set3)#union(set2)

print(set4)