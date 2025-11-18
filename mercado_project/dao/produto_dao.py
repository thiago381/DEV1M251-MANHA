from banco.conexao import BancoDeDados
from modelos.produto import Produto

class ProdutoDAO:
    def __init__(self):
        self.db = BancoDeDados()

    def buscar_todos(self):
        # Busca todos os produtos cadastrados no banco
        self.db.cursor.execute("SELECT * FROM produtos")
        produtos = []
        for linha in self.db.cursor.fetchall():
            produtos.append(Produto(linha['id'], linha['nome'], linha['preco']))
        return produtos

    def fechar(self):
        self.db.fechar()
