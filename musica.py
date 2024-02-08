from pydub import AudioSegment
from pydub.generators import Sine
import math
'''
# Definindo os parâmetros da música
duracao_tom = 500  # duração em milissegundos

frequencia_tom1 = 110  # frequência do primeiro tom em Hz (nota A4)
frequencia_tom2 = 220  # frequência do segundo tom em Hz (nota A5)
frequencia_tom3 = 440
frequencia_tom4 = 880
frequencia_tom5 = 1760
frequencia_tom6 = 3520
frequencia_tom7 = 7040
frequencia_tom8 = 14080

# Criando os tons
sine_tom1 = Sine(frequencia_tom1).to_audio_segment(duration=duracao_tom)
sine_tom2 = Sine(frequencia_tom2).to_audio_segment(duration=duracao_tom)
sine_tom3 = Sine(frequencia_tom3).to_audio_segment(duration=duracao_tom)
sine_tom4 = Sine(frequencia_tom4).to_audio_segment(duration=duracao_tom)
sine_tom5 = Sine(frequencia_tom5).to_audio_segment(duration=duracao_tom)
sine_tom6 = Sine(frequencia_tom6).to_audio_segment(duration=duracao_tom)
sine_tom7 = Sine(frequencia_tom7).to_audio_segment(duration=duracao_tom)
sine_tom8 = Sine(frequencia_tom8).to_audio_segment(duration=duracao_tom)

# Criando a música
musica = sine_tom1 + sine_tom2 + sine_tom3 + sine_tom4 + sine_tom5 + sine_tom6 + sine_tom7 + sine_tom8
musica = 0
for i in range(1, 441):
  musica += Sine(i).to_audio_segment(duration = 110)
'''
musica = 0
# Frequência da nota C4 (em Hz)
frequencia_C4 = 261.63

fator_do = 2**(1 / 12)
fator_re = 2**(2 / 12)  # 2 meios-tons acima da nota Dó
fator_mi = 2**(4 / 12)  # 4 meios-tons acima da nota Dó
fator_fa = 2**(5 / 12)  # 5 meios-tons acima da nota Dó
fator_sol = 2**(7 / 12)  # 7 meios-tons acima da nota Dó
fator_la = 2**(9 / 12)  # 9 meios-tons acima da nota Dó
fator_si = 2**(11 / 12)  # 11 meios-tons acima da nota Dó

# Frequência da nota Dó (C) na mesma oitava
frequencia_Do = frequencia_C4 * fator_do
# Frequência da nota Ré (D) na mesma oitava
frequencia_Re = frequencia_C4 * fator_re
# Frequência da nota Mi (E) na mesma oitava
frequencia_Mi = frequencia_C4 * fator_mi
# Frequência da nota Fá (F) na mesma oitava
frequencia_Fa = frequencia_C4 * fator_fa
# Frequência da nota Sol (G) na mesma oitava
frequencia_Sol = frequencia_C4 * fator_sol
# Frequência da nota Lá (A) na mesma oitava
frequencia_La = frequencia_C4 * fator_la
# Frequência da nota Si (B) na mesma oitava
frequencia_Si = frequencia_C4 * fator_si

# Duração da nota em milissegundos
duracao = 480

do = Sine(frequencia_Do).to_audio_segment(duration=duracao)
re = Sine(frequencia_Re).to_audio_segment(duration=duracao)
mi = Sine(frequencia_Mi).to_audio_segment(duration=duracao)
fa = Sine(frequencia_Fa).to_audio_segment(duration=duracao)
sol = Sine(frequencia_Sol).to_audio_segment(duration=duracao)
la = Sine(frequencia_La).to_audio_segment(duration=duracao)
si = Sine(frequencia_Si).to_audio_segment(duration=duracao)

# Convertendo a onda senoidal em um segmento de áudio com a duração especificada
# musica = onda_do + onda_re + onda_mi + onda_fa + onda_sol + onda_la + onda_si
'''
DO-DO-RE-DO-FA-MI
DO-DO-RE-DO-SOL-FA
LA-LA-DO-LA-FA-MI-RE
LA-LA-SOL-FA-SOL-FA
'''

primeira_estrofe = do + do + re + do + fa + mi
segunda_estrofe = do + do + re + do + sol + fa
terceira_estrofe = la + la + do + la + fa + mi + re
quarta_estrofe = la + la + sol + fa + sol + fa
musica = primeira_estrofe + segunda_estrofe + terceira_estrofe + quarta_estrofe

#musica = do + re + mi + fa + fa + fa + do + re + do + re + re + re + sol + fa + mi + mi + mi + do  + re + mi + fa + fa + fa

# Salvando a música em um arquivo
musica.export("minha_musica.mp3", format="mp3")

print("Música criada com sucesso!")

'''
# Frequências das notas da melodia de "Nemo" (em Hz)
notas_nemo = [329.63, 349.23, 329.63, 293.66, 261.63, 293.66, 329.63, 349.23, 392.00, 349.23, 329.63, 293.66, 261.63, 293.66, 329.63, 349.23, 392.00, 349.23, 329.63, 293.66, 329.63, 392.00, 440.00]

# Duração de cada nota (em milissegundos)
duracao_nota = 500

# Criando a sequência de notas musicais
melodia_nemo = AudioSegment.empty()
for frequencia in notas_nemo:
    nota = Sine(frequencia).to_audio_segment(duration=duracao_nota)
    melodia_nemo += nota

# Salvando a melodia em um arquivo
melodia_nemo.export("melodia_nemo.wav", format="wav")

print("Melodia de 'Nemo' criada com sucesso!")


from pydub.generators import Sawtooth
import random

# Definindo parâmetros
duração_total = 10000  # 10 segundos
duração_compasso = 500   # 0.5 segundos por compasso
#notas = [220, 330, 440, 550]  # Frequências das notas
notas = [273, 322, 441, 587]  # Frequências das notas
# Criando o segmento de áudio
música_eletrônica = AudioSegment.empty()

# Gerando o padrão da música eletrônica
for _ in range(int(duração_total / duração_compasso)):
    nota = random.choice(notas)
    onda = Sawtooth(nota).to_audio_segment(duration=duração_compasso)
    música_eletrônica += onda

# Exportando o segmento de áudio para um arquivo
música_eletrônica.export("música_eletrônica.mp3", format="mp3")

print("Música eletrônica criada com sucesso!")
'''