# Atividade PBL – Aula 10

# Testes Funcionais Automatizados – LocalEats

## 👥 Integrante(s)

* Vítor Saraiva de Souza

---

## 🔹 1. Fluxo funcional escolhido

### 📌 Fluxo

Login de usuário

### 🔎 Descrição

Permite autenticar um usuário no sistema através do preenchimento de e-mail e senha.

### 🎯 Importância

O login é um fluxo essencial para o acesso às funcionalidades do sistema, garantindo que apenas usuários autenticados possam utilizar determinados recursos.

---

## 🔹 2. Teste com Codegen

### 💻 Comando utilizado

```bash
playwright codegen https://local-eats-unisenac.vercel.app/
```

### 🔗 Link para o código gerado

👉 `tests/codegen_login.py`

### 🧠 Observações

* O Playwright Codegen permitiu gerar rapidamente o fluxo inicial de automação.
* Os comandos de preenchimento dos campos e clique no botão de login foram criados automaticamente.
* O código gerado apresentou alguns comandos desnecessários e pouco reutilizáveis.
* Foi necessária uma refatoração para aplicar boas práticas e melhorar a organização.

---

## 🔹 3. Teste automatizado com Pytest

### 🔗 Link para o teste

👉 `tests/test_login.py`

### 📌 O que o teste faz?

* Acessa a página de login do LocalEats.
* Preenche o campo de e-mail.
* Preenche o campo de senha.
* Clica no botão "Entrar".
* Valida que o fluxo foi executado corretamente.

---

## 🔹 4. Refatoração com Page Object Model (POM)

### 🔗 Link para Page Object

👉 `pages/login_page.py`

### 🔗 Link para teste refatorado

👉 `tests/test_login.py`

### 🧠 Melhorias realizadas

* Separação entre a lógica da interface e o teste automatizado.
* Centralização dos seletores da página.
* Código mais organizado e legível.
* Maior reutilização dos métodos.
* Facilidade de manutenção futura.
* Redução da duplicação de comandos Playwright.

---

## 🔹 5. Execução dos testes

### ▶️ Comando

```bash
pytest tests/test_login.py -v
```

### 📊 Resultado

Total de testes: 1

Testes passaram: 1

Testes falharam: 0

Resultado da execução:

```text
tests/test_login.py::test_login_com_sucesso[chromium] PASSED

1 passed in 7.51s
```

### 📸 Evidência

Print da execução armazenado em:

```text
artefatos/evidencias/aula-10-testes-funcionais/
```

---

## 🔹 6. Análise crítica

Durante o desenvolvimento, o Playwright Codegen facilitou a criação inicial do teste, reduzindo o esforço necessário para identificar seletores e interações da interface.

Apesar disso, o código gerado automaticamente continha trechos pouco reutilizáveis e excessivamente verbosos, exigindo refatoração para aplicação do padrão Page Object Model.

Os seletores gerados funcionaram corretamente, porém seletores baseados em textos visíveis podem se tornar frágeis caso a interface seja modificada futuramente.

O teste apresentou comportamento estável durante a execução e não sofreu falhas durante a validação realizada.

Para torná-lo mais robusto, seria interessante validar explicitamente o resultado do login através de mensagens de sucesso, redirecionamentos ou elementos específicos exibidos após a autenticação.

Os principais riscos de manutenção estão relacionados a mudanças na interface, nomes dos campos ou estrutura dos elementos HTML utilizados pelos seletores.

---

## 🔹 7. Reflexão

Os testes automatizados não substituem completamente os testes manuais, pois determinadas validações relacionadas à experiência do usuário ainda dependem de observação humana.

Nem todos os fluxos precisam ser automatizados. O ideal é priorizar fluxos críticos para o negócio, como login, cadastro, carrinho de compras e finalização de pedidos.

A automação aumenta significativamente a confiança da equipe durante alterações e novas versões do sistema, permitindo identificar problemas rapidamente.

No contexto do LocalEats, os testes funcionais automatizados ajudam a garantir que funcionalidades importantes continuem operando corretamente após modificações no sistema.

---

## 💡 Conclusão

A utilização do Playwright, em conjunto com Pytest e Page Object Model, permitiu automatizar o fluxo de login do sistema LocalEats de forma organizada e reutilizável.

A atividade demonstrou a importância da automação de testes funcionais como complemento aos testes manuais e unitários, contribuindo para aumentar a qualidade, a confiabilidade e a manutenibilidade do software.
