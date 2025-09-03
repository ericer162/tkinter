import mysql.connector
from mysql.connector import Error
from datetime import datetime

def criar_banco_dados():
    """Função para criar o banco de dados e todas as tabelas"""
    
    # Script SQL completo
    sql_script = """
    -- Criação do banco de dados
    DROP DATABASE IF EXISTS sistema_vendas;
    CREATE DATABASE sistema_vendas;
    USE sistema_vendas;

    -- Tabela de clientes
    CREATE TABLE clientes (
        cliente_id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE,
        telefone VARCHAR(20),
        data_cadastro DATE DEFAULT CURRENT_DATE
    );

    -- Tabela de produtos
    CREATE TABLE produtos (
        produto_id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        descricao TEXT,
        preco DECIMAL(10, 2) NOT NULL,
        estoque INT NOT NULL DEFAULT 0,
        categoria VARCHAR(50)
    );

    -- Tabela de pedidos
    CREATE TABLE pedidos (
        pedido_id INT AUTO_INCREMENT PRIMARY KEY,
        cliente_id INT NOT NULL,
        data_pedido DATETIME DEFAULT CURRENT_TIMESTAMP,
        status VARCHAR(20) DEFAULT 'pendente',
        total DECIMAL(10, 2),
        FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
    );

    -- Tabela de itens do pedido
    CREATE TABLE itens_pedido (
        item_id INT AUTO_INCREMENT PRIMARY KEY,
        pedido_id INT NOT NULL,
        produto_id INT NOT NULL,
        quantidade INT NOT NULL,
        preco_unitario DECIMAL(10, 2) NOT NULL,
        subtotal DECIMAL(10, 2) GENERATED ALWAYS AS (quantidade * preco_unitario) STORED,
        FOREIGN KEY (pedido_id) REFERENCES pedidos(pedido_id),
        FOREIGN KEY (produto_id) REFERENCES produtos(produto_id)
    );

    -- VIEW para relatório de vendas por cliente
    CREATE VIEW vendas_por_cliente AS
    SELECT 
        c.cliente_id,
        c.nome AS cliente,
        COUNT(p.pedido_id) AS total_pedidos,
        SUM(COALESCE(ip.subtotal, 0)) AS valor_total_gasto
    FROM 
        clientes c
    LEFT JOIN 
        pedidos p ON c.cliente_id = p.cliente_id
    LEFT JOIN 
        itens_pedido ip ON p.pedido_id = ip.pedido_id
    GROUP BY 
        c.cliente_id, c.nome
    ORDER BY 
        valor_total_gasto DESC;

    -- Inserção de dados de exemplo
    INSERT INTO clientes (nome, email, telefone) VALUES
    ('João Silva', 'joao@email.com', '(11) 9999-8888'),
    ('Maria Souza', 'maria@email.com', '(21) 7777-6666'),
    ('Carlos Oliveira', 'carlos@email.com', '(31) 5555-4444');

    INSERT INTO produtos (nome, descricao, preco, estoque, categoria) VALUES
    ('Notebook Elite', 'Notebook 16GB RAM, SSD 512GB', 4500.00, 10, 'Eletrônicos'),
    ('Smartphone Pro', 'Tela 6.5", 128GB, Câmera Tripla', 3200.00, 15, 'Eletrônicos'),
    ('Mesa Escritório', 'Mesa de madeira 140x80cm', 899.90, 5, 'Móveis');

    INSERT INTO pedidos (cliente_id, status, total) VALUES
    (1, 'entregue', 4500.00),
    (2, 'processando', 4099.90),
    (1, 'pendente', 3200.00);

    INSERT INTO itens_pedido (pedido_id, produto_id, quantidade, preco_unitario) VALUES
    (1, 1, 1, 4500.00),
    (2, 3, 1, 899.90),
    (2, 2, 1, 3200.00),
    (3, 2, 1, 3200.00);
    """
    
    try:
        # Conecta ao MySQL (sem especificar o banco de dados)
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        
        # Divide o script em comandos individuais
        commands = sql_script.split(';')
        
        cursor = conn.cursor()
        for command in commands:
            if command.strip():
                cursor.execute(command)
        
        conn.commit()
        print("Banco de dados e tabelas criados com sucesso!")
        
    except Error as e:
        print(f"Erro ao criar banco de dados: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

class DatabaseManager:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',  # substitua pelo seu usuário
                password='',  # substitua pela sua senha
                database='sistema_vendas'
            )
            print("Conexão ao MySQL estabelecida com sucesso!")
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
            self.connection = None

    def execute_query(self, query, params=None, fetch=False):
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params or ())
            if fetch:
                result = cursor.fetchall()
            else:
                self.connection.commit()
                result = cursor.rowcount
            return result
        except Error as e:
            print(f"Erro ao executar query: {e}")
            return None
        finally:
            cursor.close()

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Conexão ao MySQL fechada.")

    # Operações CRUD para Clientes
    def adicionar_cliente(self, nome, email, telefone):
        query = """
        INSERT INTO clientes (nome, email, telefone)
        VALUES (%s, %s, %s)
        """
        return self.execute_query(query, (nome, email, telefone))

    def listar_clientes(self):
        query = "SELECT * FROM clientes ORDER BY nome"
        return self.execute_query(query, fetch=True)

    # Operações CRUD para Produtos
    def adicionar_produto(self, nome, descricao, preco, estoque, categoria):
        query = """
        INSERT INTO produtos (nome, descricao, preco, estoque, categoria)
        VALUES (%s, %s, %s, %s, %s)
        """
        return self.execute_query(query, (nome, descricao, preco, estoque, categoria))

    def listar_produtos(self):
        query = "SELECT * FROM produtos ORDER BY nome"
        return self.execute_query(query, fetch=True)

    # Operações de Pedidos
    def relatorio_vendas_por_cliente(self):
        query = "SELECT * FROM vendas_por_cliente"
        return self.execute_query(query, fetch=True)

    def criar_pedido(self, cliente_id, produtos):
        try:
            cursor = self.connection.cursor()
            
            # Inicia transação
            self.connection.start_transaction()
            
            # Cria o pedido
            cursor.execute("""
                INSERT INTO pedidos (cliente_id) 
                VALUES (%s)
            """, (cliente_id,))
            pedido_id = cursor.lastrowid
            
            total_pedido = 0
            
            # Adiciona itens ao pedido
            for produto in produtos:
                produto_id, quantidade = produto
                
                # Obtém preço do produto
                cursor.execute("""
                    SELECT preco FROM produtos 
                    WHERE produto_id = %s
                """, (produto_id,))
                preco = cursor.fetchone()[0]
                
                # Insere item do pedido
                cursor.execute("""
                    INSERT INTO itens_pedido 
                    (pedido_id, produto_id, quantidade, preco_unitario)
                    VALUES (%s, %s, %s, %s)
                """, (pedido_id, produto_id, quantidade, preco))
                
                # Atualiza estoque
                cursor.execute("""
                    UPDATE produtos 
                    SET estoque = estoque - %s 
                    WHERE produto_id = %s
                """, (quantidade, produto_id))
                
                total_pedido += preco * quantidade
            
            # Atualiza total do pedido
            cursor.execute("""
                UPDATE pedidos 
                SET total = %s 
                WHERE pedido_id = %s
            """, (total_pedido, pedido_id))
            
            # Confirma transação
            self.connection.commit()
            return pedido_id
            
        except Error as e:
            self.connection.rollback()
            print(f"Erro ao criar pedido: {e}")
            return None
        finally:
            cursor.close()

    def listar_pedidos_cliente(self, cliente_id):
        query = """
        SELECT p.pedido_id, p.data_pedido, p.status, p.total,
               GROUP_CONCAT(pr.nome SEPARATOR ', ') AS produtos
        FROM pedidos p
        JOIN itens_pedido ip ON p.pedido_id = ip.pedido_id
        JOIN produtos pr ON ip.produto_id = pr.produto_id
        WHERE p.cliente_id = %s
        GROUP BY p.pedido_id
        ORDER BY p.data_pedido DESC
        """
        return self.execute_query(query, (cliente_id,), fetch=True)

