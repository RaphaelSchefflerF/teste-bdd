from selenium import webdriver

def before_all(context):
    # Inicializando o navegador antes de todos os cenários
    context.driver = webdriver.Chrome()  # Garante que o ChromeDriver está instalado e acessível

def after_all(context):
    # Fecha o navegador após todos os testes
    context.driver.quit()
