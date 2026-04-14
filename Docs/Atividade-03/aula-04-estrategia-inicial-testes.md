# Estratégia Inicial de Testes – LocalEats

---

## 1. Funcionalidades

- Login  
- Busca de restaurantes  
- Visualização de cardápio e avaliações  
- Finalização de pedidos  
- Favoritos  
- Recomendações personalizadas  

---

## 2. Níveis de Teste

### Funcionalidade: Login
- **Unitário:** validação de campos obrigatórios e autenticação  
- **Integração:** comunicação com banco de dados e serviço de autenticação  
- **Sistema:** fluxo completo de login do usuário  
- **Aceitação:** usuário acessa a plataforma com sucesso  

---

### Funcionalidade: Busca de restaurantes
- **Unitário:** filtros por categoria, localização e preço  
- **Integração:** integração com banco de dados de restaurantes  
- **Sistema:** usuário realiza busca e visualiza resultados  
- **Aceitação:** usuário encontra restaurantes corretos conforme filtros  

---

### Funcionalidade: Visualização de cardápio e avaliações
- **Unitário:** carregamento de dados de cardápio e avaliações  
- **Integração:** conexão com banco de dados e API de avaliações  
- **Sistema:** usuário acessa página do restaurante  
- **Aceitação:** usuário visualiza corretamente informações e avaliações  

---

### Funcionalidade: Finalização de pedidos
- **Unitário:** validação de dados do pedido e pagamento  
- **Integração:** integração com sistema de pagamento e pedidos  
- **Sistema:** fluxo completo de pedido até confirmação  
- **Aceitação:** usuário conclui pedido sem erros  

---

### Funcionalidade: Favoritos
- **Unitário:** adicionar e remover favoritos  
- **Integração:** persistência de dados no banco  
- **Sistema:** usuário gerencia lista de favoritos  
- **Aceitação:** favoritos são salvos e exibidos corretamente  

---

### Funcionalidade: Recomendações personalizadas
- **Unitário:** lógica de recomendação baseada em preferências  
- **Integração:** integração com dados do usuário  
- **Sistema:** sistema apresenta recomendações  
- **Aceitação:** usuário recebe sugestões relevantes  

---

## 3. Prioridades e Riscos

### Alta prioridade
- Login → sem login o usuário não utiliza o sistema  
- Finalização de pedidos → impacta diretamente o negócio  
- Busca de restaurantes → funcionalidade principal  

**Justificativa:**  
Falhas nessas funcionalidades impedem o uso da plataforma, geram perda de usuários e prejuízo financeiro para os restaurantes.

---

### Baixa prioridade
- Favoritos → não impede uso  
- Recomendações → funcionalidade complementar  

**Justificativa:**  
Essas funcionalidades melhoram a experiência, mas não impedem o funcionamento principal do sistema.

---

## 4. Pirâmide de Testes

- **Maior foco:** Testes unitários  
- **Médio foco:** Testes de integração  
- **Menor foco:** Testes de sistema e aceitação  

**Justificativa:**  
Testes unitários são mais rápidos e baratos, permitindo identificar erros cedo. Testes de integração garantem comunicação correta entre componentes. Testes de sistema e aceitação são mais caros e lentos, devendo ser usados com menor frequência, focando nos fluxos críticos.

---

## 5. Testes em Produção

- **Uso de:** monitoramento, logs e testes A/B  
- **Aplicar em:** novas funcionalidades e recomendações  

**Justificativa:**  
Testes em produção permitem identificar problemas reais que não aparecem em ambiente de teste, especialmente relacionados a desempenho e comportamento do usuário. Devem ser usados com cautela para não impactar negativamente a experiência.
