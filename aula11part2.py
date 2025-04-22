###atividade-01_07/04/2025###
###1) Crie uma lista com 5 nomes e exiba todos os nomes um por um###

# import tkinter as tk
# from tkinter import messagebox

# def mostrar_nomes():
#     nomes = ["Eric", "Cleitao", "Kratos", "Will Smith", "Vin Diesel"]
    
#     for nome in nomes:
#         messagebox.showinfo("Nome", nome)

# root = tk.Tk()
# root.title("Lista de Nomes")
# root.geometry("300x100")

# btn_mostrar = tk.Button(
#     root,
#     text="Mostrar Nomes",
#     command=mostrar_nomes
# )
# btn_mostrar.pack(pady=20)


# root.mainloop()


###atividade-02###
###2) Peça 5 numeros ao usuario, guarde-os em uma lista e calcule a media.###

# import tkinter as tk
# from tkinter import messagebox

# def calcular_media():
#     try:
#         nums = [
#             float(entrada1.get()),
#             float(entrada2.get()),
#             float(entrada3.get()),
#             float(entrada4.get()),
#             float(entrada5.get())
#         ]
        
#         media = sum(nums) / len(nums)
        
#         messagebox.showinfo("Resultado", 
#                           f"Números digitados: {nums}\n"
#                           f"Média: {media:.2f}")
#     except ValueError:
#         messagebox.showerror("Erro", "Por favor, digite apenas números válidos!")


# janela = tk.Tk()
# janela.title("Calculadora de Média")
# janela.geometry("300x250")

# tk.Label(janela, text="Digite 5 números:").pack(pady=10)

# entrada1 = tk.Entry(janela)
# entrada1.pack(pady=5)

# entrada2 = tk.Entry(janela)
# entrada2.pack(pady=5)

# entrada3 = tk.Entry(janela)
# entrada3.pack(pady=5)

# entrada4 = tk.Entry(janela)
# entrada4.pack(pady=5)

# entrada5 = tk.Entry(janela)
# entrada5.pack(pady=5)

# tk.Button(janela, text="Calcular Média", command=calcular_media).pack(pady=10)

# janela.mainloop()


###atividade-03###
###3) Peça 5 palavras ao usuário e exiba a maior (em número de letras).###

# import tkinter as tk
# from tkinter import messagebox

# def encontrar_maior_palavra():
#     palavras = [
#         entrada1.get().strip(),
#         entrada2.get().strip(),
#         entrada3.get().strip(),
#         entrada4.get().strip(),
#         entrada5.get().strip()
#     ]
    
#     for palavra in palavras:
#         if not palavra:
#             messagebox.showwarning("Aviso", "Por favor, preencha todas as palavras!")
#             return
    
#     maior_palavra = max(palavras, key=len)
    
#     messagebox.showinfo("Resultado", 
#                        f"A maior palavra é: '{maior_palavra}'\n"
#                        f"Quantidade de letras: {len(maior_palavra)}")

# janela = tk.Tk()
# janela.title("Encontrar a Maior Palavra")
# janela.geometry("300x250")

# tk.Label(janela, text="Digite 5 palavras:").pack(pady=5)

# tk.Label(janela, text="Palavra 1:").pack()
# entrada1 = tk.Entry(janela)
# entrada1.pack()

# tk.Label(janela, text="Palavra 2:").pack()
# entrada2 = tk.Entry(janela)
# entrada2.pack()

# tk.Label(janela, text="Palavra 3:").pack()
# entrada3 = tk.Entry(janela)
# entrada3.pack()

# tk.Label(janela, text="Palavra 4:").pack()
# entrada4 = tk.Entry(janela)
# entrada4.pack()

# tk.Label(janela, text="Palavra 5:").pack()
# entrada5 = tk.Entry(janela)
# entrada5.pack()

# botao = tk.Button(janela, text="Encontrar Maior Palavra", command=encontrar_maior_palavra)
# botao.pack(pady=10)

# janela.mainloop()


###atividade-04###
###4) Crie um programa que leia 10 números e mostre somente os pares.###

# import tkinter as tk
# from tkinter import ttk, messagebox

# class FiltroNumerosPares:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Filtro de Números Pares")
#         self.root.geometry("500x400")
        
#         self.numeros = []
#         self.contador = 0
        
#         self.style = ttk.Style()
#         self.style.configure('TFrame', background='#f0f0f0')
#         self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
#         self.style.configure('TButton', font=('Arial', 10))
        
