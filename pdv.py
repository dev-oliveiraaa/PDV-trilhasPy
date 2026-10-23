
def calcDesc(valor, idade, quantidade, cupom):
    if idade >= 65:
        valor = valor - (valor * 0.20)

    if valor > 100.00:
        valor = valor - (valor * 0.10)

    if quantidade > 3:
        valor = valor - (valor * 0.05)

    if cupom == "FIDELIDADE10":
        valor = valor - (valor * 0.10)

    return valor


def ler():
    try:
        valor = float(input("Digite o valor da compra (ou 0 para encerrar): \n"))
    except ValueError:
        print("Valor inválido! Digite um número.")
        return ler()

    if valor == 0:
        return None, None, None, None

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

    cupom = input(
        "Digite o cupom de fidelidade (ou Enter para ignorar): "
    ).strip()

    if cupom != "" and cupom != "FIDELIDADE10":
        print("Cupom inválido! Tente novamente.")
        return ler()

    return valor, idade, quantidade, cupom


def menu():
    compras = []

    while True:
        valor, idade, quantidade, cupom = ler()

        if valor is None:
            break

        valorFinal = calcDesc(valor, idade, quantidade, cupom)
        desconto = valor - valorFinal

        print("Valor final da compra: R$ %.2f" % valorFinal)

        compras.append(
            (valor, idade, quantidade, valorFinal, desconto)
        )

    if not compras:
        print("Nenhuma compra realizada.")
        return

    totalBruto = sum(compra[0] for compra in compras)
    totalDescontos = sum(compra[4] for compra in compras)
    totalLiquido = sum(compra[3] for compra in compras)

    print("\nResumo das compras realizadas:")
    print("Total de compras realizadas: %d" % len(compras))
    print("Total bruto das compras: R$ %.2f" % totalBruto)
    print("Total de descontos concedidos: R$ %.2f" % totalDescontos)
    print("Total líquido das compras: R$ %.2f" % totalLiquido)

    
    with open("resumo.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Resumo das compras realizadas:\n\n")

        for i, compra in enumerate(compras, start=1):
            arquivo.write("Compra %d:\n" % i)
            arquivo.write("Valor original: R$ %.2f\n" % compra[0])
            arquivo.write("Idade do cliente: %d anos\n" % compra[1])
            arquivo.write("Quantidade de itens: %d\n" % compra[2])
            arquivo.write("Valor final: R$ %.2f\n" % compra[3])
            arquivo.write("Desconto: R$ %.2f\n\n" % compra[4])

        arquivo.write("Total de compras realizadas: %d\n" % len(compras))
        arquivo.write("Total bruto das compras: R$ %.2f\n" % totalBruto)
        arquivo.write("Total de descontos concedidos: R$ %.2f\n" % totalDescontos)
        arquivo.write("Total líquido das compras: R$ %.2f\n" % totalLiquido)

    print("\nResumo salvo no arquivo resumo.txt!")


menu()