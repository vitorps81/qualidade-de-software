# Aula 6 – Planejamento e Execução de Testes  
**Disciplina:** Qualidade de Software  
**Projeto:** LocalEats  

---

## Integrante

- [Vítor Saraiva de Souza]

---

## 1. Plano de Testes

### 1.1 Objetivo

Validar as principais funcionalidades do sistema LocalEats, garantindo que atendam aos requisitos esperados e apresentem comportamento consistente, especialmente nas áreas onde já foram identificados problemas, como busca de restaurantes e finalização de pedidos.

**Exemplo:**  
Validar as principais funcionalidades do sistema LocalEats, garantindo que atendam aos requisitos esperados e apresentem comportamento consistente.

---

### 1.2 Escopo

**O que será testado:**
- Login  
- Busca de restaurantes  
- Finalização de pedidos  
- Avaliações  

**O que não será testado:**
- Integrações externas (ex: sistemas de pagamento)  
- Funcionalidades administrativas  

---

### 1.3 Funcionalidades selecionadas

Lista das funcionalidades que serão foco dos testes:

- Login  
- Busca de restaurantes  
- Pedido  
- Avaliação 

---

### 1.4 Estratégia de Testes

Descreva como os testes serão realizados.

**Tipos de teste:**
- Testes funcionais  

**Abordagem:**  
Testes manuais baseados em cenários simples.

---

### 1.5 Responsáveis

| Nome | Responsabilidade |
|------|------------------|
| Vítor Saraiva de Souza | Planejamento, execução e análise dos testes |

---

## 2. Casos de Teste

### CT-01 – Login com sucesso

**Pré-condição:** Usuário cadastrado  

**Passos:**
1. Acessar login  
2. Inserir dados válidos  
3. Clicar em entrar  

**Resultado esperado:** Login realizado  

---

### CT-02 – Login com erro

**Pré-condição:** Usuário cadastrado  

**Passos:**
1. Inserir senha errada  
2. Clicar em entrar  

**Resultado esperado:** Exibir erro  

---

### CT-03 – Busca de restaurante

**Pré-condição:** Usuário logado  

**Passos:**
1. Buscar restaurante  
2. Ver resultados  

**Resultado esperado:** Mostrar resultados  

---

### CT-04 – Finalizar pedido

**Pré-condição:** Produto no carrinho  

**Passos:**
1. Finalizar pedido  

**Resultado esperado:** Pedido concluído  

---

### CT-05 – Avaliar restaurante

**Pré-condição:** Usuário logado  

**Passos:**
1. Inserir avaliação  

**Resultado esperado:** Avaliação salva   

---

## 3. Execução dos Testes

Preencha a tabela com os resultados obtidos.

| Caso de Teste | Resultado | Evidência |
|---------------|----------|-----------|
| CT-01 | Passou | Login realizado corretamente |
| CT-02 | Passou | Mensagem de erro exibida |
| CT-03 | Falhou | Resultados incorretos na busca |
| CT-04 | Falhou | Erro ao finalizar pedido |
| CT-05 | Falhou | Avaliação não persistiu |

---

## 4. Análise dos Resultados

**Testes executados:** 5  
**Passaram:** 2  
**Falharam:** 3  

**Problemas encontrados:**
- Busca com erro  
- Falha no pedido  
- Problema na avaliação

---

## 5. Reflexão

**O plano de testes ajudou a organizar melhor os testes? Por quê?**  
Sim, o plano de testes ajudou a estruturar o processo, permitindo uma execução mais organizada e focada nos principais problemas do sistema.

---

**Algum problema só foi percebido durante a execução?**  
Sim, o erro na finalização de pedidos ficou mais evidente durante a execução, demonstrando falhas críticas que impactam diretamente o uso da plataforma.

---

**O que melhoraria no processo de testes?**  
Melhoraria a cobertura de testes, incluindo mais cenários de erro, além de testes automatizados e testes de desempenho.

---

## Conclusão

As funcionalidades testadas não apresentaram comportamento totalmente aceitável, pois foram identificadas falhas críticas na busca de restaurantes, na finalização de pedidos e na persistência de avaliações. Esses problemas impactam diretamente a experiência do usuário e o uso do sistema.

---

## 6. Conclusão Geral

**Resumo final:**

- **Qualidade geral do sistema:** Média, com falhas relevantes  
- **Pontos positivos:** Login funcional e tratamento básico de erros  
- **Principais problemas identificados:** Busca incorreta, falhas em pedidos e avaliações  
- **Impressão geral:** O sistema ainda precisa de melhorias antes de ser considerado estável e confiável
