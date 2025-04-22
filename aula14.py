# ##atividade-01_09/04/2025###
# ## 1)Crie uma pilha vazia e permita ao usuário empilhar 5 números digitados. 
# Em seguida, exiba o conteúdo da pilha.###

# import tkinter as tk
# from tkinter import messagebox

# class PilhaApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Pilha de Números")
        
#         self.pilha = []
        
#         self.label = tk.Label(root, text="Digite um número para empilhar:")
#         self.label.pack(pady=5)
        
#         self.entry = tk.Entry(root)
#         self.entry.pack(pady=5)
        
#         self.empilhar_btn = tk.Button(root, text="Empilhar", command=self.empilhar)
#         self.empilhar_btn.pack(pady=5)
        
#         self.mostrar_btn = tk.Button(root, text="Mostrar Pilha", command=self.mostrar_pilha)
#         self.mostrar_btn.pack(pady=5)
        
#         self.limpar_btn = tk.Button(root, text="Limpar Pilha", command=self.limpar_pilha)
#         self.limpar_btn.pack(pady=5)
        
#         self.contador = 0
#         self.contador_label = tk.Label(root, text="Números empilhados: 0/5")
#         self.contador_label.pack(pady=5)
        
#         self.lista_pilha = tk.Listbox(root, width=40, height=10)
#         self.lista_pilha.pack(pady=10)
    
#     def empilhar(self):
#         if self.contador >= 5:
#             messagebox.showinfo("Aviso", "Você já empilhou 5 números!")
#             return
            
#         try:
#             numero = int(self.entry.get())
#             self.pilha.append(numero)
#             self.contador += 1
#             self.contador_label.config(text=f"Números empilhados: {self.contador}/5")
#             self.entry.delete(0, tk.END)            
#             self.atualizar_visualizacao()
            
#             if self.contador == 5:
#                 messagebox.showinfo("Sucesso", "Você empilhou 5 números com sucesso!")
                
#         except ValueError:
#             messagebox.showerror("Erro", "Por favor, digite um número válido!")
    
#     def mostrar_pilha(self):
#         if not self.pilha:
#             messagebox.showinfo("Pilha", "A pilha está vazia!")
#             return        
#         pilha_str = "Conteúdo da pilha (do topo para a base):\n"
#         for elemento in reversed(self.pilha):
#             pilha_str += f"{elemento}\n"
            
#         messagebox.showinfo("Conteúdo da Pilha", pilha_str)
    
#     def limpar_pilha(self):
#         self.pilha = []
#         self.contador = 0
#         self.contador_label.config(text="Números empilhados: 0/5")
#         self.lista_pilha.delete(0, tk.END)
#         messagebox.showinfo("Pilha", "Pilha limpa com sucesso!")
    
#     def atualizar_visualizacao(self):
#         self.lista_pilha.delete(0, tk.END)
#         for elemento in reversed(self.pilha):
#             self.lista_pilha.insert(0, str(elemento))

# root = tk.Tk()
# app = PilhaApp(root)
# root.mainloop()



# ##atividade-02###
# ##2) Permita que o usuário empilhe quantos itens quiser, até digitar "sair".
# Mostre a pilha ao final.###

# import tkinter as tk
# from tkinter import messagebox

# class PilhaDinamicaApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Pilha Dinâmica")
#         self.root.geometry("400x450")
        
#         self.pilha = []
        
#         self.main_frame = tk.Frame(root)
#         self.main_frame.pack(pady=20)
        
#         self.label_instrucao = tk.Label(self.main_frame, 
#                                       text="Digite números para empilhar\n(ou 'sair' para finalizar):")
#         self.label_instrucao.grid(row=0, column=0, columnspan=2, pady=5)
        
#         self.entrada_numero = tk.Entry(self.main_frame, width=15)
#         self.entrada_numero.grid(row=1, column=0, padx=5)
        
#         self.botao_empilhar = tk.Button(self.main_frame, text="Empilhar", 
#                                       command=self.processar_entrada)
#         self.botao_empilhar.grid(row=1, column=1, padx=5)
        
#         self.label_pilha = tk.Label(self.main_frame, text="Pilha (Topo para Base):")
#         self.label_pilha.grid(row=2, column=0, columnspan=2, pady=(20,5))
        
