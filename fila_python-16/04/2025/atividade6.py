###atividade-06###
#6)Crie uma fila de compras (nomes de produtos). Ao remover, informe qual produto foi comprado.

from collections import deque

class FilaCompras:
    def __init__(self):
        self.fila = deque()
    
    def adicionar_produto(self):
        produto = input("Digite o nome do produto a ser adicionado: ")
        self.fila.append(produto)
        print(f"'{produto}' foi adicionado à lista de compras. Total: {len(self.fila)}")
    
    def comprar_produto(self):
        if not self.fila:
            print("A lista de compras está vazia!")
            return
        
        produto = self.fila.popleft()
        print(f"\nProduto comprado: {produto}")
        print(f"Produtos restantes na lista: {len(self.fila)}")
    
    def visualizar_lista(self):
        if not self.fila:
            print("Sua lista de compras está vazia!")
            return
        
        print("\nLista de Compras:")
        for i, produto in enumerate(self.fila, 1):
            print(f"{i}º - {produto}")
        print(f"Total de produtos: {len(self.fila)}")
    
    def limpar_lista(self):
        self.fila.clear()
        print("Lista de compras foi completamente esvaziada!")
    
    def menu(self):
        while True:
            print("\n" + "="*40)
            print("LISTA DE COMPRAS".center(40))
            print("="*40)
            print("1. Adicionar produto")
            print("2. Comprar próximo produto")
            print("3. Ver lista de compras")
            print("4. Limpar lista")
            print("0. Sair")
            print("="*40)
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '0':
                print("Saindo do sistema de compras...")
                break
            elif opcao == '1':
                self.adicionar_produto()
            elif opcao == '2':
                self.comprar_produto()
            elif opcao == '3':
                self.visualizar_lista()
            elif opcao == '4':
                self.limpar_lista()
            else:
                print("Opção inválida! Digite um número entre 0 e 4.")

# Iniciando o sistema
if __name__ == "__main__":
    sistema = FilaCompras()
    sistema.menu()