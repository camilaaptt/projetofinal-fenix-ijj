from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("que eu acesse o site do Instituto Joga Junto")
def go_to_page(context):
    context.browser.get("https://projetofinal.jogajuntoinstituto.org/")

@when("eu preencher os dados no formulario de login")
def form_text(context):
    context.browser.find_element(By.NAME, "email").send_keys("squadfenix@qa-ijj.com.br")
    context.browser.find_element(By.NAME, "password").send_keys("fenix06")
    btn = context.browser.find_element(By.XPATH, "/html/body/div[1]/main/form/button")
    btn.submit()

@then("devo visualizar a mensagem 'logado com sucesso'")
def verify_message(context):
    message = "logado com sucesso"
    try:
        WebDriverWait(context.browser, 3).until(EC.text_to_be_present_in_element((By.XPATH, "//*"), message))
        assert True
    except AssertionError:
        assert False