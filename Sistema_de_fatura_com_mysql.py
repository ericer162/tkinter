import tkinter as tk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error

def criar_conexao():
    """Cria uma conexão com o banco de dados SQLite"""
    conn = None
    try:
        conn = sqlite3.connect('aguas_guariroba.db')
        return conn
    except Error as e:
        print(e)
    return conn

def criar_tabela_usuarios(conn):
    """Cria a tabela de usuários se não existir"""
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        );
        """)
    except Error as e:
        print(e)

def inserir_usuario(conn, nome, senha):
    """Insere um novo usuário no banco de dados"""
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, senha))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(e)
        return None

def buscar_usuario_por_nome(conn, nome):
    """Busca um usuário pelo nome"""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nome = ?", (nome,))
        return cursor.fetchone()
    except Error as e:
        print(e)
        return None


class Usuario:
    def __init__(self, nome=None, senha=None):
        self.__nome = nome
        self.__senha = senha
        
        if nome and senha:
            self.carregar_dados(nome, senha)
    
    @property
    def nome(self):
        return self.__nome
    
    def carregar_dados(self, nome, senha):
        """Carrega os dados do usuário do banco de dados"""
        conn = criar_conexao()
        usuario_db = buscar_usuario_por_nome(conn, nome)
        conn.close()
        
        if usuario_db:
            self.__nome = usuario_db[1]
            self.__senha = usuario_db[2]
    
    def verificar_senha(self, senha_digitada):
        """Verifica se a senha digitada corresponde à senha cadastrada"""
        return self.__senha == senha_digitada


def calcular_fatura(consumo):
    """
    Calcula o valor da fatura de água e esgoto com base no consumo
    
    Args:
        consumo (float): Consumo em m³
        
    Returns:
        dict: Dicionário com os valores de água, esgoto e total
    """

    if consumo <= 5:
        valor_agua = 37.47
    else:
        valor_agua = 0
        faixas = [
            (0, 5, 1.16),     
            (6, 10, 6.46),    
            (11, 15, 6.49),   
            (16, 25, 6.55),   
            (26, 50, 11.08)   
        ]
        
        for faixa in faixas:
            inicio, fim, tarifa = faixa
            if consumo > inicio:

                m3_faixa = min(consumo, fim) - inicio
                if m3_faixa > 0:
                    valor_agua += m3_faixa * tarifa
    

    valor_esgoto = valor_agua * 0.8
    total = valor_agua + valor_esgoto
    
    return {
        'agua': round(valor_agua, 2),
        'esgoto': round(valor_esgoto, 2),
        'total': round(total, 2)
    }



class LoginWindow:
    def __init__(self, root, on_login_success):
        self.root = root
        self.root.title("Águas Guariroba - Login")
        self.root.geometry("300x200")
        self.on_login_success = on_login_success
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)
        
 
        self.label_usuario = tk.Label(self.frame, text="Usuário:")
        self.label_usuario.grid(row=0, column=0, padx=5, pady=5)
        
        self.entry_usuario = tk.Entry(self.frame)
        self.entry_usuario.grid(row=0, column=1, padx=5, pady=5)
        
        self.label_senha = tk.Label(self.frame, text="Senha:")
        self.label_senha.grid(row=1, column=0, padx=5, pady=5)
        
        self.entry_senha = tk.Entry(self.frame, show="*")
        self.entry_senha.grid(row=1, column=1, padx=5, pady=5)
        
        self.btn_login = tk.Button(
            self.frame, 
            text="Login", 
            command=self.verificar_login
        )
        self.btn_login.grid(row=2, columnspan=2, pady=10)
    
    def verificar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        
        if not usuario or not senha:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        
        user = Usuario(usuario, senha)
        
        if user.nome and user.verificar_senha(senha):
            self.on_login_success(user.nome)
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")


class MainApp:
    def __init__(self, root, usuario):
        self.root = root
        self.root.title(f"Águas Guariroba - Bem-vindo, {usuario}")
        self.root.geometry("400x300")
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)
        
        # Widgets
        self.label_consumo = tk.Label(self.frame, text="Consumo (m³):")
        self.label_consumo.grid(row=0, column=0, padx=5, pady=5)
        
        self.entry_consumo = tk.Entry(self.frame)
        self.entry_consumo.grid(row=0, column=1, padx=5, pady=5)
        
        self.btn_calcular = tk.Button(
            self.frame, 
            text="Calcular Fatura", 
            command=self.calcular
        )
        self.btn_calcular.grid(row=1, columnspan=2, pady=10)
        
        # Frame para resultados
        self.result_frame = tk.LabelFrame(self.root, text="Resultado")
        self.result_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Labels de resultado
        self.label_agua = tk.Label(self.result_frame, text="Água: R$ 0,00")
        self.label_agua.pack(pady=5)
        
        self.label_esgoto = tk.Label(self.result_frame, text="Esgoto: R$ 0,00")
        self.label_esgoto.pack(pady=5)
        
        self.label_total = tk.Label(self.result_frame, text="Total: R$ 0,00", font=('Arial', 10, 'bold'))
        self.label_total.pack(pady=5)
    
    def calcular(self):
        try:
            consumo = float(self.entry_consumo.get())
            if consumo < 0:
                raise ValueError("O consumo não pode ser negativo")
            
            fatura = calcular_fatura(consumo)
            
            self.label_agua.config(text=f"Água: R$ {fatura['agua']:.2f}")
            self.label_esgoto.config(text=f"Esgoto: R$ {fatura['esgoto']:.2f}")
            self.label_total.config(text=f"Total: R$ {fatura['total']:.2f}")
        
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor válido para o consumo!")



def iniciar_sistema():
    conn = criar_conexao()
    if conn is not None:
        criar_tabela_usuarios(conn)

        if not buscar_usuario_por_nome(conn, "admin"):
            inserir_usuario(conn, "admin", "agua2024")
        
        conn.close()
    
    root = tk.Tk()
    
    def abrir_app(usuario):
        login_window.root.destroy()
        app = MainApp(tk.Tk(), usuario)
        app.root.mainloop()
    
    login_window = LoginWindow(root, abrir_app)
    root.mainloop()

if __name__ == "__main__":
    iniciar_sistema()