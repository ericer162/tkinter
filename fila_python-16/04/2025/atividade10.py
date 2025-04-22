###atividade-10###
#10)Desafio: Implemente uma fila com tempo de espera simulado (use time.sleep()) ao atender cada item.

from collections import deque
import time
import random

class FilaEspera:
    def __init__(self):
        self.fila = deque()
        self.tempo_total_espera = 0
    
    def adicionar_item(self, item=None):
        if not item:
            item = input("Digite o item a ser adicionado: ").strip()
            if not item:
                print("O item não pode estar vazio!")
                return
        
        tempo_processamento = random.randint(1, 5)  # Tempo aleatório entre 1-5 segundos
        self.fila.append((item, tempo_processamento))
        print(f"'{item}' adicionado. Tempo estimado: {tempo_processamento}s. Posição: {len(self.fila)}")
    
    def atender_item(self):
        if not self.fila:
            print("A fila está vazia!")
            return None
        
        item, tempo = self.fila.popleft()
        print(f"\nAtendendo: {item} (Tempo estimado: {tempo}s)")
        
        # Simulação do tempo de processamento
        for i in range(tempo, 0, -1):
            print(f"Tempo restante: {i}s", end='\r')
            time.sleep(1)
        
        self.tempo_total_espera += tempo
        print(f"\nItem '{item}' atendido com sucesso!")
        print(f"Itens restantes: {len(self.fila)}")
        print(f"Tempo total de espera acumulado: {self.tempo_total_espera}s")
        
        if self.fila:
            proximo_item, proximo_tempo = self.fila[0]
            print(f"Próximo item: '{proximo_item}' (Tempo estimado: {proximo_tempo}s)")
        
        return item
    
    def visualizar_fila(self):
        if not self.fila:
            print("A fila está vazia!")
            return
        
        print("\nFila de Espera:")
        tempo_total_fila = sum(t for _, t in self.fila)
        for i, (item, tempo) in enumerate(self.fila, 1):
            print(f"{i}º - {item} (Tempo: {tempo}s)")
        
        print(f"\nTempo total estimado para fila: {tempo_total_fila}s")
        print(f"Tempo médio por item: {tempo_total_fila/len(self.fila):.1f}s")
        print(f"Tempo total acumulado: {self.tempo_total_espera}s")
    
    def menu_principal(self):
        while True:
            print("\n" + "="*50)
            print("SISTEMA DE FILA COM TEMPO DE ESPERA".center(50))
            print("="*50)
            print("1. Adicionar item")
            print("2. Atender próximo item")
            print("3. Visualizar fila")
            print("4. Adicionar 5 itens aleatórios (teste)")
            print("0. Sair")
            print("="*50)
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == '0':
                print("\nRelatório Final:")
                print(f"Itens atendidos: {self.tempo_total_espera}s de processamento total")
                print(f"Itens não atendidos: {len(self.fila)}")
                print("Sistema encerrado.")
                break
            
            elif opcao == '1':
                self.adicionar_item()
            
            elif opcao == '2':
                self.atender_item()
            
            elif opcao == '3':
                self.visualizar_fila()
            
            elif opcao == '4':
                for item in ["Relatório", "Planilha", "E-mail", "Impressão", "Consulta"]:
                    self.adicionar_item(item)
            
            else:
                print("Opção inválida! Tente novamente.")

# Teste do sistema
if __name__ == "__main__":
    print("=== SIMULADOR DE FILA COM TEMPO DE ESPERA ===")
    print("Nota: Cada item tem um tempo aleatório de processamento entre 1-5 segundos")
    
    fila = FilaEspera()
    fila.menu_principal()