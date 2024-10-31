from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

@given('que o usuário está na página inicial do Google')
def step_user_on_google_homepage(context):
    context.driver.get('https://www.google.com')
    time.sleep(2)

@when('o usuário buscar por "Google Acadêmico"')
def step_user_searches_google_academic(context):
    search_box = context.driver.find_element(By.NAME, 'q')
    search_box.send_keys("Google Acadêmico")
    search_box.send_keys(Keys.RETURN)
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Google Acadêmico')]"))
    )

@when('o usuário abre o Google Acadêmico nos resultados')
def step_user_opens_google_academic(context):
    link = context.driver.find_element(By.XPATH, "//h3[contains(text(), 'Google Acadêmico')]")
    link.click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'q'))
    )
    time.sleep(2)

@when('o usuário buscar por "{query}" no Google Acadêmico')
def step_user_searches_in_google_academic(context, query):
    search_box = context.driver.find_element(By.NAME, 'q')
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

@then('a quantidade de resultados para "{query}" deve ser salva em um arquivo CSV')
def step_save_number_of_results_to_csv(context, query):
    results_info = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'gs_ab_md'))
    )
    result_text = results_info.text

    # Extrai o número de resultados do texto
    quantidade_resultados = result_text.split()[1]

    # Escreve no arquivo CSV
    with open("resultados_google_academico.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Busca", "Quantidade de Resultados"])
        writer.writerow([query, quantidade_resultados])

    print(f"Resultados para '{query}': {quantidade_resultados}")

import csv

@then('o usuário deve abrir o último resultado acessível para "{query}" e salvar no arquivo')
def step_open_and_save_last_accessible_result(context, query):
    # Continua clicando em "Próxima" até a última página acessível
    while True:
        try:
            next_button = WebDriverWait(context.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Próxima"))
            )
            next_button.click()
            time.sleep(2)  # Tempo para carregar a próxima página
        except:
            # Se o botão "Próxima" não estiver mais presente, estamos na última página
            break

    # Encontra o último item na última página acessível
    results = context.driver.find_elements(By.CSS_SELECTOR, 'h3.gs_rt a')
    if results:
        last_result = results[-1]
        last_title = last_result.text
        last_link = last_result.get_attribute("href")
        print(f"Abrindo e salvando o último artigo acessível para '{query}':", last_title, last_link)
        
        # Clica no último resultado
        last_result.click()

        # Salva o nome e o link do último resultado no arquivo CSV
        with open("resultados_google_academico.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Busca", "Último Resultado Acessível", "Link"])
            writer.writerow([query, last_title, last_link])
    else:
        print("Nenhum resultado encontrado.")
