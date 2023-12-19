from pathlib import Path

import scrapy


class TCMBASpider(scrapy.Spider):
    name = "bahia"
    allowed_domains = ["tcm.ba.gov.br"]
    BASE_URL = "https://www.tcm.ba.gov.br"
    start_urls = [
        "https://www.tcm.ba.gov.br/controle-social/consulta-de-despesas/",
    ]

    def parse(self, response):
        params = {
            "consulta": "ano",
            "ano": "2022",
            "dtPeriodo1": "",
            "dtPeriodo2": "",
            "desp": "P",
            "municipio": "2900108+++",
            "entidade": "1",
            "orgao": "",
            "despesa": "",
            "recurso": "",
            "favorecido": "",
            "txtEntidade": "Prefeitura Municipal de ABAÍRA",
            "txtOrgao": "",
            "txtUnidadeOrcamentaria": "",
            "txtElementoDespesa": "",
            "txtFonteRecurso": "",
            "pesquisar": "Pesquisar",
        }

        yield scrapy.FormRequest.from_response(
            response,
            url="https://www.tcm.ba.gov.br/controle-social/consulta-de-despesas/",
            method="GET",
            formdata=params,
            callback=self.parse_page,
        )

    def parse_page(self, response):
        page = "test"
        filename = f"{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