#         self.listbox_pilha = tk.Listbox(self.main_frame, width=20, height=10, 
#                                       font=('Arial', 12), selectbackground="lightblue")
#         self.listbox_pilha.grid(row=3, column=0, columnspan=2)
        
#         self.label_contador = tk.Label(self.main_frame, 
#                                       text=f"Elementos na pilha: {len(self.pilha)}")
#         self.label_contador.grid(row=4, column=0, columnspan=2, pady=10)
        
#         self.botao_finalizar = tk.Button(self.main_frame, text="Finalizar e Mostrar", 
#                                        command=self.finalizar_e_mostrar)
#         self.botao_finalizar.grid(row=5, column=0, columnspan=2, pady=10)
        
#         self.entrada_numero.focus_set()
        
#         self.root.bind('<Return>', lambda event: self.processar_entrada())
    
#     def processar_entrada(self):
#         texto = self.entrada_numero.get().strip().lower()
        
#         if texto == "sair":
#             self.finalizar_e_mostrar()
#             return
            
#         if not texto:
#             messagebox.showwarning("Entrada Vazia", "Digite um número ou 'sair'!")
#             return
            
#         try:
#             numero = float(texto)
#             self.pilha.append(numero)
#             self.atualizar_visualizacao()
#             self.entrada_numero.delete(0, tk.END)
#             self.label_contador.config(text=f"Elementos na pilha: {len(self.pilha)}")
            
#         except ValueError:
#             messagebox.showerror("Erro", "Por favor, digite um número válido ou 'sair'!")
#             self.entrada_numero.delete(0, tk.END)
    
#     def atualizar_visualizacao(self):
#         """Atualiza o Listbox para mostrar a pilha corretamente (topo no topo)"""
#         self.listbox_pilha.delete(0, tk.END)
        
#         for elemento in reversed(self.pilha):
#             self.listbox_pilha.insert(tk.END, f" {elemento}")
            
#         if self.pilha:
#             self.listbox_pilha.itemconfig(0, {'bg':'lightgreen'})
    
#     def finalizar_e_mostrar(self):
#         if not self.pilha:
#             messagebox.showinfo("Pilha Vazia", "Nenhum elemento foi empilhado!")
#             return
            
#         conteudo = "Conteúdo Final da Pilha (Topo → Base):\n\n"
#         for i, elemento in enumerate(reversed(self.pilha)):
#             conteudo += f"{i+1}º: {elemento}\n"
            
#         messagebox.showinfo("Resultado Final", conteudo)
#         self.root.destroy()  

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = PilhaDinamicaApp(root)
#     root.mainloop()



# ##atividade-03###
# ##3)Implemente a operação de desempilhar e avise se a pilha estiver vazia.###

# import tkinter as tk
# from tkinter import messagebox

# class PilhaCompletaApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Pilha Completa - Empilhar/Desempilhar")
#         self.root.geometry("450x500")
        
#         self.pilha = []
        
#         self.main_frame = tk.Frame(root)
#         self.main_frame.pack(pady=20)
        
#         self.label_instrucao = tk.Label(self.main_frame, 
#                                       text="Digite números para empilhar:")
#         self.label_instrucao.grid(row=0, column=0, columnspan=3, pady=5)
        
#         self.entrada_numero = tk.Entry(self.main_frame, width=15)
#         self.entrada_numero.grid(row=1, column=0, padx=5)
        
#         self.botao_empilhar = tk.Button(self.main_frame, text="Empilhar", 
#                                       command=self.empilhar)
#         self.botao_empilhar.grid(row=1, column=1, padx=5)
        
#         self.botao_desempilhar = tk.Button(self.main_frame, text="Desempilhar", 
#                                          command=self.desempilhar)
#         self.botao_desempilhar.grid(row=1, column=2, padx=5)
        
#         self.label_pilha = tk.Label(self.main_frame, text="Pilha (Topo para Base):")
#         self.label_pilha.grid(row=2, column=0, columnspan=3, pady=(20,5))
        
#         self.listbox_pilha = tk.Listbox(self.main_frame, width=25, height=12, 
#                                       font=('Arial', 12), selectbackground="lightblue")
#         self.listbox_pilha.grid(row=3, column=0, columnspan=3)
        
