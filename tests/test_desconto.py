import pytest
from src.desconto import aplicar_desconto


def test_deve_aplicar_desconto_percentual_valido():
    valor_total = 100
    percentual = 10

    resultado = aplicar_desconto(valor_total, percentual)

    assert resultado == 90


def test_deve_retornar_mesmo_valor_quando_desconto_for_zero():
    valor_total = 80
    percentual = 0

    resultado = aplicar_desconto(valor_total, percentual)

    assert resultado == 80


def test_deve_gerar_erro_quando_percentual_for_maior_que_cem():
    valor_total = 100
    percentual = 120

    with pytest.raises(ValueError, match="Percentual de desconto inválido"):
        aplicar_desconto(valor_total, percentual)
