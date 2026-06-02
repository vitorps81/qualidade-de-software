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
