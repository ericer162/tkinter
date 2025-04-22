###atividade-07###
#7)Permita pesquisar se um item está ou não na fila. Exiba mensagem: “X está na fila” ou “X não encontrado”.

from collections import deque

class FilaCompras:
    def __init__(self):
        self.fila = deque()
    
    def adicionar_produto(self):
        produto = input("Digite o nome do produto a ser adicionado: ").strip()
        if produto:
            self.fila.append(produto)
            print(f"'{produto}' foi adicionado à lista de compras. Total: {len(self.fila)}")
        else:
            print("Nome do produto não pode estar vazio!")
    
    def comprar_produto(self):
        if not self.fila:
            print("A lista de compras está vazia!")
            return
        
        produto = self.fila.popleft()
        print(f"\nProduto comprado: {produto}")
        print(f"Produtos restantes na lista: {len(self.fila)}")
    
    def pesquisar_produto(self):
        if not self.fila:
            print("A lista de compras está vazia!")
            return
        
        produto = input("Digite o nome do produto a pesquisar: ").strip()
        if produto in self.fila:
            print(f"'{produto}' está na lista de compras (posição {list(self.fila).index(produto) + 1})")
        else:
            print(f"'{produto}' não encontrado na lista de compras")
    
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
            print("3. Pesquisar produto")
            print("4. Ver lista de compras")
            print("5. Limpar lista")
            print("0. Sair")
            print("="*40)
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == '0':
                print("Saindo do sistema de compras...")
                break
            elif opcao == '1':
                self.adicionar_produto()
            elif opcao == '2':
                self.comprar_produto()
            elif opcao == '3':
                self.pesquisar_produto()
            elif opcao == '4':
                self.visualizar_lista()
            elif opcao == '5':
                self.limpar_lista()
            else:
                print("Opção inválida! Digite um número entre 0 e 5.")

# Iniciando o sistema
if __name__ == "__main__":
    sistema = FilaCompras()
    sistema.menu()