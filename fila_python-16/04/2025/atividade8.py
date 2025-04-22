###atividade-08###
#8)Simule uma fila de impressão de documentos. Cada documento tem um nome. Ao imprimir, remova o primeiro.

from collections import deque
import time  # Para simular o tempo de impressão

class FilaImpressao:
    def __init__(self):
        self.fila = deque()
    
    def adicionar_documento(self):
        documento = input("Digite o nome do documento a ser adicionado: ").strip()
        if documento:
            self.fila.append(documento)
            print(f"Documento '{documento}' adicionado à fila de impressão. Posição: {len(self.fila)}")
        else:
            print("O nome do documento não pode estar vazio!")
    
    def imprimir_documento(self):
        if not self.fila:
            print("Não há documentos na fila de impressão!")
            return
        
        documento = self.fila.popleft()
        print(f"\nImprimindo documento: {documento}...")
        time.sleep(2)  # Simula o tempo de impressão
        print(f"Documento '{documento}' impresso com sucesso!")
        print(f"Documentos restantes na fila: {len(self.fila)}")
    
    def visualizar_fila(self):
        if not self.fila:
            print("A fila de impressão está vazia!")
            return
        
        print("\nFila de Impressão:")
        for i, doc in enumerate(self.fila, 1):
            print(f"{i}º - {doc}")
        print(f"Total de documentos: {len(self.fila)}")
    
    def menu(self):
        while True:
            print("\n" + "="*40)
            print("FILA DE IMPRESSÃO".center(40))
            print("="*40)
            print("1. Adicionar documento")
            print("2. Imprimir próximo documento")
            print("3. Ver fila de impressão")
            print("0. Sair")
            print("="*40)
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == '0':
                print("Encerrando o sistema de impressão...")
                break
            elif opcao == '1':
                self.adicionar_documento()
            elif opcao == '2':
                self.imprimir_documento()
            elif opcao == '3':
                self.visualizar_fila()
            else:
                print("Opção inválida! Digite um número entre 0 e 3.")

# Iniciando o sistema
if __name__ == "__main__":
    impressora = FilaImpressao()
    impressora.menu()