# Função para exibir menu interativo
def menu_interativo():
    print("\nSistema de Gerenciamento de Vendas")
    print("1. Criar banco de dados e tabelas")
    print("2. Adicionar novo cliente")
    print("3. Listar todos os clientes")
    print("4. Adicionar novo produto")
    print("5. Listar todos os produtos")
    print("6. Criar novo pedido")
    print("7. Listar pedidos de um cliente")
    print("8. Ver relatório de vendas por cliente")
    print("9. Sair")
    return input("Escolha uma opção: ")

# Programa principal
if __name__ == "__main__":
    db = None
    
    while True:
        opcao = menu_interativo()
        
        if opcao == '1':
            criar_banco_dados()
            db = DatabaseManager()
            
        elif opcao == '2':
            if db is None:
                db = DatabaseManager()
            nome = input("Nome do cliente: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            db.adicionar_cliente(nome, email, telefone)
            print("Cliente adicionado com sucesso!")
            
        elif opcao == '3':
            if db is None:
                db = DatabaseManager()
            print("\nLista de Clientes:")
            for cliente in db.listar_clientes():
                print(f"{cliente['cliente_id']}: {cliente['nome']} - {cliente['email']} - {cliente['telefone']}")
                
        elif opcao == '4':
            if db is None:
                db = DatabaseManager()
            nome = input("Nome do produto: ")
            descricao = input("Descrição: ")
            preco = float(input("Preço: "))
            estoque = int(input("Estoque inicial: "))
            categoria = input("Categoria: ")
            db.adicionar_produto(nome, descricao, preco, estoque, categoria)
            print("Produto adicionado com sucesso!")
            
        elif opcao == '5':
            if db is None:
                db = DatabaseManager()
            print("\nLista de Produtos:")
            for produto in db.listar_produtos():
                print(f"{produto['produto_id']}: {produto['nome']} - R$ {produto['preco']:.2f} - Estoque: {produto['estoque']}")
                
        elif opcao == '6':
            if db is None:
                db = DatabaseManager()
            cliente_id = int(input("ID do cliente: "))
            
            # Listar produtos disponíveis
            produtos = db.listar_produtos()
            print("\nProdutos disponíveis:")
            for p in produtos:
                print(f"{p['produto_id']}: {p['nome']} - R$ {p['preco']:.2f} (Estoque: {p['estoque']})")
            
            # Coletar itens do pedido
            itens = []
            while True:
                produto_id = int(input("ID do produto (0 para finalizar): "))
                if produto_id == 0:
                    break
                quantidade = int(input("Quantidade: "))
                itens.append((produto_id, quantidade))
            
            if itens:
                pedido_id = db.criar_pedido(cliente_id, itens)
                if pedido_id:
                    print(f"Pedido {pedido_id} criado com sucesso!")
                    
        elif opcao == '7':
            if db is None:
                db = DatabaseManager()
            cliente_id = int(input("ID do cliente: "))
            pedidos = db.listar_pedidos_cliente(cliente_id)
            if pedidos:
                print(f"\nPedidos do cliente ID {cliente_id}:")
                for pedido in pedidos:
                    print(f"Pedido #{pedido['pedido_id']} - {pedido['data_pedido']}")
                    print(f"Status: {pedido['status']} - Total: R$ {pedido['total']:.2f}")
                    print(f"Produtos: {pedido['produtos']}\n")
            else:
                print("Nenhum pedido encontrado para este cliente.")
                
        elif opcao == '8':
            if db is None:
                db = DatabaseManager()
            print("\nRelatório de Vendas por Cliente:")
            for venda in db.relatorio_vendas_por_cliente():
                print(f"{venda['cliente']}:")
                print(f"  Pedidos: {venda['total_pedidos']}")
                print(f"  Valor total: R$ {venda['valor_total_gasto']:.2f}\n")
                
        elif opcao == '9':
            if db is not None:
                db.close_connection()
            print("Saindo do sistema...")
            break
            
        else:
            print("Opção inválida. Tente novamente.")