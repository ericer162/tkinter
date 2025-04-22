###atividade-04###
#4)Crie uma fila de tarefas. Ao atender uma tarefa (remover da fila), mostre qual foi e quantas ainda restam.

from collections import deque

class FilaTarefas:
    def __init__(self):
        self.fila = deque()
    
    def adicionar_tarefa(self, tarefa):
        self.fila.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada. Total na fila: {len(self.fila)}")
    
    def atender_tarefa(self):
        if not self.fila:
            print("Não há tarefas na fila!")
            return None
        
        tarefa = self.fila.popleft()
        print(f"\nTarefa atendida: {tarefa}")
        print(f"Tarefas restantes: {len(self.fila)}")
        return tarefa
    
    def mostrar_fila(self):
        if not self.fila:
            print("A fila de tarefas está vazia!")
            return
        
        print("\nFila de Tarefas:")
        for i, tarefa in enumerate(self.fila, 1):
            print(f"{i}º - {tarefa}")

# Exemplo de uso
fila = FilaTarefas()

print("Sistema de Gerenciamento de Tarefas")
print("Digite 'sair' para encerrar\n")

while True:
    print("\nOpções:")
    print("1 - Adicionar tarefa")
    print("2 - Atender próxima tarefa")
    print("3 - Ver fila de tarefas")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '0':
        print("Encerrando o sistema...")
        break
    
    elif opcao == '1':
        tarefa = input("Digite a tarefa a ser adicionada: ")
        if tarefa.lower() == 'sair':
            print("Operação cancelada")
            continue
        fila.adicionar_tarefa(tarefa)
    
    elif opcao == '2':
        fila.atender_tarefa()
    
    elif opcao == '3':
        fila.mostrar_fila()
    
    else:
        print("Opção inválida! Tente novamente.")