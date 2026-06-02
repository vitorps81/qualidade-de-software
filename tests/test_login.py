from pages.login_page import LoginPage


def test_login_com_sucesso(page):
    login = LoginPage(page)

    login.acessar()

    login.realizar_login(
        "teste@teste.com",
        "123456"
    )

    assert page.url is not None
