###atividade-01_16/04/2025###
#Crie uma fila com 5 nomes. Mostre a fila e depois remova o primeiro nome (simulando atendimento).

# Criando uma fila com 5 nomes
fila = ["Eric", "Kratos", "Cleitao", "Mustang", "Torreto"]

# Mostrando a fila inicial
print("Fila inicial:", fila)

# Removendo o primeiro nome (simulando atendimento)
atendido = fila.pop(0)  # pop(0) remove o primeiro elemento

# Mostrando o resultado
print(f"\nAtendido: {atendido}")
print("Fila atualizada:", fila)

