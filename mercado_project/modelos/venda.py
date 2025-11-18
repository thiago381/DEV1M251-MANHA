from datetime import datetime

class Venda:
    def __init__(self, carrinho, forma_pagamento):
        self._carrinho = carrinho
        self._forma_pagamento = forma_pagamento
        self._data_venda = datetime.now()
        self._total = self._carrinho.calcular_total()
        self._valor_final = self._calcular_valor_final()

    def _calcular_valor_final(self):
        total = self._total
        # Aplica descontos e acréscimos conforme a forma de pagamento
        if self._forma_pagamento == 1:  # À vista dinheiro ou PIX (10% desconto)
            return total * 0.90
        elif self._forma_pagamento == 2:  # Débito (5% desconto)
            return total * 0.95
        elif self._forma_pagamento == 3:  # Crédito 1x (mesmo valor)
            return total
        elif self._forma_pagamento == 4:  # Crédito 2x (+5%)
            return total * 1.05
        elif self._forma_pagamento == 5:  # Crédito 3x (+10%)
            return total * 1.10
        elif self._forma_pagamento == 6:  # Crédito 4x (+15%)
            return total * 1.15
        else:
            return total

    @property
    def total(self):
        return self._total

    @property
    def valor_final(self):
        return self._valor_final

    @property
    def forma_pagamento(self):
        return self._forma_pagamento

    @property
    def data_venda(self):
        return self._data_venda

    @property
    def itens(self):
        # Retorna os itens do carrinho para salvar na venda
        return self._carrinho.listar_itens()