#         self.label_contador = tk.Label(self.main_frame, 
#                                       text=f"Elementos na pilha: {len(self.pilha)}")
#         self.label_contador.grid(row=4, column=0, columnspan=3, pady=10)
        
#         self.botao_finalizar = tk.Button(self.main_frame, text="Mostrar Conteúdo", 
#                                        command=self.mostrar_conteudo)
#         self.botao_finalizar.grid(row=5, column=0, columnspan=3, pady=10)
        
#         self.entrada_numero.focus_set()
        
#         self.root.bind('<Return>', lambda event: self.empilhar())
    
#     def empilhar(self):
#         texto = self.entrada_numero.get().strip()
        
#         if not texto:
#             messagebox.showwarning("Entrada Vazia", "Digite um número para empilhar!")
#             return
            
#         try:
#             numero = float(texto)  
#             self.pilha.append(numero)
#             self.atualizar_visualizacao()
#             self.entrada_numero.delete(0, tk.END)
#             self.label_contador.config(text=f"Elementos na pilha: {len(self.pilha)}")
            
#         except ValueError:
#             messagebox.showerror("Erro", "Por favor, digite um número válido!")
#             self.entrada_numero.delete(0, tk.END)
    
#     def desempilhar(self):
#         if not self.pilha:
#             messagebox.showwarning("Pilha Vazia", "Não é possível desempilhar - a pilha está vazia!")
#             return
            
#         elemento_removido = self.pilha.pop()
#         messagebox.showinfo("Elemento Desempilhado", 
#                            f"Elemento removido do topo: {elemento_removido}")
#         self.atualizar_visualizacao()
#         self.label_contador.config(text=f"Elementos na pilha: {len(self.pilha)}")
    
#     def atualizar_visualizacao(self):
#         """Atualiza o Listbox para mostrar a pilha corretamente (topo no topo)"""
#         self.listbox_pilha.delete(0, tk.END)
        
#         for elemento in reversed(self.pilha):
#             self.listbox_pilha.insert(tk.END, f" {elemento}")
            
#         if self.pilha:
#             self.listbox_pilha.itemconfig(0, {'bg':'lightgreen'})
    
#     def mostrar_conteudo(self):
#         if not self.pilha:
#             messagebox.showinfo("Pilha Vazia", "A pilha não contém elementos!")
#             return
            
#         conteudo = "Conteúdo da Pilha (Topo → Base):\n\n"
#         for i, elemento in enumerate(reversed(self.pilha)):
#             conteudo += f"{i+1}º: {elemento}\n"
            
#         messagebox.showinfo("Conteúdo da Pilha", conteudo)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = PilhaCompletaApp(root)
#     root.mainloop()


# ##atividade-04###
# ##4)Faça um programa com menu: empilhar, desempilhar, ver topo da pilha, ver toda a pilha, sair.

# import tkinter as tk
# from tkinter import messagebox

# class PilhaApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Gerenciador de Pilha")
#         self.root.geometry("400x400")
        
#         self.pilha = []
        
#         self.frame = tk.Frame(root)
#         self.frame.pack(pady=20)
        
#         self.titulo = tk.Label(self.frame, text="Operações de Pilha", font=('Arial', 14))
#         self.titulo.grid(row=0, column=0, columnspan=2, pady=10)
        
#         self.btn_empilhar = tk.Button(self.frame, text="Empilhar", command=self.empilhar, width=15)
#         self.btn_empilhar.grid(row=1, column=0, padx=5, pady=5)
        
#         self.btn_desempilhar = tk.Button(self.frame, text="Desempilhar", command=self.desempilhar, width=15)
#         self.btn_desempilhar.grid(row=1, column=1, padx=5, pady=5)
        
#         self.btn_ver_topo = tk.Button(self.frame, text="Ver Topo", command=self.ver_topo, width=15)
#         self.btn_ver_topo.grid(row=2, column=0, padx=5, pady=5)
        
#         self.btn_ver_pilha = tk.Button(self.frame, text="Ver Pilha", command=self.ver_pilha, width=15)
#         self.btn_ver_pilha.grid(row=2, column=1, padx=5, pady=5)
        
#         self.btn_sair = tk.Button(self.frame, text="Sair", command=root.quit, width=15)
#         self.btn_sair.grid(row=3, column=0, columnspan=2, pady=10)
        
