import pytest
from src.entrega import calcular_taxa_entrega


def test_deve_retornar_taxa_fixa_para_distancia_ate_tres_km():
    distancia_km = 3

    resultado = calcular_taxa_entrega(distancia_km)

    assert resultado == 5.00


def test_deve_calcular_taxa_proporcional_para_distancia_maior_que_tres_km():
    distancia_km = 5

    resultado = calcular_taxa_entrega(distancia_km)

    assert resultado == 9.00


def test_deve_gerar_erro_quando_distancia_for_negativa():
    distancia_km = -2

    with pytest.raises(ValueError, match="Distância inválida"):
        calcular_taxa_entrega(distancia_km)
