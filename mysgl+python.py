import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime

class SistemaCRUDMySQL:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadrastro com MySQL")
        self.root.geometry("1200x800")
        
        # Conexão com o banco de dados
        self.conexao = self.criar_conexao()
        
        # Variáveis de controle
        self.categoria_selecionada = None
        self.produto_selecionado = None
        
        # Criar interface
        self.criar_interface()
        
    def criar_conexao(self):
        try:
            conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='sistema_crud'
            )
            print("Conexão ao MySQL estabelecida com sucesso")
            return conexao
        except Error as e:
            messagebox.showerror("Erro de Conexão", f"Erro ao conectar ao MySQL: {e}")
            return None
    
    def criar_interface(self):
        # Notebook (abas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Aba de Categorias
        self.aba_categorias = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_categorias, text="Categorias")
        self.criar_aba_categorias()
        
        # Aba de Produtos
        self.aba_produtos = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_produtos, text="Produtos")
        self.criar_aba_produtos()
        
        # Aba de Relatórios
        self.aba_relatorios = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_relatorios, text="Relatórios")
        self.criar_aba_relatorios()
        
        # Atualizar dados iniciais
        self.atualizar_treeview_categorias()
        self.atualizar_treeview_produtos()
        self.atualizar_relatorio_vendas()
    
    def criar_aba_categorias(self):
        # Frame do formulário
        frame_form = ttk.LabelFrame(self.aba_categorias, text="Formulário de Categoria", padding=10)
        frame_form.pack(fill=X, padx=10, pady=5)
        
        # Campos do formulário
        ttk.Label(frame_form, text="Nome:").grid(row=0, column=0, sticky=E, padx=5, pady=5)
        self.entry_cat_nome = ttk.Entry(frame_form, width=40)
        self.entry_cat_nome.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_form, text="Descrição:").grid(row=1, column=0, sticky=E, padx=5, pady=5)
        self.entry_cat_desc = ttk.Text(frame_form, width=40, height=4)
        self.entry_cat_desc.grid(row=1, column=1, padx=5, pady=5)
        
        # Frame de botões
        frame_botoes = ttk.Frame(self.aba_categorias)
        frame_botoes.pack(fill=X, padx=10, pady=5)
        
        self.btn_cat_adicionar = ttk.Button(frame_botoes, text="Adicionar", command=self.adicionar_categoria)
        self.btn_cat_adicionar.pack(side=LEFT, padx=5)
        
        self.btn_cat_editar = ttk.Button(frame_botoes, text="Editar", state=DISABLED, command=self.editar_categoria)
        self.btn_cat_editar.pack(side=LEFT, padx=5)
        
        self.btn_cat_excluir = ttk.Button(frame_botoes, text="Excluir", state=DISABLED, command=self.excluir_categoria)
        self.btn_cat_excluir.pack(side=LEFT, padx=5)
        
        self.btn_cat_limpar = ttk.Button(frame_botoes, text="Limpar", command=self.limpar_campos_categoria)
        self.btn_cat_limpar.pack(side=LEFT, padx=5)
        
        # Treeview de categorias
        frame_tree = ttk.Frame(self.aba_categorias)
        frame_tree.pack(fill=BOTH, expand=True, padx=10, pady=5)
        
        self.tree_categorias = ttk.Treeview(frame_tree, columns=("ID", "Nome", "Descrição", "Data Criação"), show="headings")
        
        # Configurar colunas
        colunas = [
            ("ID", 50),
            ("Nome", 200),
            ("Descrição", 300),
            ("Data Criação", 150)
        ]
        
        for col, width in colunas:
            self.tree_categorias.column(col, width=width, anchor=CENTER)
            self.tree_categorias.heading(col, text=col)
        
        # Barra de rolagem
        scrollbar = ttk.Scrollbar(frame_tree, orient=VERTICAL, command=self.tree_categorias.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.tree_categorias.configure(yscrollcommand=scrollbar.set)
        self.tree_categorias.pack(fill=BOTH, expand=True)
        
        # Evento de seleção
        self.tree_categorias.bind("<<TreeviewSelect>>", self.selecionar_categoria)
    
    def criar_aba_produtos(self):
        # Frame do formulário
        frame_form = ttk.LabelFrame(self.aba_produtos, text="Formulário de Produto", padding=10)
        frame_form.pack(fill=X, padx=10, pady=5)
        
        # Campos do formulário
        ttk.Label(frame_form, text="Categoria:").grid(row=0, column=0, sticky=E, padx=5, pady=5)
        self.combo_categoria = ttk.Combobox(frame_form, state="readonly")
        self.combo_categoria.grid(row=0, column=1, sticky=W, padx=5, pady=5)
        
        ttk.Label(frame_form, text="Nome:").grid(row=1, column=0, sticky=E, padx=5, pady=5)
        self.entry_prod_nome = ttk.Entry(frame_form, width=40)
        self.entry_prod_nome.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame_form, text="Descrição:").grid(row=2, column=0, sticky=E, padx=5, pady=5)
        self.entry_prod_desc = ttk.Text(frame_form, width=40, height=4)
        self.entry_prod_desc.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(frame_form, text="Preço:").grid(row=3, column=0, sticky=E, padx=5, pady=5)
        self.entry_prod_preco = ttk.Entry(frame_form, width=40)
        self.entry_prod_preco.grid(row=3, column=1, padx=5, pady=5)
        
        ttk.Label(frame_form, text="Estoque:").grid(row=4, column=0, sticky=E, padx=5, pady=5)
        self.entry_prod_estoque = ttk.Entry(frame_form, width=40)
        self.entry_prod_estoque.grid(row=4, column=1, padx=5, pady=5)
        
        # Frame de botões
        frame_botoes = ttk.Frame(self.aba_produtos)
        frame_botoes.pack(fill=X, padx=10, pady=5)
        
        self.btn_prod_adicionar = ttk.Button(frame_botoes, text="Adicionar", command=self.adicionar_produto)
        self.btn_prod_adicionar.pack(side=LEFT, padx=5)
        
        self.btn_prod_editar = ttk.Button(frame_botoes, text="Editar", state=DISABLED, command=self.editar_produto)
        self.btn_prod_editar.pack(side=LEFT, padx=5)
        
        self.btn_prod_excluir = ttk.Button(frame_botoes, text="Excluir", state=DISABLED, command=self.excluir_produto)
        self.btn_prod_excluir.pack(side=LEFT, padx=5)
        
        self.btn_prod_limpar = ttk.Button(frame_botoes, text="Limpar", command=self.limpar_campos_produto)
        self.btn_prod_limpar.pack(side=LEFT, padx=5)
        
        self.btn_prod_vender = ttk.Button(frame_botoes, text="Registrar Venda", state=DISABLED, command=self.registrar_venda)
        self.btn_prod_vender.pack(side=LEFT, padx=5)
        
        # Treeview de produtos
        frame_tree = ttk.Frame(self.aba_produtos)
        frame_tree.pack(fill=BOTH, expand=True, padx=10, pady=5)
        
        self.tree_produtos = ttk.Treeview(frame_tree, columns=("ID", "Nome", "Categoria", "Preço", "Estoque", "Atualização"), show="headings")
        
        # Configurar colunas
        colunas = [
            ("ID", 50),
            ("Nome", 200),
            ("Categoria", 150),
            ("Preço", 100),
            ("Estoque", 80),
            ("Atualização", 150)
        ]
        
        for col, width in colunas:
            self.tree_produtos.column(col, width=width, anchor=CENTER)
            self.tree_produtos.heading(col, text=col)
        
        # Barra de rolagem
        scrollbar = ttk.Scrollbar(frame_tree, orient=VERTICAL, command=self.tree_produtos.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.tree_produtos.configure(yscrollcommand=scrollbar.set)
        self.tree_produtos.pack(fill=BOTH, expand=True)
        
        # Evento de seleção
        self.tree_produtos.bind("<<TreeviewSelect>>", self.selecionar_produto)
    
    def criar_aba_relatorios(self):
        # Frame de relatório de vendas por categoria
        frame_relatorio = ttk.LabelFrame(self.aba_relatorios, text="Vendas por Categoria", padding=10)
        frame_relatorio.pack(fill=BOTH, expand=True, padx=10, pady=5)
        
        self.tree_relatorio = ttk.Treeview(frame_relatorio, columns=("Categoria", "Total Vendas", "Valor Total", "Valor Médio"), show="headings")
        
        # Configurar colunas
        colunas = [
            ("Categoria", 200),
            ("Total Vendas", 100),
            ("Valor Total", 150),
            ("Valor Médio", 150)
        ]
        
        for col, width in colunas:
            self.tree_relatorio.column(col, width=width, anchor=CENTER)
            self.tree_relatorio.heading(col, text=col)
        
        # Barra de rolagem
        scrollbar = ttk.Scrollbar(frame_relatorio, orient=VERTICAL, command=self.tree_relatorio.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.tree_relatorio.configure(yscrollcommand=scrollbar.set)
        self.tree_relatorio.pack(fill=BOTH, expand=True)
        
        # Botão para atualizar relatório
        ttk.Button(frame_relatorio, text="Atualizar Relatório", command=self.atualizar_relatorio_vendas).pack(pady=5)
    
    # Métodos para Categorias
    def atualizar_treeview_categorias(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT categoria_id, nome, descricao, data_criacao FROM categorias")
            categorias = cursor.fetchall()
            
            # Limpar treeview
            for item in self.tree_categorias.get_children():
                self.tree_categorias.delete(item)
            
            # Adicionar registros
            for cat in categorias:
                self.tree_categorias.insert("", END, values=cat)
            
            # Atualizar combobox de categorias
            self.combo_categoria['values'] = [f"{cat[0]} - {cat[1]}" for cat in categorias]
            
        except Error as e:
            messagebox.showerror("Erro", f"Erro ao carregar categorias: {e}")
    
    def selecionar_categoria(self, event):
        selecionado = self.tree_categorias.focus()
        if selecionado:
            valores = self.tree_categorias.item(selecionado, "values")
            self.categoria_selecionada = valores[0]
            
            # Preencher campos
            self.entry_cat_nome.delete(0, END)
            self.entry_cat_nome.insert(0, valores[1])
            
            self.entry_cat_desc.delete("1.0", END)
            self.entry_cat_desc.insert("1.0", valores[2])
            
            # Habilitar botões
            self.btn_cat_editar.config(state=NORMAL)
            self.btn_cat_excluir.config(state=NORMAL)
            self.btn_cat_adicionar.config(state=DISABLED)
    
    def limpar_campos_categoria(self):
        self.entry_cat_nome.delete(0, END)
        self.entry_cat_desc.delete("1.0", END)
        self.categoria_selecionada = None
        
        # Resetar botões
        self.btn_cat_editar.config(state=DISABLED)
        self.btn_cat_excluir.config(state=DISABLED)
        self.btn_cat_adicionar.config(state=NORMAL)
    
    def validar_categoria(self):
        if not self.entry_cat_nome.get():
            messagebox.showerror("Erro", "O nome da categoria é obrigatório")
            return False
        return True
    
    def adicionar_categoria(self):
        if not self.validar_categoria():
            return
            
        try:
            cursor = self.conexao.cursor()
            query = "INSERT INTO categorias (nome, descricao) VALUES (%s, %s)"
            valores = (
                self.entry_cat_nome.get(),
                self.entry_cat_desc.get("1.0", END)
            )
            
            cursor.execute(query, valores)
            self.conexao.commit()
            
            messagebox.showinfo("Sucesso", "Categoria adicionada com sucesso!")
            self.limpar_campos_categoria()
            self.atualizar_treeview_categorias()
            
        except Error as e:
            messagebox.showerror("Erro", f"Erro ao adicionar categoria: {e}")
    
    def editar_categoria(self):
        if not self.categoria_selecionada or not self.validar_categoria():
            return
            
        try:
            cursor = self.conexao.cursor()
            query = "UPDATE categorias SET nome = %s, descricao = %s WHERE categoria_id = %s"
            valores = (
                self.entry_cat_nome.get(),
                self.entry_cat_desc.get("1.0", END),
                self.categoria_selecionada
            )
            
            cursor.execute(query, valores)
            self.conexao.commit()
            
            messagebox.showinfo("Sucesso", "Categoria atualizada com sucesso!")
            self.limpar_campos_categoria()
            self.atualizar_treeview_categorias()
            
        except Error as e:
            messagebox.showerror("Erro", f"Erro ao atualizar categoria: {e}")
    
    def excluir_categoria(self):
        if not self.categoria_selecionada:
            return
            
        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir esta categoria?")
        if not resposta:
            return
            
        try:
            cursor = self.conexao.cursor()
            
            # Verificar se existem produtos associados
            cursor.execute("SELECT COUNT(*) FROM produtos WHERE categoria_id = %s", (self.categoria_selecionada,))
            count = cursor.fetchone()[0]
            
            if count > 0:
                messagebox.showerror("Erro", "Não é possível excluir categorias com produtos associados")
                return
            
            # Excluir categoria
            cursor.execute("DELETE FROM categorias WHERE categoria_id = %s", (self.categoria_selecionada,))
            self.conexao.commit()
            
            messagebox.showinfo("Sucesso", "Categoria excluída com sucesso!")
            self.limpar_campos_categoria()
            self.atualizar_treeview_categorias()
            
        except Error as e:
            messagebox.showerror("Erro", f"Erro ao excluir categoria: {e}")
    
    # Métodos para Produtos
    def atualizar_treeview_produtos(self):
        try:
            cursor = self.conexao.cursor()
            query = """
                SELECT p.produto_id, p.nome, c.nome, p.preco, p.estoque, p.data_atualizacao 
                FROM produtos p
                LEFT JOIN categorias c ON p.categoria_id = c.categoria_id
                ORDER BY p.nome
            """
            cursor.execute(query)
            produtos = cursor.fetchall()
            
            # Limpar treeview
            for item in self.tree_produtos.get_children():
                self.tree_produtos.delete(item)
            
            # Adicionar registros
            for prod in produtos:
                self.tree_produtos.insert("", END, values=prod)
                
        except Error as e:
            messagebox.showerror("Erro", f"Erro ao carregar produtos: {e}")
    
    def selecionar_produto(self, event):
        selecionado = self.tree_produtos.focus()
        if selecionado:
            valores = self.tree_produtos.item(selecionado, "values")
            self.produto_selecionado = valores[0]
            
            # Preencher campos
            self.entry_prod_nome.delete(0, END)
            self.entry_prod_nome.insert(0, valores[1])
            
            # Encontrar categoria no combobox
            cat_text = f"{valores[2]}"
            for i, item in enumerate(self.combo_categoria['values']):
                if cat_text in item:
                    self.combo_categoria.current(i)
                    break
            
            self.entry_prod_desc.delete("1.0", END)
            
            # Buscar descrição completa do produto
            try:
                cursor = self.conexao.cursor()
                cursor.execute("SELECT descricao FROM produtos WHERE produto_id = %s", (self.produto_selecionado,))
                descricao = cursor.fetchone()[0]
                self.entry_prod_desc.insert("1.0", descricao)
            except Error as e:
                messagebox.showerror("Erro", f"Erro ao carregar descrição: {e}")
            
            self.entry_prod_preco.delete(0, END)
            self.entry_prod_preco.insert(0, valores[3])
            
            self.entry_prod_estoque.delete(0, END)
            self.entry_prod_estoque.insert(0, valores[4])
            
            # Habilitar botões
            self.btn_prod_editar.config(state=NORMAL)
            self.btn_prod_excluir.config(state=NORMAL)
            self.btn_prod_vender.config(state=NORMAL)
            self.btn_prod_adicionar.config(state=DISABLED)
    
    def limpar_campos_produto(self):
        self.entry_prod_nome.delete(0, END)
        self.combo_categoria.set('')
        self.entry_prod_desc.delete("1.0", END)
        self.entry_prod_preco.delete(0, END)
        self.entry_prod_estoque.delete(0, END)
        self.produto_selecionado = None
        
        # Resetar botões
        self.btn_prod_editar.config(state=DISABLED)
        self.btn_prod_excluir.config(state=DISABLED)
        self.btn_prod_vender.config(state=DISABLED)
        self.btn_prod_adicionar.config(state=NORMAL)
    
    def validar_produto(self):
        erros = []
        
        if not self.entry_prod_nome.get():
            erros.append("O nome do produto é obrigatório")
        
        if not self.combo_categoria.get():
            erros.append("A categoria é obrigatória")
        
        try:
            float(self.entry_prod_preco.get())
        except:
            erros.append("Preço inválido")
        
        try:
            int(self.entry_prod_estoque.get())
        except:
            erros.append("Estoque inválido")
        
        if erros:
            messagebox.showerror("Erro de Validação", "\n".join(erros))
            return False
        
        return True
    
    def adicionar_produto(self):
        if not self.validar_produto():
            return
            
        try:
            cursor = self.conexao.cursor()
            query = """
                INSERT INTO produtos 
                (nome, descricao, preco, estoque, categoria_id) 
                VALUES (%s, %s, %s, %s, %s)
            """
            
            # Extrair ID da categoria selecionada no combobox
            cat_id = self.combo_categoria.get().split(" - ")[0]
            
            valores = (
                self.entry_prod_nome.get(),
                self.entry_prod_desc.get("1.0", END),
                float(self.entry_prod_preco.get()),
                int(self.entry_prod_estoque.get()),
                cat_id
            )
            
            cursor.execute(query, valores)
            self.conexao.commit()
            
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
            self.limpar_campos_produto()
            self.atualizar_treeview_produtos()
            
        except Error as e:
            messagebox.showerror("Erro", f"Erro ao adicionar produto: {e}")
    
    def editar_produto(self):
        if not self.produto_selecionado or not self.validar_produto():
            return
            
        try:
            cursor = self.conexao.cursor()
            query = """
                UPDATE produtos 
                SET nome = %s, descricao = %s, preco = %s, estoque = %s, categoria_id = %s 
                WHERE produto_id = %s
            """
            
            # Extrair ID da categoria selecionada no combobox
            cat_id = self.combo_categoria.get().split(" - ")[0]
            
            valores = (
                self.entry_prod_nome.get(),
                self.entry_prod_desc.get("1.0", END),
                float(self.entry_prod_preco.get()),
                int(self.entry_prod_estoque.get()),
                cat_id,
                self.produto_selecionado
            )
            
            cursor.execute(query, valores)
            self.conexao.commit()
            
            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
            self.limpar_campos_produto()
            self.atualizar_treeview_produtos()
            
        except Error as e:
            messagebox.showerror("Erro", f"Erro ao atualizar produto: {e}")
    
    def excluir_produto(self):
        if not self.produto_selecionado:
            return
            
        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir este produto?")
        if not resposta:
            return
            
        try:
            cursor = self.conexao.cursor()
            
            # Verificar se existem vendas associadas
            cursor.execute("SELECT COUNT(*) FROM vendas WHERE produto_id = %s", (self.produto_selecionado,))
            count = cursor.fetchone()[0]
            
            if count > 0:
                messagebox.showerror("Erro", "Não é possível excluir produtos com vendas associadas")
                return
            
            # Excluir produto
            cursor.execute("DELETE FROM produtos WHERE produto_id = %s", (self.produto_selecionado,))
            self.conexao.commit()
            
            messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
            self.limpar_campos_produto()
            self.atualizar_treeview_produtos()
            
        except Error as e:
            messagebox.showerror("Erro", f"Erro ao excluir produto: {e}")
    
    def registrar_venda(self):
        if not self.produto_selecionado:
            return
            
        # Janela de diálogo para quantidade
        dialog = Toplevel(self.root)
        dialog.title("Registrar Venda")
        dialog.geometry("300x150")
        
        ttk.Label(dialog, text="Quantidade:").pack(pady=10)
        entry_quantidade = ttk.Entry(dialog)
        entry_quantidade.pack(pady=5)
        entry_quantidade.focus()
        
        def confirmar_venda():
            try:
                quantidade = int(entry_quantidade.get())
                if quantidade <= 0:
                    messagebox.showerror("Erro", "Quantidade deve ser maior que zero")
                    return
                    
                # Verificar estoque
                cursor = self.conexao.cursor()
                cursor.execute("SELECT estoque, preco FROM produtos WHERE produto_id = %s", (self.produto_selecionado,))
                estoque, preco = cursor.fetchone()
                
                if quantidade > estoque:
                    messagebox.showerror("Erro", "Quantidade indisponível em estoque")
                    return
                
                # Registrar venda
                valor_total = quantidade * preco
                query = "INSERT INTO vendas (produto_id, quantidade, valor_total) VALUES (%s, %s, %s)"
                cursor.execute(query, (self.produto_selecionado, quantidade, valor_total))
                
                # Atualizar estoque
                cursor.execute("UPDATE produtos SET estoque = estoque - %s WHERE produto_id = %s", 
                             (quantidade, self.produto_selecionado))
                
                self.conexao.commit()
                
                messagebox.showinfo("Sucesso", f"Venda registrada!\nTotal: R$ {valor_total:.2f}")
                dialog.destroy()
                self.atualizar_treeview_produtos()
                self.atualizar_relatorio_vendas()
                
            except ValueError:
                messagebox.showerror("Erro", "Quantidade inválida")
            except Error as e:
                messagebox.showerror("Erro", f"Erro ao registrar venda: {e}")
        
        ttk.Button(dialog, text="Confirmar", command=confirmar_venda).pack(pady=10)
    
    # Métodos para Relatórios
    def atualizar_relatorio_vendas(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT * FROM vendas_por_categoria")
            vendas = cursor.fetchall()
            
            # Limpar treeview
            for item in self.tree_relatorio.get_children():
                self.tree_relatorio.delete(item)
            
            # Adicionar registros
            for venda in vendas:
                self.tree_relatorio.insert("", END, values=venda)
                
        except Error as e:
            messagebox.showerror("Erro", f"Erro ao carregar relatório: {e}")

if __name__ == "__main__":
    root = Tk()
    app = SistemaCRUDMySQL(root)
    root.mainloop()