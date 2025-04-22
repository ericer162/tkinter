###atividade-09###
#9)Crie uma fila de embarque. Ao chamar passageiros, mostre quem foi chamado e quantos restam na fila.

from collections import deque
import time

class FilaEmbarque:
    def __init__(self):
        self.fila = deque()
        self.passageiros_embarcados = 0
    
    def adicionar_passageiro(self):
        nome = input("Digite o nome do passageiro: ").strip()
        if nome:
            self.fila.append(nome)
            print(f"Passageiro {nome} adicionado à fila. Posição: {len(self.fila)}")
        else:
            print("Nome do passageiro não pode estar vazio!")
    
    def chamar_embarque(self, quantidade=1):
        if not self.fila:
            print("Não há passageiros na fila de embarque!")
            return
        
        print("\n=== CHAMANDO PASSAGEIROS ===")
        for i in range(quantidade):
            if not self.fila:
                print("\nTodos os passageiros já foram chamados!")
                break
            
            passageiro = self.fila.popleft()
            self.passageiros_embarcados += 1
            print(f"\nChamando: {passageiro}")
            print(f"Passageiros embarcados: {self.passageiros_embarcados}")
            print(f"Passageiros restantes: {len(self.fila)}")
            time.sleep(1)  # Intervalo entre chamadas
        
        if self.fila:
            print(f"\nPróximo a ser chamado: {self.fila[0]}")
    
    def visualizar_fila(self):
        if not self.fila:
            print("A fila de embarque está vazia!")
            return
        
        print("\nFila de Embarque:")
        for i, passageiro in enumerate(self.fila, 1):
            print(f"{i}º - {passageiro}")
        print(f"\nTotal na fila: {len(self.fila)}")
        print(f"Já embarcaram: {self.passageiros_embarcados}")
    
    def menu(self):
        while True:
            print("\n" + "="*40)
            print("SISTEMA DE EMBARQUE".center(40))
            print("="*40)
            print("1. Adicionar passageiro")
            print("2. Chamar passageiros (1 por vez)")
            print("3. Chamar grupo (múltiplos passageiros)")
            print("4. Ver fila de embarque")
            print("0. Finalizar embarque")
            print("="*40)
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == '0':
                print("\n=== EMBARQUE CONCLUÍDO ===")
                print(f"Total de passageiros embarcados: {self.passageiros_embarcados}")
                if self.fila:
                    print(f"Passageiros restantes: {len(self.fila)}")
                break
            
            elif opcao == '1':
                self.adicionar_passageiro()
            
            elif opcao == '2':
                self.chamar_embarque()
            
            elif opcao == '3':
                try:
                    qtd = int(input("Quantos passageiros chamar? "))
                    self.chamar_embarque(qtd)
                except ValueError:
                    print("Digite um número válido!")
            
            elif opcao == '4':
                self.visualizar_fila()
            
            else:
                print("Opção inválida! Digite um número entre 0 e 4.")

# Iniciando o sistema
if __name__ == "__main__":
    print("=== SISTEMA DE FILA DE EMBARQUE ===")
    embarque = FilaEmbarque()
    embarque.menu()