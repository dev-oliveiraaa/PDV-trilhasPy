
def calcDesc(valor, idade, quantidade):
    if idade >= 65:
        valor = valor - (valor * 0.20)

    if valor > 100.00:
        valor = valor - (valor * 0.10)
        
    if quantidade > 3:
        valor = valor - (valor * 0.05)

    return valor


def ler():
    try:
        valor = float(input("Digite o valor da compra (ou 0 para encerrar): \n"))
    except ValueError:
        print("Valor inválido! Digite um número.")
        return ler()

    if valor == 0:
        return None, None, None

    if valor < 0:
        print("Valor inválido. Tente novamente.")
        return ler()

    try:
        idade = int(input("Digite a idade do cliente: "))
    except ValueError:
        print("Idade inválida! Digite um número inteiro.")
        return ler()

    try:
        quantidade = int(input("Digite a quantidade de itens: "))
    except ValueError:
        print("Quantidade inválida! Digite um número inteiro.")
        return ler()

    if idade <= 0:
        print("Idade inválida. Tente novamente.")
        return ler()

    if quantidade <= 0:
        print("Quantidade inválida. Tente novamente.")
        return ler()

    return valor, idade, quantidade


def menu():
    compras = []

    while True:
        valor, idade, quantidade = ler()

        if valor is None:
            break

        valorFinal = calcDesc(valor, idade, quantidade)
        desconto = valor - valorFinal

        print("Valor final da compra: R$ %.2f" % valorFinal)

        compras.append((valor, idade, quantidade, valorFinal, desconto))

    if not compras:
        print("Nenhuma compra realizada.")
        return

    print("\nResumo das compras realizadas:")

        
    print("Total de compras realizadas: %d" % len(compras))
    print("Total bruto das compras: R$ %.2f" % sum(compra[0] for compra in compras))
    print("Total de descontos concedidos: R$ %.2f" % sum(compra[4] for compra in compras))
    print("Total líquido das compras: R$ %.2f" % sum(compra[3] for compra in compras))


menu()
