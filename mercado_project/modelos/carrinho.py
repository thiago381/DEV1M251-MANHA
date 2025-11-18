class Carrinho:
    def __init__(self):
        # Itens do carrinho: lista de dicionários {'produto': Produto, 'quantidade': int}
        self._itens = []

    def adicionar_item(self, produto, quantidade):
        # Adiciona item ao carrinho, se já existir incrementa quantidade
        for item in self._itens:
            if item['produto'].id == produto.id:
                item['quantidade'] += quantidade
                return
        self._itens.append({'produto': produto, 'quantidade': quantidade})

    def remover_item(self, produto_id):
        # Remove item pelo id do produto
        self._itens = [item for item in self._itens if item['produto'].id != produto_id]

    def listar_itens(self):
        # Retorna lista dos itens no carrinho
        return self._itens

    def calcular_total(self):
        # Calcula o valor total do carrinho
        total = 0
        for item in self._itens:
            total += item['produto'].preco * item['quantidade']
        return total
