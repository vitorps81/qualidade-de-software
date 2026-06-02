def calcular_taxa_entrega(distancia_km):
    if distancia_km < 0:
        raise ValueError("Distância inválida")

    taxa_fixa = 5.00

    if distancia_km <= 3:
        return taxa_fixa

    km_adicional = distancia_km - 3
    return taxa_fixa + (km_adicional * 2.00)
