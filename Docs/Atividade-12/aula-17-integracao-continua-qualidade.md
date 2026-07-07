# Aula 17 – Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos

**Disciplina:** Qualidade de Software  
**Projeto:** LocalEats

---

## 👤 Integrante

- Vítor Saraiva de Souza

---

# 1. Repositório da Atividade

| Item | Descrição |
|--------|--------|
| Nome do repositório | localeats-ci-laboratorio |
| Link do repositório | https://github.com/vitorps81/localeats-ci-laboratorio |

### Estrutura de Diretórios

```text
localeats-ci-laboratorio/
├── .github/
│   └── workflows/
│       └── quality.yml
├── src/
│   ├── __init__.py
│   └── pedido.py
├── tests/
│   └── test_pedido.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 2. Planejamento da Funcionalidade

| Item | Descrição |
|--------|--------|
| Título da Issue | Implementar Validação do Valor Mínimo do Pedido |
| Objetivo da funcionalidade | Validar se o valor total do pedido atende ao valor mínimo exigido antes da finalização da compra. |
| Link da Issue | https://github.com/vitorps81/localeats-ci-laboratorio/issues/1 |

---

# 3. Teste Automatizado

| Item | Descrição |
|--------|--------|
| Tipo de teste | Unitário |
| Objetivo do teste | Validar o cálculo do total do pedido e verificar se a regra do valor mínimo é aplicada corretamente. |
| Link para o arquivo do teste | https://github.com/vitorps81/localeats-ci-laboratorio/blob/master/tests/test_pedido.py |

### Código do teste

```python
import pytest
from src.pedido import calcular_total_pedido


def test_deve_calcular_total_quando_valor_minimo_atingido():
    itens = [{"preco": 10}, {"preco": 20}]
    valor_minimo = 15

    resultado = calcular_total_pedido(itens, valor_minimo)

    assert resultado == 30


def test_deve_calcular_total_quando_total_igual_ao_valor_minimo():
    itens = [{"preco": 10}, {"preco": 5}]
    valor_minimo = 15

    resultado = calcular_total_pedido(itens, valor_minimo)

    assert resultado == 15


def test_deve_gerar_erro_quando_valor_minimo_nao_for_atingido():
    itens = [{"preco": 5}, {"preco": 4}]
    valor_minimo = 15

    with pytest.raises(ValueError, match="Valor mínimo do pedido não atingido"):
        calcular_total_pedido(itens, valor_minimo)
```

---

# 4. Pipeline de Integração Contínua

| Item | Descrição |
|--------|--------|
| Nome do workflow | Quality Pipeline |
| Evento que dispara a execução | Push e Pull Request nas branches **main** e **master** |
| Link para o workflow | https://github.com/vitorps81/localeats-ci-laboratorio/blob/master/.github/workflows/quality.yml |
| Link da execução | https://github.com/vitorps81/localeats-ci-laboratorio/actions |

### Código do workflow

```yaml
name: Quality Pipeline

on:
  push:
    branches:
      - main
      - master

  pull_request:
    branches:
      - main
      - master

jobs:
  tests:
    runs-on: ubuntu-latest

    steps:
      - name: Baixar o código
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.13"

      - name: Instalar dependências
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Executar testes
        run: |
          pytest -v
```

---

# 5. Indicadores de Qualidade

| Indicador | Valor |
|------------|--------|
| Quantidade de testes executados | 3 |
| Quantidade de testes aprovados | 3 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline | Sucesso |

---

# 6. Registro de Defeito

| Item | Descrição |
|--------|--------|
| Título do defeito | Erro na Validação do Valor Mínimo do Pedido |
| Severidade | Média |
| Link da Issue | https://github.com/vitorps81/localeats-ci-laboratorio/issues/2 |

### Descrição do defeito

Foi identificado que pedidos abaixo do valor mínimo poderiam ser aceitos pelo sistema.

O problema foi identificado durante a execução dos testes unitários automatizados.

A correção consistiu em adicionar uma validação na função `calcular_total_pedido()` para lançar uma exceção (`ValueError`) quando o valor mínimo do pedido não fosse atingido.

---

# 📸 Evidências

As evidências desta atividade foram registradas por meio de:

- Execução dos testes automatizados no ambiente local (`3 passed`).
- Execução do pipeline **Quality Pipeline** no GitHub Actions com status de sucesso.
- Criação da Issue **#1** para planejamento da funcionalidade.
- Criação da Issue **#2** para registro do defeito.
- Registro das telas do GitHub Actions e das Issues como comprovação da atividade.

---

# ✅ Conclusão

A atividade permitiu compreender como a Integração Contínua (CI) pode contribuir para a qualidade do desenvolvimento de software. A utilização do GitHub Actions automatizou a execução dos testes sempre que alterações foram enviadas ao repositório, reduzindo o risco de introduzir falhas no sistema.

Além disso, o uso de GitHub Issues demonstrou a importância do registro e acompanhamento de funcionalidades e defeitos durante o desenvolvimento. A combinação entre testes automatizados, pipeline de Integração Contínua e gestão de defeitos tornou o processo mais organizado, confiável e alinhado às boas práticas de qualidade de software.