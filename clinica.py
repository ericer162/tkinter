import tkinter as tk
from tkinter import messagebox
import mysql.connector

class SistemaClinicaSimples:
    def __init__(self, root):
        self.root = root
        self.root.title("Clínica Médica - LGPD Simplificado")
        self.root.geometry("600x400")
        
        # Conexão com o MySQL (simplificada)
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='clinica_simples'
        )
        
        self.criar_tabelas()
        
        # Interface principal
        self.criar_interface()
    
    def criar_tabelas(self):
        cursor = self.conexao.cursor()
        
        # Tabela simplificada de pacientes
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100),
            cpf VARCHAR(14),
            telefone VARCHAR(20),
            consentimento BOOLEAN DEFAULT FALSE,
            ativo BOOLEAN DEFAULT TRUE
        )
        """)
        
        # Tabela simplificada de logs
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            acao VARCHAR(50),
            data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        self.conexao.commit()
    
    def criar_interface(self):
        # Frame principal
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Cadastro de pacientes
        tk.Label(frame, text="Nome:").grid(row=0, column=0, sticky='w')
        self.ent_nome = tk.Entry(frame, width=30)
        self.ent_nome.grid(row=0, column=1, pady=5)
        
        tk.Label(frame, text="CPF:").grid(row=1, column=0, sticky='w')
        self.ent_cpf = tk.Entry(frame, width=20)
        self.ent_cpf.grid(row=1, column=1, pady=5, sticky='w')
        
        self.var_consentimento = tk.BooleanVar()
        tk.Checkbutton(frame, text="Consentimento para contato", 
                      variable=self.var_consentimento).grid(row=2, column=1, sticky='w', pady=5)
        
        tk.Button(frame, text="Cadastrar Paciente", command=self.cadastrar_paciente,
                bg='green', fg='white').grid(row=3, column=1, pady=10, sticky='e')
        
        # Lista de pacientes
        self.lista_pacientes = tk.Listbox(frame, width=50, height=10)
        self.lista_pacientes.grid(row=4, column=0, columnspan=2, pady=10)
        
        tk.Button(frame, text="Carregar Pacientes", command=self.carregar_pacientes).grid(row=5, column=0, pady=5)
        tk.Button(frame, text="Remover Selecionado", command=self.remover_paciente,
                 bg='red', fg='white').grid(row=5, column=1, pady=5)
        
        # Logs simples
        tk.Label(frame, text="Últimas ações:").grid(row=6, column=0, sticky='w')
        self.text_logs = tk.Text(frame, width=50, height=5)
        self.text_logs.grid(row=7, column=0, columnspan=2)
    
    def cadastrar_paciente(self):
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        
        if not nome or not cpf:
            messagebox.showwarning("Aviso", "Preencha nome e CPF!")
            return
            
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "INSERT INTO pacientes (nome, cpf, consentimento) VALUES (%s, %s, %s)",
                (nome, cpf, self.var_consentimento.get())
            )
            self.conexao.commit()
            
            # Registrar log
            cursor.execute("INSERT INTO logs (acao) VALUES ('Cadastrou paciente')")
            self.conexao.commit()
            
            messagebox.showinfo("Sucesso", "Paciente cadastrado com LGPD!")
            self.carregar_pacientes()
            self.carregar_logs()
            
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Falha ao cadastrar: {err}")
    
    def carregar_pacientes(self):
        self.lista_pacientes.delete(0, tk.END)
        
        cursor = self.conexao.cursor()
        cursor.execute("SELECT id, nome, cpf FROM pacientes WHERE ativo = TRUE")
        
        for (id_paciente, nome, cpf) in cursor:
            self.lista_pacientes.insert(tk.END, f"{id_paciente} - {nome} - {cpf}")
    
    def remover_paciente(self):
        selecionado = self.lista_pacientes.curselection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um paciente!")
            return
            
        item = self.lista_pacientes.get(selecionado)
        id_paciente = item.split(" - ")[0]
        
        try:
            cursor = self.conexao.cursor()
            
            # Em vez de DELETE, fazemos "remoção lógica" (LGPD)
            cursor.execute(
                "UPDATE pacientes SET ativo = FALSE WHERE id = %s",
                (id_paciente,)
            )
            self.conexao.commit()
            
            # Registrar log
            cursor.execute("INSERT INTO logs (acao) VALUES ('Removeu paciente')")
            self.conexao.commit()
            
            messagebox.showinfo("Sucesso", "Paciente removido (anonimizado)!")
            self.carregar_pacientes()
            self.carregar_logs()
            
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Falha ao remover: {err}")
    
    def carregar_logs(self):
        self.text_logs.delete(1.0, tk.END)
        
        cursor = self.conexao.cursor()
        cursor.execute("SELECT acao, data_hora FROM logs ORDER BY data_hora DESC LIMIT 5")
        
        for (acao, data_hora) in cursor:
            self.text_logs.insert(tk.END, f"{data_hora}: {acao}\n")

# Executar o sistema
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaClinicaSimples(root)
    root.mainloop()