import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


def parse_form(driver):
    # "Fase da Despesa"
    driver.find_element(
        By.XPATH, '//*[@id="form"]/div[4]/span[3]/input'
    ).click()  # span[i], 1: Empenho, 2: Liquidação, 3: Pagamento

    # Ano
    year_selector = Select(driver.find_element(By.XPATH, '//*[@id="ano"]'))
    year_selector.select_by_index(1)

    # Município
    city_selector = Select(driver.find_element(By.XPATH, '//*[@id="municipio"]'))
    city_selector.select_by_index(1)

    # Entidade
    time.sleep(3)
    entity_selector = Select(driver.find_element(By.XPATH, '//*[@id="entidade"]'))
    entity_selector.select_by_index(1)
    # len(entity_selector.options)

    # TO DO: loop through all options

    # Submit "Pesquisar"
    driver.find_element(By.XPATH, '//*[@id="form"]/div[13]/input[8]').click()
    return parse_response(driver)


def parse_response(driver):
    expense_list = []
    document_element_list = driver.find_elements(By.TAG_NAME, "tr")
    for i in range(1, len(document_element_list) - 1):
        time.sleep(3)
        document_element_list = driver.find_elements(By.TAG_NAME, "tr")  # reload list
        document_element = document_element_list[i]
        expense = parse_document(driver, document_element)
        expense_list.append(expense)
    return expense_list


def parse_document(driver, document_element):
    document_element.find_element(By.XPATH, "./td").click()

    time.sleep(5)
    expense_fields = driver.find_elements(By.CSS_SELECTOR, ".content .form-group")
    expense = parse_expense(expense_fields)
    try:
        driver.find_element(By.ID, "btn-voltar").click()
    except:
        driver.find_element(By.ID, "btn-voltar ").click()

    return expense


def parse_expense(expense_fields):
    valid_fields = expense_fields[3:-5]
    expense = {}
    for field in valid_fields:
        text = field.text
        splits = text.split(":")

        if len(splits) > 1:
            field_name = splits[0]
            field_value = splits[1]
            expense[field_name.strip()] = field_value.strip()

    print(expense)
    return expense


service = webdriver.ChromeService(executable_path="/home/vlg/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.tcm.ba.gov.br/controle-social/consulta-de-despesas/")

timeout = 5
WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, "form")))

result = parse_form(driver)
df = pd.DataFrame(result)
df.to_csv("expenses.csv", index=False)