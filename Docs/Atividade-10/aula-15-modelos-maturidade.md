# Aula 15 – Modelos de Maturidade

**Disciplina:** Qualidade de Software
**Projeto:** LocalEats

---

## 👤 Integrante

* Vítor Saraiva de Souza

---

# 1. Diagnóstico de Maturidade

| Critério                                                                 | Sim | Parcial | Não |
| ------------------------------------------------------------------------ | :-: | :-----: | :-: |
| Os requisitos são documentados?                                          |  ✅  |         |     |
| Existe controle de mudanças?                                             |     |    ✅    |     |
| Há atividades de teste definidas?                                        |  ✅  |         |     |
| Os defeitos são registrados?                                             |     |    ✅    |     |
| O processo de desenvolvimento é conhecido?                               |  ✅  |         |     |
| As tarefas são planejadas e acompanhadas regularmente?                   |     |    ✅    |     |
| Existe padronização para implementação de funcionalidades?               |  ✅  |         |     |
| Os testes são executados antes da entrega das funcionalidades?           |  ✅  |         |     |
| Há revisão de código ou validação por outro integrante?                  |     |         |  ✅  |
| São utilizadas ferramentas para gerenciamento das atividades?            |     |    ✅    |     |
| Os artefatos do projeto são organizados e versionados?                   |  ✅  |         |     |
| Existe rastreabilidade entre requisitos e funcionalidades implementadas? |     |    ✅    |     |
| Existem momentos para identificar melhorias no processo?                 |     |    ✅    |     |
| Existem indicadores ou métricas para acompanhar a qualidade?             |     |         |  ✅  |

---

## Classificação do Processo

**Nível de maturidade:** **Definido**

### Justificativa

O processo de desenvolvimento adotado apresenta etapas bem definidas, incluindo levantamento dos requisitos, implementação, testes unitários, testes funcionais, aplicação de BDD e documentação das atividades. Além disso, os artefatos do projeto são organizados e versionados durante o desenvolvimento. Entretanto, ainda existem oportunidades de evolução, como adoção de métricas de qualidade, revisão de código por outro desenvolvedor e maior controle das mudanças realizadas ao longo do projeto.

---

# 2. Lacunas Identificadas

| Lacuna                                                      | Impacto                                                                         |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Ausência de métricas para acompanhar a qualidade do projeto | Dificulta medir a evolução do processo e do produto.                            |
| Falta de revisão de código por outro desenvolvedor          | Aumenta a possibilidade de defeitos permanecerem no código.                     |
| Controle de mudanças realizado de forma simples             | Pode dificultar o acompanhamento das alterações realizadas ao longo do projeto. |

---

# 3. Propostas de Melhoria

| Melhoria                                                                                          | Benefício                                                       |
| ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Implantar métricas de qualidade (quantidade de defeitos, cobertura de testes e tempo de correção) | Permite acompanhar a evolução do processo de desenvolvimento.   |
| Adotar revisão de código antes da entrega das funcionalidades                                     | Reduz defeitos e melhora a qualidade do código produzido.       |
| Utilizar ferramentas de Integração Contínua (CI) para execução automática dos testes              | Garante validação contínua e maior confiabilidade nas entregas. |

---

# ✅ Conclusão

A análise realizada demonstrou que o processo utilizado no desenvolvimento do projeto LocalEats apresenta um nível de maturidade **Definido**, pois possui etapas organizadas e práticas de qualidade incorporadas ao desenvolvimento. No entanto, ainda existem oportunidades de melhoria relacionadas ao uso de métricas, revisão de código e automação do processo de integração contínua.

A adoção dessas melhorias contribuirá para tornar o processo mais eficiente, aumentando a qualidade do software produzido e facilitando sua manutenção e evolução.
