
def calcDesc(valor, idade):
    if idade >= 65:
        valor = valor - (valor * 0.20)

    if valor > 100.00:
        valor = valor - (valor * 0.10)

    return valor


def ler():
    try:
        valor = float(input("Digite o valor da compra (ou 0 para encerrar): \n"))
    except ValueError:
        print("Valor inválido! Digite um número.")
        return ler()

    if valor == 0:
        return None, None

    if valor < 0:
        print("Valor inválido. Tente novamente.")
        return ler()

    try:
        idade = int(input("Digite a idade do cliente: "))
    except ValueError:
        print("Idade inválida! Digite um número inteiro.")
        return ler()

    if idade <= 0:
        print("Idade inválida. Tente novamente.")
        return ler()

    valor, idade = valor, idade
    return valor, idade


def menu():
    compras = []

    while True:
        valor, idade = ler()

        if valor is None:
            break

        valorFinal = calcDesc(valor, idade)
        desconto = valor - valorFinal

        print("Valor final da compra: R$ %.2f" % valorFinal)

        compras.append((valor, idade, valorFinal, desconto))

    if not compras:
        print("Nenhuma compra realizada.")
        return

    print("\nResumo das compras realizadas:")

    for compra in compras:
        print(
            "Valor: R$ %.2f, Idade: %d, Valor Final: R$ %.2f, Desconto: R$ %.2f"
            % (compra[0], compra[1], compra[2], compra[3])
        )
        
    print("Total de compras realizadas: %d" % len(compras))


menu()
