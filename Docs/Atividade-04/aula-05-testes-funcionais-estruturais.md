# Aula 5 – Testes Funcionais vs Estruturais  
## LocalEats

---

## 👥 Integrantes
- [Vítor Saraiva de Souza]

---

## 🎯 1. Funcionalidade escolhida

**Funcionalidade:** Busca de restaurantes  

**Descrição da funcionalidade:**  
Permite que o usuário busque restaurantes com base em filtros como tipo de culinária, localização e faixa de preço.

**O que o usuário espera:**  
O usuário espera encontrar resultados corretos, rápidos e relevantes de acordo com os filtros aplicados.

---

## 🔍 2. Testes Caixa-Preta (Visão do Usuário)

Quais testes você faria sem conhecer o código?

### 🔹 Cenários de teste

**Cenário 1:** Buscar por tipo de culinária   
→ Deve retornar restaurantes que realmente oferecem pizza  

**Cenário 2:** Buscar por localização  
→ Deve retornar restaurantes próximos corretamente  

**Cenário 3:** Buscar com múltiplos filtros   
→ Deve combinar corretamente os critérios  

**Cenário 4:** Buscar com campo vazio ou inválido  
→ Sistema deve tratar erro ou retornar mensagem adequada  

---

### 🔹 Possíveis erros identificados

- Resultados incorretos   
- Resultados vazios mesmo com dados disponíveis  
- Filtros ignorados ou aplicados incorretamente  
- Lentidão na resposta  
- Interface confusa ao exibir resultados  

---

## 🔧 3. Testes Caixa-Branca (Visão do Sistema)

Como essa funcionalidade poderia ser implementada internamente?

### 🔹 Lógica hipotética (pseudo-código ou descrição)

```
if (filtro_culinaria != vazio) {
filtrar_por_culinaria();
}

if (filtro_localizacao != vazio) {
filtrar_por_localizacao();
}

if (filtro_preco != vazio) {
filtrar_por_preco();
}

ordenar_resultados();
retornar_lista();
```

---

### 🔹 Situações a serem testadas

**Situação 1:** Filtros aplicados individualmente  
→ Verificar se cada filtro funciona isoladamente  

**Situação 2:** Combinação de filtros  
→ Verificar se a lógica de combinação está correta  

**Situação 3:** Nenhum filtro aplicado  
→ Sistema deve retornar lista padrão  

---

### 🔹 Possíveis erros identificados

- Condições lógicas incorretas   
- Falha na consulta ao banco de dados  
- Erros ao combinar filtros  
- Problemas de performance na consulta  
- Dados inconsistentes retornados  

---

## ⚖️ 4. Comparação entre as abordagens

**Qual a principal diferença entre testar sem ver o código e com acesso ao código?**

A principal diferença é que o teste caixa-preta avalia o comportamento externo do sistema, enquanto o teste caixa-branca analisa a lógica interna e a implementação.

---

**Que tipo de problema cada abordagem ajuda a encontrar?**

**Caixa-preta:**  
Problemas visíveis ao usuário, como resultados incorretos, erros de interface e falhas de funcionalidade.

**Caixa-branca:**  
Problemas internos, como erros de lógica, falhas em condições, problemas de código e inconsistências na implementação.

---

## 💡 5. Reflexão no contexto do LocalEats

**Qual abordagem parece mais importante neste momento do projeto?**

A abordagem de caixa-preta é mais importante neste momento, pois os principais problemas relatados estão relacionados à experiência do usuário, como resultados incorretos e comportamentos inesperados.

---

**Apenas uma abordagem seria suficiente? Por quê?**

Não. Apenas uma abordagem não é suficiente, pois a caixa-preta identifica os problemas visíveis, mas a caixa-branca é necessária para entender e corrigir a causa desses problemas no código.

---

## 🚀 Conclusão

A atividade demonstrou a importância de utilizar diferentes abordagens de teste para garantir a qualidade do software. Foi possível compreender que testes caixa-preta e caixa-branca são complementares, sendo essenciais tanto para identificar falhas visíveis quanto para corrigir problemas internos do sistema.