#         self.main_frame = ttk.Frame(root)
#         self.main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
#         self.entry_frame = ttk.Frame(self.main_frame)
#         self.entry_frame.pack(fill=tk.X, pady=5)
        
#         self.label_instrucao = ttk.Label(
#             self.entry_frame, 
#             text="Digite 10 números (um por vez):"
#         )
#         self.label_instrucao.pack(anchor=tk.W)
        
#         self.entry_numero = ttk.Entry(self.entry_frame, font=('Arial', 12))
#         self.entry_numero.pack(fill=tk.X, pady=5)
#         self.entry_numero.bind('<Return>', lambda e: self.adicionar_numero())
        
#         self.btn_adicionar = ttk.Button(
#             self.entry_frame, 
#             text="Adicionar Número", 
#             command=self.adicionar_numero
#         )
#         self.btn_adicionar.pack(pady=5)
        
#         self.label_contador = ttk.Label(
#             self.entry_frame, 
#             text="0/10 números inseridos",
#             foreground='blue'
#         )
#         self.label_contador.pack()
        
#         self.result_frame = ttk.Frame(self.main_frame)
#         self.result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
#         self.label_resultado = ttk.Label(
#             self.result_frame, 
#             text="Números Pares:",
#             font=('Arial', 10, 'bold')
#         )
#         self.label_resultado.pack(anchor=tk.W)
        
#         self.text_resultado = tk.Text(
#             self.result_frame, 
#             height=8, 
#             wrap=tk.WORD,
#             font=('Arial', 10),
#             state=tk.DISABLED
#         )
#         self.scrollbar = ttk.Scrollbar(
#             self.result_frame, 
#             orient=tk.VERTICAL, 
#             command=self.text_resultado.yview
#         )
#         self.text_resultado.configure(yscrollcommand=self.scrollbar.set)
        
#         self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
#         self.text_resultado.pack(fill=tk.BOTH, expand=True)
        
#         self.btn_limpar = ttk.Button(
#             self.main_frame, 
#             text="Limpar Tudo", 
#             command=self.limpar_tudo
#         )
#         self.btn_limpar.pack(pady=5)
    
#     def adicionar_numero(self):
#         valor = self.entry_numero.get()
        
#         if not valor:
#             messagebox.showwarning("Aviso", "Por favor, digite um número.")
#             return
        
#         try:
#             numero = float(valor)
#             self.numeros.append(numero)
#             self.contador += 1
#             self.label_contador.config(text=f"{self.contador}/10 números inseridos")
#             self.entry_numero.delete(0, tk.END)
            
#             if self.contador == 10:
#                 self.mostrar_pares()
#                 self.btn_adicionar.config(state=tk.DISABLED)
#                 self.entry_numero.config(state=tk.DISABLED)
                
#         except ValueError:
#             messagebox.showerror("Erro", "Por favor, digite um número válido.")
#             self.entry_numero.delete(0, tk.END)
    
#     def mostrar_pares(self):
#         pares = [str(num) for num in self.numeros if num % 2 == 0]
        
#         self.text_resultado.config(state=tk.NORMAL)
#         self.text_resultado.delete(1.0, tk.END)
        
#         if not pares:
#             self.text_resultado.insert(tk.END, "Nenhum número par foi encontrado.")
#         else:
#             self.text_resultado.insert(tk.END, "\n".join(pares))
        
#         self.text_resultado.config(state=tk.DISABLED)
    
#     def limpar_tudo(self):
#         self.numeros = []
#         self.contador = 0
#         self.label_contador.config(text="0/10 números inseridos")
#         self.entry_numero.config(state=tk.NORMAL)
#         self.entry_numero.delete(0, tk.END)
#         self.btn_adicionar.config(state=tk.NORMAL)
        
#         self.text_resultado.config(state=tk.NORMAL)
#         self.text_resultado.delete(1.0, tk.END)
#         self.text_resultado.config(state=tk.DISABLED)
#         self.entry_numero.focus_set()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = FiltroNumerosPares(root)
#     root.mainloop()


###atividade-05###
###Peça ao usuário 5 produtos e adicione em uma lista. Depois, remova um produto informado pelo usuário.###

#import tkinter as tk
#from tkinter import messagebox

# class ProdutosApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Gerenciador de Produtos")
        
#         self.produtos = []
        
#         self.setup_ui()
    
#     def setup_ui(self):
#         self.frame = tk.Frame(self.root, padx=20, pady=20)
#         self.frame.pack()
        
