###atividade-03###
#3)Simule uma fila de senhas de atendimento. Cada novo nome recebe uma senha numérica sequencial.

from collections import deque

class FilaAtendimento:
    def __init__(self):
        self.fila = deque()
        self.contador_senha = 1
    
    def pegar_senha(self, nome):
        senha = self.contador_senha
        self.fila.append((senha, nome))
        print(f"Senha gerada: {senha} para {nome}")
        self.contador_senha += 1
    
    def chamar_proximo(self):
        if not self.fila:
            print("Não há clientes na fila!")
            return
        
        senha, nome = self.fila.popleft()
        print(f"\nSenha chamada: {senha}")
        print(f"Cliente atendido: {nome}")
        print(f"Clientes restantes: {len(self.fila)}")
    
    def mostrar_fila(self):
        if not self.fila:
            print("A fila está vazia!")
            return
        
        print("\nFila de atendimento:")
        for i, (senha, nome) in enumerate(self.fila, 1):
            print(f"{i}º - Senha {senha}: {nome}")

# Programa principal
fila = FilaAtendimento()

print("Sistema de Senhas de Atendimento")
print("Digite 'sair' para encerrar\n")

while True:
    print("\nOpções:")
    print("1 - Pegar senha")
    print("2 - Chamar próximo")
    print("3 - Ver fila")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '0':
        print("Encerrando o sistema...")
        break
    
    elif opcao == '1':
        nome = input("Digite seu nome: ")
        if nome.lower() == 'sair':
            print("Operação cancelada")
            continue
        fila.pegar_senha(nome)
    
    elif opcao == '2':
        fila.chamar_proximo()
    
    elif opcao == '3':
        fila.mostrar_fila()
    
    else:
        print("Opção inválida! Tente novamente.")