import lxml.html
import requests

BASE_URL = 'https://www3.bcb.gov.br/CALCIDADAO/publico'
CORRIGIR_PELA_SELIC_URL = f'{BASE_URL}/corrigirPelaSelic.do?method=corrigirPelaSelic'


class CalculadoraDoCidadaoAPI:
    def get_valor_corrigido(self, data_inicial, data_final, valor_correcao):
        values = {
            'dataInicial': data_inicial,
            'dataFinal': data_final,
            'valorCorrecao': valor_correcao,
        }

        response = requests.post(CORRIGIR_PELA_SELIC_URL, data=values)

        return self._parse_response(response.text)

    def _parse_response(self, response):
        root = lxml.html.fromstring(response)
        result = root.xpath('//form/div[2]/table/tbody/tr[8]/td[2]/text()')
        return result[0]
