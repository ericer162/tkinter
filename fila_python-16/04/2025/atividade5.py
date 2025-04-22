###atividade-05###
#5)Implemente um menu com as opções: adicionar, remover, visualizar fila, limpar fila, sair.

from collections import deque

class SistemaFila:
    def __init__(self):
        self.fila = deque()
    
    def adicionar(self):
        item = input("Digite o item a ser adicionado: ")
        self.fila.append(item)
        print(f"'{item}' foi adicionado à fila. Total: {len(self.fila)}")
    
    def remover(self):
        if not self.fila:
            print("A fila está vazia!")
            return
        
        item = self.fila.popleft()
        print(f"Item removido: {item}")
        print(f"Itens restantes: {len(self.fila)}")
    
    def visualizar(self):
        if not self.fila:
            print("A fila está vazia!")
            return
        
        print("\nFila atual:")
        for posicao, item in enumerate(self.fila, 1):
            print(f"{posicao}º - {item}")
        print(f"Total de itens: {len(self.fila)}")
    
    def limpar(self):
        self.fila.clear()
        print("Fila foi completamente esvaziada!")
    
    def menu(self):
        while True:
            print("\n" + "="*40)
            print("MENU DA FILA".center(40))
            print("="*40)
            print("1. Adicionar item")
            print("2. Remover item")
            print("3. Visualizar fila")
            print("4. Limpar fila")
            print("0. Sair")
            print("="*40)
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '0':
                print("Encerrando o sistema...")
                break
            elif opcao == '1':
                self.adicionar()
            elif opcao == '2':
                self.remover()
            elif opcao == '3':
                self.visualizar()
            elif opcao == '4':
                self.limpar()
            else:
                print("Opção inválida! Tente novamente.")

# Iniciando o sistema
if __name__ == "__main__":
    sistema = SistemaFila()
    sistema.menu()