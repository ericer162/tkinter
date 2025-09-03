import tkinter as tk
from tkinter import messagebox, ttk

class Usuario:
    def __init__(self):
        self.__senha = "agua2024"  # Atributo privado
    
    def verificar_senha(self, senha_digitada):
        """Método para verificar se a senha digitada está correta"""
        return senha_digitada == self.__senha


class CalculadoraFatura:
    @staticmethod
    def calcular_fatura(consumo):
        """
        Calcula o valor da fatura com base no consumo de água
        seguindo a tabela tarifária progressiva da Águas Guariroba
        """
        # Tabela tarifária: (limite da faixa, valor por m3)
        tabela_agua = [
            (5, 37.47),    # 1a faixa: tarifa mínima para 5m3
            (5, 1.16),     # 2a faixa: 5m3 × R$1,16
            (5, 6.46),     # 3a faixa: 5m3 × R$6,46
            (5, 6.49),     # 4a faixa: 5m3 × R$6,49
            (10, 6.55),    # 5a faixa: 10m3 × R$6,55
            (float('inf'), 11.08)  # 6a faixa: valor livre × R$11,08
        ]
        
        valor_agua = 0
        consumo_restante = consumo
        
        for i, (limite, tarifa) in enumerate(tabela_agua):
            if consumo_restante <= 0:
                break
                
            if i == 0:  # Primeira faixa tem tratamento especial (valor fixo)
                valor_agua += tarifa
                consumo_restante -= limite
            else:
                # Calcula quanto podemos cobrar nesta faixa
                consumo_na_faixa = min(limite, consumo_restante)
                valor_agua += consumo_na_faixa * tarifa
                consumo_restante -= consumo_na_faixa
        
        # Cálculo do esgoto (80% do valor da água)
        valor_esgoto = valor_agua * 0.8
        
        # Valor total da fatura
        valor_total = valor_agua + valor_esgoto
        
        return {
            'consumo': consumo,
            'valor_agua': valor_agua,
            'valor_esgoto': valor_esgoto,
            'valor_total': valor_total
        }


class AplicacaoFatura:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Fatura Digital - Águas Guariroba")
        self.root.geometry("500x400")
        self.usuario = Usuario()
        self.calculadora = CalculadoraFatura()
        
        self.criar_tela_login()
    
    def criar_tela_login(self):
        """Cria a interface de login"""
        self.limpar_tela()
        
        self.frame_login = tk.Frame(self.root, padx=20, pady=20)
        self.frame_login.pack(expand=True)
        
        tk.Label(self.frame_login, text="Bem-vindo ao Sistema de Fatura Digital", 
                font=('Arial', 12, 'bold')).pack(pady=10)
        
        tk.Label(self.frame_login, text="Digite sua senha para acessar:").pack(pady=5)
        
        self.entry_senha = tk.Entry(self.frame_login, show="*", width=25)
        self.entry_senha.pack(pady=5)
        self.entry_senha.bind('<Return>', lambda e: self.verificar_login())
        
        btn_login = tk.Button(self.frame_login, text="Acessar", 
                            command=self.verificar_login)
        btn_login.pack(pady=10)
    
    def verificar_login(self):
        """Verifica se a senha está correta"""
        senha = self.entry_senha.get()
        
        if self.usuario.verificar_senha(senha):
            self.criar_tela_principal()
        else:
            messagebox.showerror("Erro", "Senha incorreta! Tente novamente.")
            self.entry_senha.delete(0, tk.END)
    
    def criar_tela_principal(self):
        """Cria a tela principal do sistema"""
        self.limpar_tela()
        
        self.frame_principal = tk.Frame(self.root, padx=20, pady=20)
        self.frame_principal.pack(expand=True)
        
        tk.Label(self.frame_principal, text="Cálculo de Fatura de Água", 
                font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Entrada de consumo
        tk.Label(self.frame_principal, text="Consumo de água (m³):").pack()
        self.entry_consumo = tk.Entry(self.frame_principal, width=25)
        self.entry_consumo.pack(pady=5)
        self.entry_consumo.bind('<Return>', lambda e: self.calcular_fatura())
        
        # Botão de cálculo
        btn_calcular = tk.Button(self.frame_principal, text="Calcular Fatura", 
                                command=self.calcular_fatura)
        btn_calcular.pack(pady=10)
        
        btn_logout = tk.Button(self.frame_principal, text="Sair", 
                              command=self.criar_tela_login)
        btn_logout.pack(pady=10)
    
    def calcular_fatura(self):
        """Calcula e exibe a fatura"""
        try:
            consumo = float(self.entry_consumo.get())
            if consumo < 0:
                messagebox.showerror("Erro", "O consumo não pode ser negativo!")
                return
                
            fatura = self.calculadora.calcular_fatura(consumo)
            self.mostrar_fatura(fatura)
            
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor numérico válido!")
    
    def mostrar_fatura(self, dados_fatura):
        """Exibe a fatura em uma nova janela"""
        janela_fatura = tk.Toplevel(self.root)
        janela_fatura.title("Fatura Digital")
        janela_fatura.geometry("400x300")
        
        frame_fatura = tk.Frame(janela_fatura, padx=20, pady=20)
        frame_fatura.pack(expand=True)
        
        tk.Label(frame_fatura, text="FATURA DIGITAL", 
                font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Cria um Treeview para mostrar os dados
        tree = ttk.Treeview(frame_fatura, columns=('item', 'valor'), show='headings', height=4)
        tree.heading('item', text='Item')
        tree.heading('valor', text='Valor (R$)')
        tree.column('item', width=150)
        tree.column('valor', width=100)
        
        tree.pack(pady=10)
        
        # Adiciona os dados
        tree.insert('', 'end', values=("Consumo de água", f"{dados_fatura['consumo']} m³"))
        tree.insert('', 'end', values=("Valor água", f"{dados_fatura['valor_agua']:.2f}"))
        tree.insert('', 'end', values=("Valor esgoto (80%)", f"{dados_fatura['valor_esgoto']:.2f}"))
        tree.insert('', 'end', values=("VALOR TOTAL", f"{dados_fatura['valor_total']:.2f}"))
        
        # Botão para fechar
        btn_fechar = tk.Button(frame_fatura, text="Fechar", 
                             command=janela_fatura.destroy)
        btn_fechar.pack(pady=10)
    
    def limpar_tela(self):
        """Remove todos os widgets da tela principal"""
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacaoFatura(root)
    root.mainloop()