#         self.label = tk.Label(self.frame, text="Digite 5 produtos para adicionar à lista:")
#         self.label.grid(row=0, column=0, columnspan=2, pady=5)
        
#         self.entry_produto = tk.Entry(self.frame, width=30)
#         self.entry_produto.grid(row=1, column=0, pady=5)
#         self.entry_produto.focus()
        
#         self.btn_adicionar = tk.Button(self.frame, text="Adicionar", command=self.adicionar_produto)
#         self.btn_adicionar.grid(row=1, column=1, pady=5, padx=5)
        
#         self.listbox = tk.Listbox(self.frame, width=40, height=10)
#         self.listbox.grid(row=2, column=0, columnspan=2, pady=10)
        
#         self.label_remover = tk.Label(self.frame, text="Digite o produto a remover:")
#         self.label_remover.grid(row=3, column=0, columnspan=2, pady=5)
        
#         self.entry_remover = tk.Entry(self.frame, width=30)
#         self.entry_remover.grid(row=4, column=0, pady=5)
        
#         self.btn_remover = tk.Button(self.frame, text="Remover", command=self.remover_produto)
#         self.btn_remover.grid(row=4, column=1, pady=5, padx=5)
        
#         self.label_contador = tk.Label(self.frame, text="0/5 produtos adicionados")
#         self.label_contador.grid(row=5, column=0, columnspan=2, pady=5)
    
#     def adicionar_produto(self):
#         produto = self.entry_produto.get().strip()
        
#         if produto:
#             if len(self.produtos) < 5:
#                 self.produtos.append(produto)
#                 self.listbox.insert(tk.END, produto)
#                 self.entry_produto.delete(0, tk.END)
#                 self.label_contador.config(text=f"{len(self.produtos)}/5 produtos adicionados")
                
#                 if len(self.produtos) == 5:
#                     self.btn_adicionar.config(state=tk.DISABLED)
#                     messagebox.showinfo("Sucesso", "Você adicionou 5 produtos. Agora pode remover algum.")
#             else:
#                 messagebox.showwarning("Aviso", "Você já adicionou 5 produtos!")
#         else:
#             messagebox.showwarning("Aviso", "Por favor, digite um produto!")
    
#     def remover_produto(self):
#         produto_remover = self.entry_remover.get().strip()
        
#         if produto_remover:
#             if produto_remover in self.produtos:
#                 self.produtos.remove(produto_remover)
                
#                 self.listbox.delete(0, tk.END)
#                 for produto in self.produtos:
#                     self.listbox.insert(tk.END, produto)
                
#                 self.entry_remover.delete(0, tk.END)
#                 self.label_contador.config(text=f"{len(self.produtos)}/5 produtos adicionados")
                
#                 if len(self.produtos) < 5:
#                     self.btn_adicionar.config(state=tk.NORMAL)
#             else:
#                 messagebox.showwarning("Aviso", "Este produto não está na lista!")
#         else:
#             messagebox.showwarning("Aviso", "Por favor, digite um produto para remover!")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ProdutosApp(root)
#     root.mainloop()


###atividade-08###
###8) Peça ao usuário para digitar 5 números e, ao final, mostre a lista ordenada.###

import tkinter as tk
from tkinter import messagebox

def ordenar_numeros():
    try:
        # Obter os números dos campos de entrada
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        num3 = float(entrada3.get())
        num4 = float(entrada4.get())
        num5 = float(entrada5.get())
        
        # Criar lista e ordenar
        numeros = [num1, num2, num3, num4, num5]
        numeros_ordenados = sorted(numeros)
        
        # Mostrar resultado
        messagebox.showinfo("Resultado", f"Lista ordenada: {numeros_ordenados}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite apenas números válidos")

# Criar a janela principal
janela = tk.Tk()
janela.title("Ordenador de Números")
janela.geometry("300x250")
janela.configure(background='#49d6ca')
# Rótulo de instrução
tk.Label(janela, text="Digite 5 números:").pack(pady=10)

# Campos de entrada
entrada1 = tk.Entry(janela)
entrada1.pack(pady=2)
entrada2 = tk.Entry(janela)
entrada2.pack(pady=2)
entrada3 = tk.Entry(janela)
entrada3.pack(pady=2)
entrada4 = tk.Entry(janela)
entrada4.pack(pady=2)
entrada5 = tk.Entry(janela)
entrada5.pack(pady=2)

# Botão para ordenar
botao_ordenar = tk.Button(janela, text="Ordenar", command=ordenar_numeros)
botao_ordenar.pack(pady=10)

# Executar a aplicação
janela.mainloop()
