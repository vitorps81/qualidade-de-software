Feature: Navegação entre páginas

  Scenario: Acessar a página inicial
    Given que o usuário acessa o LocalEats
    When a página for carregada
    Then o sistema deve exibir a interface principal

  Scenario: Navegar para uma página do sistema
    Given que o usuário acessa o LocalEats
    When selecionar uma opção de navegação
    Then a página correspondente deve ser exibida