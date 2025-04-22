###atividade_02###
#Permita que o usuário insira quantos nomes quiser. Use "sair" como condição para parar. Ao final, mostre a fila.

 # Inicializando a fila vazia
fila = []

print("Digite os nomes para adicionar à fila (digite 'sair' para encerrar):")

# Loop para adicionar nomes até o usuário digitar "sair"
while True:
    nome = input("Nome: ")
    
    # Verifica se o usuário quer sair (case insensitive)
    if nome.lower() == 'sair':
        break
    
    # Adiciona o nome ao final da fila
    fila.append(nome)

# Mostra a fila final
print("\nFila completa:")
for i, nome in enumerate(fila, 1):
    print(f"{i}º - {nome}")
      