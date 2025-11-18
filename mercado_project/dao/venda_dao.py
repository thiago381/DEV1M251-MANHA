from banco.conexao import BancoDeDados

class VendaDAO:
    def __init__(self):
        self.db = BancoDeDados()

    def salvar_venda(self, venda):
        # Insere a venda e retorna o id
        sql_venda = "INSERT INTO vendas (total, forma_pagamento) VALUES (%s, %s)"
        valores_venda = (venda.valor_final, str(venda.forma_pagamento))
        self.db.cursor.execute(sql_venda, valores_venda)
        venda_id = self.db.cursor.lastrowid

        # Insere os itens da venda
        sql_item = "INSERT INTO itens_venda (venda_id, produto_id, quantidade, preco_unitario) VALUES (%s, %s, %s, %s)"
        for item in venda.itens:
            produto = item['produto']
            quantidade = item['quantidade']
            preco = produto.preco
            self.db.cursor.execute(sql_item, (venda_id, produto.id, quantidade, preco))

        self.db.commit()

    def fechar(self):
        self.db.fechar()
