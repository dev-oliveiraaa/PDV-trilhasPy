
compras = []

while True:
    valor = float(input("Digite o valor da compra (ou 0 para encerrar): "))

    if valor == 0:
        break

    if valor < 0:
        print("Valor inválido. Tente novamente.")
        continue

    idade = int(input("Digite a idade do cliente: "))
    quantidade = int(input("Digite a quantidade de itens: "))

    if idade <= 0:
        print("Idade inválida. Tente novamente.")
        continue

    if quantidade <= 0:
        print("Quantidade inválida. Tente novamente.")
        continue

    cupom = input(
        "Digite o cupom de fidelidade (ou Enter para ignorar): "
    ).strip()

    if cupom != "" and cupom != "FIDELIDADE10":
        print("Cupom inválido! Tente novamente.")
        continue

    valorFinal = valor

    if idade >= 65:
        valorFinal = valorFinal - (valorFinal * 0.20)

    if valorFinal > 100.00:
        valorFinal = valorFinal - (valorFinal * 0.10)

    if quantidade > 3:
        valorFinal = valorFinal - (valorFinal * 0.05)

    if cupom == "FIDELIDADE10":
        valorFinal = valorFinal - (valorFinal * 0.10)

    desconto = valor - valorFinal

    print("Valor final da compra: R$ %.2f" % valorFinal)

    compras.append(
        (valor, idade, quantidade, valorFinal, desconto)
    )


if not compras:
    print("Nenhuma compra realizada.")

else:
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

        arquivo.write(
            "Total de compras realizadas: %d\n" % len(compras)
        )
        arquivo.write("Total bruto das compras: R$ %.2f\n" % totalBruto)
        arquivo.write(
            "Total de descontos concedidos: R$ %.2f\n" % totalDescontos
        )
        arquivo.write("Total líquido das compras: R$ %.2f\n" % totalLiquido)

    print("\nResumo salvo no arquivo resumo.txt!")
