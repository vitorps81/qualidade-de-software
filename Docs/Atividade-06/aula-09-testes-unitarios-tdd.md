# Aula 9 – Testes Unitários e TDD

**Disciplina:** Qualidade de Software
**Projeto:** LocalEats

---

## Integrante

* Vítor Saraiva de Souza

---

## 1. Funcionalidade Escolhida

### Funcionalidade

**Cálculo do Total do Pedido com Valor Mínimo**

### Descrição

Essa funcionalidade é responsável por somar os valores dos itens adicionados ao pedido e verificar se o valor mínimo exigido pelo restaurante foi atingido.

### Importância

Essa é uma regra central do fluxo de compra, pois impede que pedidos sejam realizados abaixo do valor mínimo definido pelo estabelecimento.

### Regras de Negócio

* O total do pedido corresponde à soma dos preços dos itens.
* O pedido deve atingir o valor mínimo estabelecido.
* Caso o valor mínimo não seja atingido, deve ser gerado um erro.

### Arquivos

| Arquivo              | Finalidade                         |
| -------------------- | ---------------------------------- |
| src/pedido.py        | Implementação da regra de negócio  |
| tests/test_pedido.py | Testes unitários da funcionalidade |

---

## 2. Testes Unitários

### Teste 1 – Pedido com valor acima do mínimo

#### Cenário Testado

Validar se a função calcula corretamente o total do pedido quando a soma dos itens é superior ao valor mínimo exigido.

#### Dados de Entrada

```python
itens = [{"preco": 10}, {"preco": 20}]
valor_minimo = 15
```

#### Resultado Esperado

* Retornar 30
* Não gerar erro

#### Código do Teste

```python
def test_deve_calcular_total_quando_valor_minimo_atingido():
    itens = [{"preco": 10}, {"preco": 20}]
    valor_minimo = 15

    resultado = calcular_total_pedido(itens, valor_minimo)

    assert resultado == 30
```

#### Resultado Obtido

Teste aprovado

---

### Teste 2 – Pedido com valor igual ao mínimo

#### Cenário Testado

Validar se a função aceita pedidos cujo valor total seja exatamente igual ao valor mínimo.

#### Dados de Entrada

```python
itens = [{"preco": 10}, {"preco": 5}]
valor_minimo = 15
```

#### Resultado Esperado

* Retornar 15
* Não gerar erro

#### Código do Teste

```python
def test_deve_calcular_total_quando_total_igual_ao_valor_minimo():
    itens = [{"preco": 10}, {"preco": 5}]
    valor_minimo = 15

    resultado = calcular_total_pedido(itens, valor_minimo)

    assert resultado == 15
```

#### Resultado Obtido

Teste aprovado

---

### Teste 3 – Pedido abaixo do valor mínimo

#### Cenário Testado

Validar se a função gera erro quando o pedido não atinge o valor mínimo exigido.

#### Dados de Entrada

```python
itens = [{"preco": 5}, {"preco": 4}]
valor_minimo = 15
```

#### Resultado Esperado

Gerar exceção:

```python
ValueError
```

#### Código do Teste

```python
def test_deve_gerar_erro_quando_valor_minimo_nao_for_atingido():
    itens = [{"preco": 5}, {"preco": 4}]
    valor_minimo = 15

    with pytest.raises(ValueError):
        calcular_total_pedido(itens, valor_minimo)
```

#### Resultado Obtido

Teste aprovado

---

## 3. Aplicação do TDD

### 🔴 Red

Primeiramente foi criado o teste antes da implementação da funcionalidade.

```python
def test_deve_calcular_total_quando_valor_minimo_atingido():
    ...
```

Resultado inicial:

```text
FAILED
NameError: calcular_total_pedido is not defined
```

O teste falhou porque a função ainda não existia.

---

### 🟢 Green

Foi criada uma implementação mínima para que o teste passasse.

```python
def calcular_total_pedido(itens, valor_minimo):
    return 30
```

Após essa implementação, o teste passou.

---

### 🔵 Refactor

O código foi refatorado para atender corretamente às regras de negócio.

```python
def calcular_total_pedido(itens, valor_minimo):
    total = sum(item["preco"] for item in itens)

    if total < valor_minimo:
        raise ValueError("Valor mínimo do pedido não atingido")

    return total
```

A lógica ficou mais flexível, reutilizável e adequada para diferentes cenários.

---

## 4. Refatoração

### Melhorias Realizadas

* Utilização de nomes claros para função e variáveis.
* Implementação da soma dinâmica dos itens.
* Inclusão de validação para valor mínimo.
* Tratamento explícito de erros utilizando exceções.
* Código mais simples e legível.

### Benefícios

* Facilidade de manutenção.
* Melhor entendimento da regra de negócio.
* Maior confiabilidade da funcionalidade.

---

## 5. Execução dos Testes

### Comando Executado

```bash
pytest
```

### Resultado

```text
======================== test session starts ========================

collected 3 items

tests/test_pedido.py ... [100%]

======================== 3 passed ========================
```

### Resumo

| Métrica          | Quantidade |
| ---------------- | ---------- |
| Total de testes  | 3          |
| Testes aprovados | 3          |
| Testes falharam  | 0          |

### Evidência

Print da execução armazenado em:

```text
artefatos/evidencias/aula-09-testes-unitarios-tdd/
```

---

## 6. Reflexão

### Foi difícil escrever testes antes do código?

Inicialmente sim, pois exige uma mudança de pensamento. Foi necessário focar primeiro no comportamento esperado da funcionalidade antes da implementação.

### O TDD ajudou no desenvolvimento?

Sim. O TDD auxiliou na definição clara dos requisitos e permitiu desenvolver a funcionalidade com mais segurança.

### Os testes aumentaram a confiança no código?

Sim. Os testes automatizados permitem verificar rapidamente se alterações futuras causaram regressões.

### O que melhorariam?

Seriam adicionados mais cenários de teste, incluindo listas vazias, valores negativos e diferentes limites de pedido.

### Como isso ajuda no projeto do grupo?

Os testes automatizados garantem maior qualidade e estabilidade do sistema LocalEats, permitindo evoluir novas funcionalidades com menor risco de falhas.

---

## 7. Conclusão

A utilização de testes unitários e da metodologia TDD permitiu validar a regra de negócio escolhida de forma automatizada, aumentando a qualidade do código e reduzindo riscos de erros futuros.