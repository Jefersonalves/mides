import logging

import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_city_entities(ibge_code):
    url = f"https://webservice.tcm.ba.gov.br/despesas/entidade?muni={ibge_code}"
    response = requests.get(
        url, verify=False, headers={"Origin": "https://www.tcm.ba.gov.br"}
    )
    entity_list = response.json()
    entity_codes = [entity["cd_Unidade"] for entity in entity_list]
    return entity_codes


def get_all_entities():
    # TO DO: loop through available cities
    city_codes = [2900108, 2900207]
    entity_codes = []
    for code in city_codes:
        entity_codes.extend(get_city_entities(code))
    return entity_codes


def parse_table(response):
    # pd.read_html(r.content), doesn't work
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table")
    lines = table.find_all("tr")

    header = lines[2]
    header_cells = header.find_all("th")
    header_cells_text = [cell.text.strip() for cell in header_cells]

    expenses = []
    for line in lines[3:]:
        cells = line.find_all("td")
        cells_text = [cell.text.strip() for cell in cells]
        expenses.append(cells_text)

    df = pd.DataFrame(expenses, columns=header_cells_text)
    return df


def extract_expenses():
    df_list = []
    entity_codes = get_all_entities()
    for code in entity_codes:
        url = (
            "https://webservice.tcm.ba.gov.br/exportar/despesa?tipo=pdf"
            f"&entidade={code}"
            "&orgao="
            "&orcamentaria="
            "&elemento="
            "&recurso="
            "&dataInicio="
            "&dataFinal="
            "&despesa=P"
            "&favorecido="
            "&ano=2023"
        )
        try:
            response = requests.get(
                url, verify=False, headers={"Origin": "https://www.tcm.ba.gov.br"}
            )
            df = parse_table(response)
            df["Código Entidade"] = code
            df_list.append(df)
        except:
            logging.error(f"Error at url {url}")
            continue

    return pd.concat(df_list)


result = extract_expenses()
result.to_csv("expenses.csv", index=False)
