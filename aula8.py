def calcular_pontos(livros_comprados):
    pontos = 0
    for livros in livros_comprados:
        if livros == 0:
            pontos += 0
        elif livros == 1:
            pontos += 5
        elif livros == 2:
            pontos += 15
        elif livros == 3:
            pontos += 30 
        else:pontos += 60
    return pontos


def mostrar_brindes(pontos):
    if 20 <= pontos <= 30:
        return "Pode escolher entre: EcoBag OU Caneta personalizada"
    elif 35 <= pontos <= 60:
        return "Pode escolher entre: Livro (até R$30) OU Luminária de cabeceira"
    elif pontos >= 65:
        return "Pode escolher entre: 2 livros (até R$100) OU Powerbank"
    else:
        return "Pontos insuficientes para trocar por brindes"


def main():
    print("Programa de Fidelidade da Livraria")
    print("Digite a quantidade de livros comprados em cada compra (digite -1 para encerrar):")

    compras = []
    while True:
        try:
            livros = int(input("Livros comprados nesta compra: "))
            if livros == -1:
                break
            compras.append(livros)
        except ValueError:
            print("Por favor, digite um número válido.")

    pontos_totais = calcular_pontos(compras)

    print(f"\nTotal de pontos acumulados: {pontos_totais}")
    print(mostrar_brindes(pontos_totais))


if __name__ == "__main__":
    main()