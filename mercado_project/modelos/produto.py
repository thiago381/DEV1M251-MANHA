class Produto:
    def __init__(self, id_, nome, preco):
        self._id = id_
        self._nome = nome
        self._preco = preco

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco
