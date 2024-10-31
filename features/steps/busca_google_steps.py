import csv
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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

@then('o usuário deve coletar títulos e links de artigos em múltiplas páginas e salvar no arquivo CSV')
def step_collect_articles_and_save_to_csv(context):
    articles = []

    # Limite de páginas para evitar sobrecarga de coleta
    page_limit = 5  
    current_page = 1

    while current_page <= page_limit:
        # Coleta todos os artigos na página atual
        results = context.driver.find_elements(By.CSS_SELECTOR, 'h3.gs_rt a')
        for result in results:
            title = result.text
            link = result.get_attribute("href")
            if title and link:
                articles.append({"Título": title, "Link": link})

        # Verifica se existe um botão "Próxima" para ir à próxima página
        try:
            next_button = WebDriverWait(context.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Próxima"))
            )
            next_button.click()
            time.sleep(2)
            current_page += 1
        except:
            # Sai do loop se não houver próxima página
            break

    # Salva os artigos em um arquivo CSV
    with open("artigos_google_academico.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Título", "Link"])
        writer.writeheader()
        writer.writerows(articles)

    # Exibe o número total de artigos coletados
    print(f"Total de artigos coletados: {len(articles)}")