#         self.label_entrada = tk.Label(self.frame, text="Valor para empilhar:")
#         self.label_entrada.grid(row=4, column=0, pady=5)
        
#         self.entrada_valor = tk.Entry(self.frame, width=20)
#         self.entrada_valor.grid(row=4, column=1, pady=5)
        
#         self.label_pilha = tk.Label(root, text="Conteúdo da Pilha:", font=('Arial', 12))
#         self.label_pilha.pack()
        
#         self.texto_pilha = tk.Text(root, height=10, width=40, state='disabled')
#         self.texto_pilha.pack(pady=10)
    
#     def atualizar_display(self):
#         """Atualiza a exibição da pilha"""
#         self.texto_pilha.config(state='normal')
#         self.texto_pilha.delete(1.0, tk.END)
        
#         if not self.pilha:
#             self.texto_pilha.insert(tk.END, "Pilha vazia")
#         else:
#             for item in reversed(self.pilha):
#                 self.texto_pilha.insert(tk.END, f"{item}\n")
        
#         self.texto_pilha.config(state='disabled')
    
#     def empilhar(self):
#         """Adiciona um elemento no topo da pilha"""
#         valor = self.entrada_valor.get()
        
#         if valor:
#             self.pilha.append(valor)
#             self.entrada_valor.delete(0, tk.END)
#             self.atualizar_display()
#             messagebox.showinfo("Sucesso", f"Valor '{valor}' empilhado com sucesso!")
#         else:
#             messagebox.showwarning("Aviso", "Por favor, digite um valor para empilhar")
    
#     def desempilhar(self):
#         """Remove o elemento do topo da pilha"""
#         if not self.pilha:
#             messagebox.showwarning("Aviso", "A pilha está vazia!")
#         else:
#             valor = self.pilha.pop()
#             self.atualizar_display()
#             messagebox.showinfo("Sucesso", f"Valor '{valor}' desempilhado com sucesso!")
    
#     def ver_topo(self):
#         """Mostra o elemento no topo da pilha"""
#         if not self.pilha:
#             messagebox.showinfo("Topo da Pilha", "A pilha está vazia!")
#         else:
#             messagebox.showinfo("Topo da Pilha", f"Topo da pilha: {self.pilha[-1]}")
    
#     def ver_pilha(self):
#         """Mostra todos os elementos da pilha"""
#         self.atualizar_display()
#         if not self.pilha:
#             messagebox.showinfo("Pilha", "A pilha está vazia!")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = PilhaApp(root)
#     root.mainloop()



# ##atividade-05###
# ##5) Crie uma função chamada tamanho_pilha() que retorne quantos elementos estão na pilha.

# import tkinter as tk
# from tkinter import messagebox

# class PilhaApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Contador de Pilha")
        
#         self.pilha = []
        
#         self.frame = tk.Frame(root, padx=20, pady=20)
#         self.frame.pack()
        
#         self.label_tamanho = tk.Label(self.frame, text="Tamanho da Pilha: 0", font=("Arial", 12))
#         self.label_tamanho.pack(pady=10)
        
#         self.btn_push = tk.Button(self.frame, text="Push (Adicionar)", command=self.push)
#         self.btn_push.pack(pady=5)
        
#         self.btn_pop = tk.Button(self.frame, text="Pop (Remover)", command=self.pop)
#         self.btn_pop.pack(pady=5)
        
#         self.btn_tamanho = tk.Button(self.frame, text="Ver Tamanho", command=self.tamanho_pilha)
#         self.btn_tamanho.pack(pady=5)
    
#     def push(self):
#         """Adiciona um elemento à pilha e atualiza o label."""
#         elemento = f"Item {len(self.pilha) + 1}"  # Simula um novo item
#         self.pilha.append(elemento)
#         self.atualizar_label()
#         messagebox.showinfo("Push", f"Adicionado: {elemento}")
    
#     def pop(self):
#         """Remove um elemento da pilha e atualiza o label."""
#         if not self.pilha:
#             messagebox.showwarning("Erro", "Pilha vazia!")
#         else:
#             removido = self.pilha.pop()
#             self.atualizar_label()
#             messagebox.showinfo("Pop", f"Removido: {removido}")
    
