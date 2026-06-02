def aplicar_desconto(valor_total, percentual):
    if percentual < 0 or percentual > 100:
        raise ValueError("Percentual de desconto inválido")

    valor_final = valor_total - (valor_total * percentual / 100)

    if valor_final < 0:
        raise ValueError("Valor final não pode ser negativo")

    return valor_final
