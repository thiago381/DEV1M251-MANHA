from dao.produto_dao import ProdutoDAO
from dao.venda_dao import VendaDAO
from modelos.carrinho import Carrinho
from modelos.venda import Venda

def mostrar_menu_pagamento():
    print("     FORMAS DE PAGAMENTO    ")
    print("1- À vista em dinheiro ou PIX - 10% de desconto")
    print("2- Cartão de débito - 5% de desconto")
    print("3- Cartão de crédito 1x - mesmo preço")
    print("4- Cartão de crédito 2x - acréscimo de 5%")
    print("5- Cartão de crédito 3x - acréscimo de 10%")
    print("6- Cartão de crédito 4x - acréscimo de 15%")

def main():
    produto_dao = ProdutoDAO()
    venda_dao = VendaDAO()

    total_arrecadado_dia = 0
    total_itens_vendidos = 0
    atender_novo_cliente = 's'

    # Carrega produtos do banco
    produtos = produto_dao.buscar_todos()

    while atender_novo_cliente.lower() == 's':
        carrinho = Carrinho()
        print("=================MERCADO DO WILL=================")

        while True:
            print("===============MENU DE PRODUTOS==============")
            for produto in produtos:
                print(f"[{produto.id}] {produto.nome} R$ {produto.preco:.2f}")

            try:
                opcao = int(input("Selecione uma das opções: "))
            except ValueError:
                print("Opção inválida. Tente novamente.")
                continue

            produto_escolhido = next((p for p in produtos if p.id == opcao), None)
            if not produto_escolhido:
                print("Você escolheu uma opção inválida!")
                continue

            try:
                quantidade = int(input("Quantos produtos você deseja adicionar? "))
                if quantidade <= 0:
                    print("Quantidade deve ser maior que zero.")
                    continue
            except ValueError:
                print("Quantidade inválida.")
                continue

            carrinho.adicionar_item(produto_escolhido, quantidade)
            print(f"{quantidade} unidade(s) de {produto_escolhido.nome} adicionada(s) ao carrinho.")

            continuar = input("Deseja adicionar mais produtos ao carrinho? (S/N): ")
            if continuar.lower() != 's':
                break

        # Mostrar resumo do carrinho
        itens_carrinho = carrinho.listar_itens()
        print("\nResumo do carrinho:")
        for item in itens_carrinho:
            print(f"- {item['produto'].nome}: {item['quantidade']} unidade(s) - R$ {item['produto'].preco * item['quantidade']:.2f}")

        print(f"Total parcial: R$ {carrinho.calcular_total():.2f}\n")

        mostrar_menu_pagamento()

        forma_pagamento = 0
        while forma_pagamento not in range(1, 7):
            try:
                forma_pagamento = int(input("Escolha uma das opções acima: "))
                if forma_pagamento not in range(1, 7):
                    print("Opção inválida, tente novamente.")
            except ValueError:
                print("Entrada inválida, digite um número.")

        venda = Venda(carrinho, forma_pagamento)
        venda_dao.salvar_venda(venda)

        print("=================CHECKOUT==================")
        print(f"Forma de pagamento: {forma_pagamento}")
        total_itens = sum(item['quantidade'] for item in itens_carrinho)
        print(f"Quantidade total de produtos comprados: {total_itens} unidades.")
        print(f"Valor total da sua compra R$ {venda.valor_final:.2f}")

        total_arrecadado_dia += venda.valor_final
        total_itens_vendidos += total_itens

        atender_novo_cliente = input("Deseja atender um novo cliente? (S/N): ")

    print("===============FECHAMENTO DO DIA=================")
    print(f"Total de itens vendidos no dia: {total_itens_vendidos} unidades.")
    print(f"Valor total arrecadado no dia: R$ {total_arrecadado_dia:.2f}")
    print("===========================================")

    produto_dao.fechar()
    venda_dao.fechar()

if __name__ == "__main__":
    main()
