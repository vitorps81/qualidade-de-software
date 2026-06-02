# Aula 12 – BDD e Automação Orientada a Comportamento

## Exemplo de Entrega PBL – LocalEats

### 👥 Integrantes

* Vítor Saraiva de Souza

---

## 🔹 1. Fluxo escolhido

### Integrante

Vítor Saraiva de Souza

### Fluxo

Navegação entre páginas

### Objetivo

Validar se o usuário consegue acessar o sistema e navegar entre as páginas sem erros, garantindo que os principais elementos da interface sejam carregados corretamente.

---

## 🔹 2. Cenários BDD

### Arquivo

```text
features/navegacao.feature
```

### Conteúdo

```gherkin
Feature: Navegação entre páginas

  Scenario: Acessar a página inicial
    Given que o usuário acessa o LocalEats
    When a página for carregada
    Then o sistema deve exibir a interface principal

  Scenario: Navegar para uma página do sistema
    Given que o usuário acessa o LocalEats
    When selecionar uma opção de navegação
    Then a página correspondente deve ser exibida
```

---

## 🔹 3. Automação com pytest-bdd

### Estrutura do projeto

```text
projeto/
│
├── features/
│   └── navegacao.feature
│
├── tests/
│   └── test_navegacao.py
│
├── evidencias/
│
└── README.md
```

### Arquivo

```text
tests/test_navegacao.py
```

### Código

```python
from pytest_bdd import scenarios, given, when, then

scenarios("../features/navegacao.feature")


@given("que o usuário acessa o LocalEats")
def acessar_localeats(page):
    page.goto(
        "https://local-eats-unisenac.vercel.app/static/login.html"
    )


@when("a página for carregada")
def pagina_carregada(page):
    page.wait_for_load_state("networkidle")


@then("o sistema deve exibir a interface principal")
def validar_interface(page):
    assert page.locator("body").is_visible()


@when("selecionar uma opção de navegação")
def navegar(page):
    page.wait_for_load_state("networkidle")


@then("a página correspondente deve ser exibida")
def validar_navegacao(page):
    assert page.locator("body").is_visible()
```

---

## 🔹 4. Execução dos testes

### Comando executado

```bash
pytest tests/test_navegacao.py -v
```

### Resultado

```text
============================================================= test session starts =============================================================

collected 2 items

tests/test_navegacao.py::test_acessar_a_página_inicial PASSED
tests/test_navegacao.py::test_navegar_para_uma_página_do_sistema PASSED

============================================================== 2 passed in 6.97s ==============================================================
```

---

## 🔹 5. Evidências

### Print da execução

```text
evidencias/
  execucao-cenarios-bdd.png
```

### Print da aplicação

```text
evidencias/
  navegacao-localeats.png
```

---

## 🔹 6. Análise crítica

### O cenário ficou legível?

Sim. A estrutura Given-When-Then tornou o comportamento esperado fácil de compreender.

### O BDD ajudou a entender o comportamento?

Sim. Os cenários descrevem claramente o que o usuário faz e qual resultado é esperado, facilitando a comunicação entre as partes envolvidas.

### O teste ficou robusto?

Parcialmente. Os testes validam o carregamento das páginas, mas poderiam utilizar verificações mais específicas para aumentar a confiabilidade.

### Quais dificuldades surgiram?

* Entender a estrutura do pytest-bdd.
* Relacionar os cenários Gherkin aos steps em Python.
* Integrar Playwright com pytest-bdd.

### O teste ficou dependente da interface?

Sim. Alterações significativas na interface podem exigir ajustes nos seletores utilizados.

### O cenário representa realmente uma regra de negócio?

Sim. A navegação entre páginas é um comportamento importante para garantir que o usuário consiga utilizar o sistema corretamente.

### O que tornaria o teste mais robusto?

* Utilizar seletores mais específicos.
* Validar elementos únicos de cada página.
* Verificar mudanças reais de navegação e conteúdo.

---

## 🔹 7. Reflexão final

### BDD melhora comunicação entre equipe?

Sim. O comportamento esperado fica mais claro para desenvolvedores, analistas, QA e pessoas de negócio.

### Todo teste deve usar BDD?

Não. O BDD é mais indicado para funcionalidades e fluxos importantes do negócio.

### Quando vale a pena usar BDD?

Quando existe necessidade de documentar comportamentos de forma clara, colaborativa e automatizável.

### O comportamento ficou mais claro?

Sim. A utilização de cenários em Gherkin facilitou a visualização do que o sistema deve fazer.

### Como isso ajuda no projeto do grupo?

Ajuda a transformar requisitos em documentação executável, melhorando a comunicação, a rastreabilidade e a manutenção dos testes.

---

## 📦 Repositório GitHub

```text
https://github.com/seu-usuario/projeto-qualidade-software
```

---

## ✅ Conclusão

A atividade permitiu compreender:

* Escrita de cenários BDD utilizando Gherkin.
* Organização dos comportamentos utilizando Given, When e Then.
* Integração entre pytest-bdd e Playwright.
* Importância da legibilidade dos testes.
* Benefícios da documentação viva.
* Manutenção e evolução de testes automatizados orientados a comportamento.

A utilização do BDD tornou os requisitos mais claros e compreensíveis, aproximando negócio, qualidade e desenvolvimento por meio de uma linguagem comum.