#     def tamanho_pilha(self):
#         """Retorna o tamanho da pilha e exibe no label."""
#         tamanho = len(self.pilha)
#         messagebox.showinfo("Tamanho", f"A pilha tem {tamanho} elementos.")
#         return tamanho
    
#     def atualizar_label(self):
#         """Atualiza o label com o tamanho atual da pilha."""
#         self.label_tamanho.config(text=f"Tamanho da Pilha: {len(self.pilha)}")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = PilhaApp(root)
#     root.mainloop()


# ##atividade-06###
# ##6)Crie uma pilha que armazene nomes. Depois,
# permita buscar se um nome está ou não na pilha.

# import tkinter as tk
# from tkinter import messagebox

# class PilhaNomesApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Pilha de Nomes")
        
#         self.pilha = PilhaNomes()  # Usando a classe PilhaNomes
        
#         # Widgets
#         self.label = tk.Label(root, text="Digite um nome:")
#         self.label.pack(pady=5)
        
#         self.entry = tk.Entry(root, width=30)
#         self.entry.pack(pady=5)
        
#         self.btn_empilhar = tk.Button(root, text="Empilhar", command=self.empilhar)
#         self.btn_empilhar.pack(pady=5)
        
#         self.btn_buscar = tk.Button(root, text="Buscar Nome", command=self.buscar)
#         self.btn_buscar.pack(pady=5)
        
#         self.btn_mostrar = tk.Button(root, text="Mostrar Pilha", command=self.mostrar)
#         self.btn_mostrar.pack(pady=5)
    
#     def empilhar(self):
#         nome = self.entry.get()
#         if nome:
#             self.pilha.empilhar(nome)
#             messagebox.showinfo("Sucesso", f"'{nome}' empilhado!")
#             self.entry.delete(0, tk.END)
    
#     def buscar(self):
#         nome = self.entry.get()
#         if nome:
#             if self.pilha.buscar_nome(nome):
#                 messagebox.showinfo("Resultado", f"'{nome}' está na pilha!")
#             else:
#                 messagebox.showinfo("Resultado", f"'{nome}' NÃO está na pilha.")
    
#     def mostrar(self):
#         messagebox.showinfo("Pilha Atual", str(self.pilha))

# # Execução
# root = tk.Tk()
# app = PilhaNomesApp(root)
# root.mainloop()


# ##atividade-07###
# 7)Simule o botão "voltar" de um navegador. Cada página visitada é empilhada. Quando o usuário escolher "voltar", remova a última.

# import tkinter as tk
# from tkinter import messagebox

# class NavegadorSimulador:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Simulador de Navegação")
        
#         # Pilha para armazenar as páginas visitadas
#         self.pilha_paginas = []
#         self.pagina_atual = "Página Inicial"
        
#         # Configuração da interface
#         self.frame = tk.Frame(root, padx=20, pady=20)
#         self.frame.pack()
        
#         # Label para mostrar a página atual
#         self.label_pagina = tk.Label(
#             self.frame, 
#             text=f"Página atual: {self.pagina_atual}", 
#             font=("Arial", 12)
#         )
#         self.label_pagina.pack(pady=10)
        
#         # Entrada para digitar a próxima página
#         self.entry_pagina = tk.Entry(self.frame, width=30)
#         self.entry_pagina.pack(pady=5)
        
#         # Botão para visitar uma nova página
#         self.btn_visitar = tk.Button(
#             self.frame, 
#             text="Visitar Página", 
#             command=self.visitar_pagina
#         )
#         self.btn_visitar.pack(pady=5)
        
#         # Botão para voltar à página anterior
#         self.btn_voltar = tk.Button(
#             self.frame, 
#             text="Voltar", 
#             command=self.voltar_pagina
#         )
#         self.btn_voltar.pack(pady=5)
    
#     def visitar_pagina(self):
#         """Adiciona uma nova página à pilha."""
#         nova_pagina = self.entry_pagina.get()
#         if nova_pagina:
#             # Empilha a página atual antes de mudar
#             if self.pagina_atual:
#                 self.pilha_paginas.append(self.pagina_atual)
            
#             # Atualiza a página atual
#             self.pagina_atual = nova_pagina
#             self.label_pagina.config(text=f"Página atual: {self.pagina_atual}")
#             self.entry_pagina.delete(0, tk.END)
    
