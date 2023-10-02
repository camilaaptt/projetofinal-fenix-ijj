from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


@given("que eu acesse o site de cadastro no e-commerce do Instituto Joga Junto")
def go_to_page(context):
    context.browser.get("https://projetofinal.jogajuntoinstituto.org/register")

@when("eu preencher os dados no formulario de cadastro")
def form_text(context):
    faker = Faker('pt-br')
    email = faker.email()
    password = faker.password()

    context.browser.find_element(By.NAME, "email").send_keys(email)
    context.browser.find_element(By.NAME, "password").send_keys(password)
    context.browser.find_element(By.NAME, "confirmPassword").send_keys(password)
    btn = context.browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/form/button")
    btn.submit()

@then("devo visualizar a mensagem 'Usuário cadastrado com sucesso'")
def verify_message(context):
    message = "Usuário cadastrado com sucesso"
    try:
        WebDriverWait(context.browser, 3).until(EC.text_to_be_present_in_element((By.XPATH, "//*"), message))
        assert True
    except AssertionError:
        assert False


   


