'''
cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20, 30, 40]
duas_listas = zip(cores, valores)
print(list(duas_listas))
'''
frutas_usuario = input('Digite o nome das frutas separadas por vírgula: ')
frutas_lista = frutas_usuario.split(', ')

print(frutas_lista)