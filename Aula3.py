'''
ano_nascimento = input('Em que ano você nasceu? ')
print(type(ano_nascimento))
idade = 2022 - int(ano_nascimento)
print(type(idade))
print(idade)
'''

'''                    Index
   Palavra     Positivo     Negativo
      A             0           -7
      b             1           -6   
      a             2           -5
      c             3           -4
      a             4           -3
      t             5           -2
      e             6           -1'''

'''    
fruta = 'Abacate'
print(fruta[0])

valor = 99.75
valor = str(valor)
print(valor[3:5])
'''    

'''   
# O Marcos Silva é um excelente [Programador]
nome = 'Marcos'
sobrenome = 'Silva'
profissao = 'Programador'

texto = 'O ' + nome + ' ' + sobrenome + ' é um excelente [' + profissao + ']'
texto2 = f'O {nome} {sobrenome} é um excelente [{profissao}]'
print(texto)
print(texto2)
'''  

'''  
mensagem = '     Eu adoro comida Caseira'
print(mensagem)
print(mensagem.lower())
print(mensagem.upper())
print(mensagem.capitalize())
print(mensagem.find('c'))
print(mensagem.replace('Caseira', 'feita em casa'))
print(mensagem.strip())
'''  
'''  
calculo = 2 + 2 * 3 / 2
print(calculo)
calculo = (2 + 2) * 3 / 2
print(calculo)
calculo = 2 ** 3 + 4 # exponencial
print(calculo)
calculo = (2 + 2) ** 3 + 4 # exponencial
print(calculo)
'''  

equal = 10 == 10
notequal = 'banana' != 'Banana'
greater = 10 > 11
less = 10 < 11
greatequal = 10 >= 10
lessequal = 9 <= 9
print(equal)
print(notequal)
print(greater)
print(less)
print(greatequal)
greatequal = 10 >= 9
print(greatequal)
print(lessequal)
lessequal = 9 <= 27
print(lessequal)