# Dicionários
  # Utiliza index no formato de Keys e Values
  # Aceita string, integer, float, boolean...

# Exemplo de dicionário
aluno = {
  'nome': 'Ana', 
  'idade': 16, 
  'nota_final': 'A', 
  'aprovação': True, 
  'materias':['fisica', 'matematica', 'ingles']
}

# aluno['nome'] = 'Jose' # Atualiza um único item
# aluno.update({'nome': 'Jose', 'nota_final': 'B'}) # Atualiza vários itens ao mesmo tempo
# aluno.update({'endereco': 'Rua A'}) # se não existir, vai adicionar
# del aluno['idade'] # apaga um dado do dicionário
#print(aluno.get('endereco', 'Não existe')) # .get é possível dar uma mensagem de tratamento no dicionário

#for keys, values in aluno.items():
#  print(keys, values)

print(aluno.items())
print(aluno.keys())
print(aluno.values())