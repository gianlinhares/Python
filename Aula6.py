# Functions
# DRY - Don't Repeat Yourself
# Parâmetro -> Argumento
# Default: define valor no parâmetro
# Non-Default: não define o valor no parâmetro
# xargs: quando serão passados vários argumentos (podem ser de 2 até o infinito)
def boas_vindas(sPessoa, iQtd = 0): #def = define (criação da função)
  print(f'Olá {sPessoa}!')
  if iQtd > 0:
    print(f'Temos {str(iQtd)} laptops em estoque')
    print()
boas_vindas('Gianluca', 3)
boas_vindas('Verônica')
def somar_dois_numeros(numero1, numero2):
  resultado = numero1 + numero2
  print(resultado)
somar_dois_numeros(4, 7)
def cliente(sNome):
  # print(f'Olá {sNome} =)')
  return f'Olá {sNome} =)'
print(cliente('Gianluca'))
def soma(*iNumeros):
  iResult = 0 #zera a variável para iniciar o for
  for iNum in iNumeros: # Percorre todos os valores que forem informados
    iResult += iNum # soma os valores que forem informados na função
  return iResult
print(soma(2, 3, 4, 7))
def agencia(**carros):
  return carros

print(agencia(marca = 'Gol', cor = 'Branca', motor = 1.0))
print(agencia(marca = 'Gol', cor = 'Azul', motor = 1.0, placa = 1234))
print(agencia(marca = 'Gol', cor = 'Preta'))
