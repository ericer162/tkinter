###atividade01_02/04/2025###
import tkinter as tk
from tkinter import messagebox

def verificar_restricao():
    try:
        ultimo_digito = int(entrada_digito.get())
        
        if ultimo_digito < 0 or ultimo_digito > 9:
            messagebox.showerror("Erro", "Digite apenas um número de 0 a 9")
            return
            
        if ultimo_digito in [1, 2]:
            mensagem = "Não Circular 2ª Feira"
        elif ultimo_digito in [3, 4]:
            mensagem = "Não Circular 3ª Feira"
        elif ultimo_digito in [5, 6]:
            mensagem = "Não Circular 4ª Feira"
        elif ultimo_digito in [7, 8]:
            mensagem = "Não Circular 5ª Feira"
        elif ultimo_digito in [9, 0]:
            mensagem = "Não Circular 6ª Feira"
            
        label_resultado.config(text=mensagem)
        
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas um número válido (0-9)")

janela = tk.Tk()
janela.title("Restrição por Final de Placa")
janela.geometry("300x200")

label_instrucao = tk.Label(janela, text="Digite o último dígito da placa:")
label_instrucao.pack(pady=10)

entrada_digito = tk.Entry(janela, width=5, font=('Arial', 14), justify='center')
entrada_digito.pack(pady=5)

botao_verificar = tk.Button(janela, text="Verificar Restrição", command=verificar_restricao)
botao_verificar.pack(pady=10)

label_resultado = tk.Label(janela, text="", font=('Arial', 12, 'bold'))
label_resultado.pack(pady=20)

janela.mainloop()



###atividade02###
def menu_interativo():
    cardapio = {
        "1": {"prato": "Pizza Margherita", "preco": 45.00},
        "2": {"prato": "Lasanha Bolonhesa", "preco": 38.50},
        "3": {"prato": "Salada Caesar", "preco": 25.00},
        "4": {"prato": "Frango Grelhado", "preco": 32.00},
        "5": {"prato": "Sushi Variado", "preco": 55.00}
    }
    
    pedido = None
    total = 0.0
    
    while True:
        print("\n" + "="*30)
        print("🍽️  RESTAURANTE DELÍCIA 🍽️")
        print("="*30)
        print("\nCARDÁPIO:")
        for cod, item in cardapio.items():
            print(f"{cod}. {item['prato']} - R${item['preco']:.2f}")
        
        print("\nOPÇÕES:")
        print("1. Escolher prato")
        print("2. Calcular total (com gorjeta)")
        print("3. Calcular total (sem gorjeta)")
        print("4. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            print("\n" + "-"*20)
            print("FAZER PEDIDO")
            print("-"*20)
            codigo = input("Digite o número do prato desejado: ")
            if codigo in cardapio:
                pedido = cardapio[codigo]
                print(f"\n✅ Você escolheu: {pedido['prato']} - R${pedido['preco']:.2f}")
            else:
                print("\n❌ Código inválido. Por favor, tente novamente.")
                
        elif opcao == "2":
            if pedido:
                total = pedido['preco'] * 1.10  # Adiciona 10% de gorjeta
                print("\n" + "-"*30)
                print(f"Total a pagar (com 10% gorjeta): R${total:.2f}")
                print(f"Detalhe: R${pedido['preco']:.2f} + R${pedido['preco']*0.10:.2f} de gorjeta")
                print("-"*30)
            else:
                print("\n❌ Você ainda não escolheu um prato.")
                
        elif opcao == "3":
            if pedido:
                total = pedido['preco']
                print("\n" + "-"*30)
                print(f"Total a pagar (sem gorjeta): R${total:.2f}")
                print("-"*30)
            else:
                print("\n❌ Você ainda não escolheu um prato.")
                
        elif opcao == "4":
            print("\nObrigado pela visita! Volte sempre! 👋")
            break
            
        else:
            print("\n❌ Opção inválida. Por favor, tente novamente.")

menu_interativo()