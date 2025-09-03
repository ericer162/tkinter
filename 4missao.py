import mysql.connector
from mysql.connector import Error
from datetime import datetime

class DatabaseManager:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='gestao_vendas',
                user='root',
                password=''  # Coloque sua senha aqui
            )
            
            if self.connection.is_connected():
                print("Conexão ao MySQL estabelecida com sucesso")
                
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
    
    def __del__(self):
        if hasattr(self, 'connection') and self.connection.is_connected():
            self.connection.close()
            print("Conexão MySQL fechada")
    
    # Operação com JOIN, GROUP BY e ORDER BY 
    def gerar_relatorio_vendas(self, data_inicio=None, data_fim=None):
        try:
            cursor = self.connection.cursor(dictionary=True)
            
            query = """
            SELECT 
                v.id AS venda_id,
                v.data_venda,
                u.nome AS vendedor,
                COUNT(iv.id) AS total_itens,
                v.total AS valor_total
            FROM 
                vendas v
            JOIN 
                usuarios u ON v.usuario_id = u.id
            JOIN 
                itens_venda iv ON v.id = iv.venda_id
            """
            
            # Filtro por período 
            if data_inicio and data_fim:
                query += " WHERE v.data_venda BETWEEN %s AND %s"
                cursor.execute(query, (data_inicio, data_fim))
            else:
                query += " GROUP BY v.id, v.data_venda, u.nome, v.total ORDER BY v.data_venda DESC"
                cursor.execute(query)
            
            resultados = cursor.fetchall()
            
            print("\nRelatório de Vendas:")
            print("-" * 60)
            for row in resultados:
                print(f"Venda ID: {row['venda_id']}")
                print(f"Data: {row['data_venda']}")
                print(f"Vendedor: {row['vendedor']}")
                print(f"Itens: {row['total_itens']}")
                print(f"Total: R${row['valor_total']:.2f}")
                print("-" * 60)
            
            return resultados
            
        except Error as e:
            print(f"Erro ao gerar relatório: {e}")
            return None
    
    def registrar_venda(self, usuario_id, itens):
        try:
            cursor = self.connection.cursor()
            
            # Calcula o total da venda
            total = sum(item['preco'] * item['quantidade'] for item in itens)
            
            # Insere a venda
            cursor.execute(
                "INSERT INTO vendas (usuario_id, total) VALUES (%s, %s)",
                (usuario_id, total)
            )
            venda_id = cursor.lastrowid
            
            # Insere os itens da venda
            for item in itens:
                cursor.execute(
                    """INSERT INTO itens_venda 
                    (venda_id, produto_id, quantidade, preco_unitario, subtotal)
                    VALUES (%s, %s, %s, %s, %s)""",
                    (venda_id, item['produto_id'], item['quantidade'], 
                     item['preco'], item['preco'] * item['quantidade'])
                )
            
            self.connection.commit()
            print(f"Venda registrada com sucesso! ID: {venda_id}")
            return venda_id
            
        except Error as e:
            self.connection.rollback()
            print(f"Erro ao registrar venda: {e}")
            return None
    
    def listar_produtos_estoque_baixo(self, limite=10):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(
                "SELECT id, nome, quantidade_estoque FROM produtos WHERE quantidade_estoque < %s ORDER BY quantidade_estoque ASC",
                (limite,)
            )
            
            produtos = cursor.fetchall()
            
            print("\nProdutos com estoque baixo:")
            for produto in produtos:
                print(f"{produto['id']} - {produto['nome']} (Estoque: {produto['quantidade_estoque']})")
            
            return produtos
            
        except Error as e:
            print(f"Erro ao listar produtos: {e}")
            return None

# Exemplo de uso
if __name__ == "__main__":
    db = DatabaseManager()
    
    # 1. Registrar uma nova venda
    nova_venda = {
        'usuario_id': 2,  # Carlos Silva
        'itens': [
            {'produto_id': 1, 'quantidade': 2, 'preco': 4500.00},  # Notebook Dell
            {'produto_id': 2, 'quantidade': 1, 'preco': 120.50}    # Mouse Sem Fio
        ]
    }
    venda_id = db.registrar_venda(**nova_venda)
    
    # 2. Listar produtos com estoque baixo
    db.listar_produtos_estoque_baixo()
    
    # 3. Gerar relatório de vendas (usando JOIN, GROUP BY e ORDER BY)
    db.gerar_relatorio_vendas()
    
    