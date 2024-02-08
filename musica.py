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
duracao = 1000

onda_do = Sine(frequencia_Do).to_audio_segment(duration=duracao)
onda_re = Sine(frequencia_Re).to_audio_segment(duration=duracao)
onda_mi = Sine(frequencia_Mi).to_audio_segment(duration=duracao)
onda_fa = Sine(frequencia_Fa).to_audio_segment(duration=duracao)
onda_sol = Sine(frequencia_Sol).to_audio_segment(duration=duracao)
onda_la = Sine(frequencia_La).to_audio_segment(duration=duracao)
onda_si = Sine(frequencia_Si).to_audio_segment(duration=duracao)

# Convertendo a onda senoidal em um segmento de áudio com a duração especificada
# musica = onda_do + onda_re + onda_mi + onda_fa + onda_sol + onda_la + onda_si
'''
DO-DO-RE-DO-FA-MI
DO-DO-RE-DO-SOL-FA
LA-LA-DO-LA-FA-MI-RE
LA-LA-SOL-FA-SOL-FA
'''

primeira_estrofe = onda_do + onda_do + onda_re + onda_do + onda_fa + onda_mi
segunda_estrofe = onda_do + onda_do + onda_re + onda_do + onda_sol + onda_fa
terceira_estrofe = onda_la + onda_la + onda_do + onda_la + onda_fa + onda_mi + onda_re
quarta_estrofe = onda_la + onda_la + onda_sol + onda_fa + onda_sol + onda_fa
musica = primeira_estrofe + segunda_estrofe + terceira_estrofe + quarta_estrofe

# Salvando a música em um arquivo
musica.export("minha_musica.mp3", format="mp3")

print("Música criada com sucesso!")
