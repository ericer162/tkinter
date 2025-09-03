import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
from tkinter import font as tkfont
from datetime import datetime

class SistemaCRUD:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadrastro")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f0f0f0")
        
        self.fonte = tkfont.Font(family="Segoe UI", size=10)
        self.fonte_titulo = tkfont.Font(family="Segoe UI", size=12, weight="bold")
        

        self.arquivo_dados = "dados.json"
        self.dados = self.carregar_dados()
        self.id_selecionado = None
        
        self.configurar_estilo()
        
        self.criar_interface()
        
    def configurar_estilo(self):
        style = ttk.Style()
        style.theme_use("clam")
        

        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", font=self.fonte)
        style.configure("TButton", font=self.fonte, padding=5)
        style.configure("TEntry", font=self.fonte, padding=5)
        style.configure("Treeview", font=self.fonte, rowheight=25)
        style.configure("Treeview.Heading", font=self.fonte_titulo)
        style.map("TButton", 
                 foreground=[('pressed', 'white'), ('active', 'white')],
                 background=[('pressed', '#0052cc'), ('active', '#0066ff')])
        
    def carregar_dados(self):
        if os.path.exists(self.arquivo_dados):
            try:
                with open(self.arquivo_dados, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def salvar_dados(self):
        with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
            json.dump(self.dados, f, indent=4, ensure_ascii=False)
    
    def criar_interface(self):
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
 
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill="x", pady=(0, 10))
        
        ttk.Label(header_frame, text="Sistema CRUD Completo", font=self.fonte_titulo).pack(side="left")
        
        search_frame = ttk.Frame(main_frame)
        search_frame.pack(fill="x", pady=(0, 10))
        
        ttk.Label(search_frame, text="Buscar:").pack(side="left", padx=(0, 5))
        self.search_entry = ttk.Entry(search_frame, width=40)
        self.search_entry.pack(side="left", padx=5)
        self.search_entry.bind("<KeyRelease>", self.buscar_registros)
        
        ttk.Button(search_frame, text="Buscar", command=self.buscar_registros).pack(side="left", padx=5)
        ttk.Button(search_frame, text="Limpar Busca", command=self.limpar_busca).pack(side="left", padx=5)
        
        form_frame = ttk.LabelFrame(main_frame, text="Formulário de Cadastro", padding=10)
        form_frame.pack(fill="x", pady=(0, 10))
        
        ttk.Label(form_frame, text="Nome Completo:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entry_nome = ttk.Entry(form_frame, width=50)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(form_frame, text="E-mail:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_email = ttk.Entry(form_frame, width=50)
        self.entry_email.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(form_frame, text="Telefone:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.entry_telefone = ttk.Entry(form_frame, width=50)
        self.entry_telefone.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(form_frame, text="Data de Nascimento:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.entry_data_nasc = ttk.Entry(form_frame, width=50)
        self.entry_data_nasc.grid(row=3, column=1, padx=5, pady=5)
        ttk.Button(form_frame, text="Hoje", width=5, command=self.inserir_data_atual).grid(row=3, column=2, padx=5)
        
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill="x", pady=(0, 10))
        
        self.btn_adicionar = ttk.Button(buttons_frame, text="Adicionar", style="Accent.TButton", command=self.adicionar_registro)
        self.btn_adicionar.pack(side="left", padx=5)
        
        self.btn_editar = ttk.Button(buttons_frame, text="Editar", state="disabled", command=self.editar_registro)
        self.btn_editar.pack(side="left", padx=5)
        
        self.btn_excluir = ttk.Button(buttons_frame, text="Excluir", state="disabled", command=self.excluir_registro)
        self.btn_excluir.pack(side="left", padx=5)
        
        self.btn_limpar = ttk.Button(buttons_frame, text="Limpar", command=self.limpar_campos)
        self.btn_limpar.pack(side="left", padx=5)
        
        self.btn_exportar = ttk.Button(buttons_frame, text="Exportar CSV", command=self.exportar_csv)
        self.btn_exportar.pack(side="right", padx=5)
        
        tree_frame = ttk.Frame(main_frame)
        tree_frame.pack(fill="both", expand=True)
        
        self.tree = ttk.Treeview(tree_frame, columns=("ID", "Nome", "E-mail", "Telefone", "Nascimento"), show="headings")
        

        colunas = [
            ("ID", 50),
            ("Nome", 200),
            ("E-mail", 200),
            ("Telefone", 100),
            ("Nascimento", 100)
        ]
        
        for col, width in colunas:
            self.tree.column(col, width=width, anchor="center")
            self.tree.heading(col, text=col)
        
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(fill="both", expand=True)
        
        self.tree.bind("<<TreeviewSelect>>", self.selecionar_registro)
        
        self.status_bar = ttk.Label(main_frame, text=f"Total de registros: {len(self.dados)}", relief="sunken")
        self.status_bar.pack(fill="x", pady=(10, 0))
        

        self.atualizar_treeview()
    
    def inserir_data_atual(self):
        data_atual = datetime.now().strftime("%d/%m/%Y")
        self.entry_data_nasc.delete(0, "end")
        self.entry_data_nasc.insert(0, data_atual)
    
    def buscar_registros(self, event=None):
        termo = self.search_entry.get().lower()
        
        if not termo:
            self.atualizar_treeview()
            return
        
        resultados = []
        for registro in self.dados:
            if (termo in registro["nome"].lower() or 
                termo in registro["email"].lower() or 
                termo in registro["telefone"].lower() or
                termo in registro.get("data_nasc", "").lower()):
                resultados.append(registro)
        
        self.atualizar_treeview(resultados)
    
    def limpar_busca(self):
        self.search_entry.delete(0, "end")
        self.atualizar_treeview()
    
    def atualizar_treeview(self, dados=None):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        registros = dados if dados is not None else self.dados
        
        for registro in registros:
            self.tree.insert("", "end", values=(
                registro["id"],
                registro["nome"],
                registro["email"],
                registro["telefone"],
                registro.get("data_nasc", "")
            ))
        
        self.status_bar.config(text=f"Total de registros: {len(registros)}")
    
    def selecionar_registro(self, event):
        selecionado = self.tree.focus()
        if selecionado:
            valores = self.tree.item(selecionado, "values")
            self.id_selecionado = valores[0]
            
            registro = next((r for r in self.dados if str(r["id"]) == self.id_selecionado), None)
            if registro:
                self.entry_nome.delete(0, "end")
                self.entry_nome.insert(0, registro["nome"])
                
                self.entry_email.delete(0, "end")
                self.entry_email.insert(0, registro["email"])
                
                self.entry_telefone.delete(0, "end")
                self.entry_telefone.insert(0, registro["telefone"])
                
                self.entry_data_nasc.delete(0, "end")
                self.entry_data_nasc.insert(0, registro.get("data_nasc", ""))
                
                self.btn_editar.config(state="normal")
                self.btn_excluir.config(state="normal")
                self.btn_adicionar.config(state="disabled")
    
    def limpar_campos(self):
        self.entry_nome.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.entry_telefone.delete(0, "end")
        self.entry_data_nasc.delete(0, "end")
        self.id_selecionado = None
        

        self.btn_editar.config(state="disabled")
        self.btn_excluir.config(state="disabled")
        self.btn_adicionar.config(state="normal")
        
        self.entry_nome.focus()
    
    def validar_campos(self):
        erros = []
        
        if not self.entry_nome.get():
            erros.append("O nome é obrigatório")
        
        if not self.entry_email.get():
            erros.append("O e-mail é obrigatório")
        elif "@" not in self.entry_email.get():
            erros.append("E-mail inválido")
        
        if not self.entry_telefone.get():
            erros.append("O telefone é obrigatório")
        
        if erros:
            messagebox.showerror("Erro de Validação", "\n".join(erros))
            return False
        
        return True
    
    def adicionar_registro(self):
        if not self.validar_campos():
            return
            
        novo_id = max([r["id"] for r in self.dados], default=0) + 1
        
        novo_registro = {
            "id": novo_id,
            "nome": self.entry_nome.get(),
            "email": self.entry_email.get(),
            "telefone": self.entry_telefone.get(),
            "data_nasc": self.entry_data_nasc.get(),
            "data_cadastro": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        
        self.dados.append(novo_registro)
        self.salvar_dados()
        self.atualizar_treeview()
        self.limpar_campos()
        
        messagebox.showinfo("Sucesso", "Registro adicionado com sucesso!")
    
    def editar_registro(self):
        if not self.validar_campos() or not self.id_selecionado:
            return
            
        for registro in self.dados:
            if str(registro["id"]) == self.id_selecionado:
                registro["nome"] = self.entry_nome.get()
                registro["email"] = self.entry_email.get()
                registro["telefone"] = self.entry_telefone.get()
                registro["data_nasc"] = self.entry_data_nasc.get()
                registro["data_atualizacao"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                break
                
        self.salvar_dados()
        self.atualizar_treeview()
        self.limpar_campos()
        
        messagebox.showinfo("Sucesso", "Registro atualizado com sucesso!")
    
    def excluir_registro(self):
        if not self.id_selecionado:
            return
            
        resposta = messagebox.askyesno(
            "Confirmação", 
            "Tem certeza que deseja excluir este registro?",
            icon="warning"
        )
        
        if resposta:
            self.dados = [r for r in self.dados if str(r["id"]) != self.id_selecionado]
            self.salvar_dados()
            self.atualizar_treeview()
            self.limpar_campos()
            
            messagebox.showinfo("Sucesso", "Registro excluído com sucesso!")
    
    def exportar_csv(self):
        if not self.dados:
            messagebox.showwarning("Aviso", "Não há dados para exportar")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("Arquivos CSV", "*.csv")],
            title="Salvar como"
        )
        
        if not file_path:
            return
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("ID;Nome;E-mail;Telefone;Data Nascimento;Data Cadastro\n")
                
                for registro in self.dados:
                    linha = (
                        f"{registro['id']};"
                        f"{registro['nome']};"
                        f"{registro['email']};"
                        f"{registro['telefone']};"
                        f"{registro.get('data_nasc', '')};"
                        f"{registro.get('data_cadastro', '')}\n"
                    )
                    f.write(linha)
            
            messagebox.showinfo("Sucesso", f"Dados exportados com sucesso para:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao exportar dados:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    
    style = ttk.Style()
    style.configure("Accent.TButton", foreground="white", background="#0078d7")
    
    app = SistemaCRUD(root)
    root.mainloop()