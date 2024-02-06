'''
Criar um programa que dependendo da temperatura (em Celsius) do steak ele retorna o ponto de cozimento em português. O usuário deverá fornecer a temperatura.

Temperatura   | Cozimento
120ºF ou 48ºC | Rare (selada)
130ºF ou 54ºC | Medium rare (Ao ponto para o mal)
140ºF ou 60ºC | Medium (Ao ponto)
150ºF ou 65ºC | Medium well (Ao ponto para o bem)
160ºF ou 71ºC | Well done (Bem passada)
'''
'''
iPontoSteak = input('Digite a tempertatura do steak: ')
iPonto = int(iPontoSteak)
if iPonto < 48:
  print('Deixe mais tempo no fogo')
elif (iPonto >= 48) & (iPonto <= 53): # (iPonto in range(48, 53)) 
  print('Rare (selada)')
elif (iPonto >= 54) & (iPonto <= 59): # (iPonto in range(54, 59)) 
  print('Medium rare (Ao ponto para o mal)')
elif (iPonto >= 60) & (iPonto <= 63): # (iPonto in range(60, 63)) 
  print('Medium (Ao ponto)')
elif (iPonto >= 64) & (iPonto <= 70): # (iPonto in range(64, 70)) 
  print('Medium well (Ao ponto para o bem)')
elif (iPonto >= 71) & (iPonto <= 75): # (iPonto in range(71, 75)) 
  print('Well done (Bem passada)')
else:
  print('Queimou')
'''

'''
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede. O usuário deverá fornecer as seguintes informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem: 'Você necessita de x latas de tinta
'''
'''
def calc_rend(iRend, iAlt, iLarg):
  return (iAlt * iLarg) / iRend;
  
iRendimento = int(input('Qual o rendimento da lata? '));
iAltura = int(input('Qual a altura da parede? '));
iLargura = int(input('Qual a largura da parede? '));
iCalculo = calc_rend(iRendimento, iAltura, iLargura);
print(f'Você precisa de {iCalculo} latas de tinta')
'''

'''
Criar um programa que gera 3 listas de acordo com a nexessidade logo abaixo

Lista1 = Funcionários que tem carro e trabalham a noite
Lista2 = Funcionários que tem carro e trabalham durante o dia
Lista3 = Funcionários que não tem carro
'''
'''
funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']
# Forma 1 de fazer
#print(set(turno_noite) & set(tem_carro))
#print(set(turno_dia) & set(tem_carro))
#print(set(funcionarios) - set(tem_carro))
# Forma 2 de fazer
print(set(tem_carro).intersection(turno_noite))
print(set(tem_carro).intersection(turno_dia))
print(set(funcionarios).difference(tem_carro))
'''
'''
Calculo do IMC
  Menor que 18,5    | Magreza
  Entre 18,5 e 24,9 | Normal
  Entre 25,0 e 29,9 | Sobrepeso
  Entre 30,0 e 39,9 | Obesidade
  Maior que 40,0    | Obesidade Grave
'''
import math
fAltura = float(input('Informe sua altura em cm: '))
fPeso = float(input('Informe seu peso: '))
fIMC = fPeso / (math.pow(fAltura/100, 2))

if fIMC < 18.5:
  print(f'Seu IMC é {fIMC}. Magreza')
elif (fIMC >= 18.5) and (fIMC <= 24.9):
  print(f'Seu IMC é {fIMC}. Normal')
elif (fIMC >= 25.0) and (fIMC <= 29.9):
  print(f'Seu IMC é {fIMC}. Sobrepeso')
elif (fIMC >= 30.0) and (fIMC <= 39.9):
  print(f'Seu IMC é {fIMC}. Obesidade')
else:
  print(f'Seu IMC é {fIMC}. Obesidade Grave')

