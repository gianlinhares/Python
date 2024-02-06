'''
# import funcoes # importa todas as funções que estão no arquivo funcoes.py
from funcoes import somar, multi; # importa somente as funções escolhidas do arquivo funcoes.py
from items.cadastro import cliente;
somar();
multi();
cliente();
'''

from funcoes import find_index;

list1 =['a', 'b', 'c', 'd', 'e'];

var1 = find_index(list1, 'b')
print(var1)