#     def voltar_pagina(self):
#         """Remove a última página da pilha (simula o 'Voltar')."""
#         if self.pilha_paginas:
#             # Desempilha a última página visitada
#             self.pagina_atual = self.pilha_paginas.pop()
#             self.label_pagina.config(text=f"Página atual: {self.pagina_atual}")
#         else:
#             messagebox.showinfo("Aviso", "Não há páginas para voltar!")

# # Execução
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = NavegadorSimulador(root)
#     root.mainloop()


# ##atividade-08###
# ##8)Utilize uma pilha para inverter uma palavra digitada pelo usuário (usando .pop()).

# import tkinter as tk
# from tkinter import messagebox

# def inverter_palavra():
#     palavra = entrada.get()
#     if not palavra:
#         messagebox.showwarning("Erro", "Digite uma palavra!")
#         return
    
#     # Empilha cada letra
#     pilha = list(palavra)
    
#     # Desempilha para inverter
#     palavra_invertida = []
#     while pilha:
#         palavra_invertida.append(pilha.pop())
    
#     resultado = "".join(palavra_invertida)
#     messagebox.showinfo("Resultado", f"Palavra invertida: {resultado}")

# # Configuração da interface
# root = tk.Tk()
# root.title("Inversor de Palavras")

# tk.Label(root, text="Digite uma palavra:").pack(pady=10)
# entrada = tk.Entry(root, width=30)
# entrada.pack(pady=5)

# tk.Button(root, text="Inverter", command=inverter_palavra).pack(pady=5)

# root.mainloop()


# ##atividade-09###
# 9)Faça um programa que armazene expressões matemáticas e use pilha para verificar se os parênteses estão corretos.

# import tkinter as tk
# from tkinter import messagebox

# def verificar_expressao():
#     expressao = entrada.get()
#     if not expressao:
#         messagebox.showwarning("Erro", "Digite uma expressão!")
#         return
    
#     pilha = []
#     pares = {')': '(', ']': '[', '}': '{'}
    
#     for char in expressao:
#         if char in pares.values():  # Se for de abertura
#             pilha.append(char)
#         elif char in pares:  # Se for de fechamento
#             if not pilha or pilha.pop() != pares[char]:
#                 messagebox.showerror("Resultado", "ERRO: Parênteses/colchetes/chaves NÃO balanceados!")
#                 return
    
#     if pilha:
#         messagebox.showerror("Resultado", "ERRO: Parênteses/colchetes/chaves NÃO balanceados!")
#     else:
#         messagebox.showinfo("Resultado", "OK: Parênteses/colchetes/chaves balanceados!")

# # Configuração da interface
# root = tk.Tk()
# root.title("Verificador de Expressões Matemáticas")

# tk.Label(root, text="Digite uma expressão:").pack(pady=10)
# entrada = tk.Entry(root, width=50)
# entrada.pack(pady=5)

# tk.Button(root, text="Verificar", command=verificar_expressao).pack(pady=5)

# root.mainloop()



# ##atividade-10###
# 10)Desafio: implemente uma calculadora de expressões em notação pós-fixada (RPN) usando pilha.
# import tkinter as tk
# from tkinter import messagebox

# def verificar_expressao():
#     expressao = entrada.get()
#     if not expressao:
#         messagebox.showwarning("Erro", "Digite uma expressão!")
#         return
    
#     pilha = []
#     pares = {')': '(', ']': '[', '}': '{'}
    
#     for char in expressao:
#         if char in pares.values():  
#             pilha.append(char)
#         elif char in pares:  
#             if not pilha or pilha.pop() != pares[char]:
#                 messagebox.showerror("Resultado", "ERRO: Parênteses/colchetes/chaves NÃO balanceados!")
#                 return
    
#     if pilha:
#         messagebox.showerror("Resultado", "ERRO: Parênteses/colchetes/chaves NÃO balanceados!")
#     else:
#         messagebox.showinfo("Resultado", "OK: Parênteses/colchetes/chaves balanceados!")

# root = tk.Tk()
# root.title("Verificador de Expressões Matemáticas")

# tk.Label(root, text="Digite uma expressão:").pack(pady=10)
# entrada = tk.Entry(root, width=50)
# entrada.pack(pady=5)

# tk.Button(root, text="Verificar", command=verificar_expressao).pack(pady=5)

# root.mainloop()