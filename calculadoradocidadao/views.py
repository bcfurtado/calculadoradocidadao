import lxml.html

from flask import request
from flask_restful import Resource
import requests


class HomeView(Resource):
    def get(self):
        return {'msg': 'Hello World!'}


class CorrigirPelaSelicView(Resource):
    def post(self):
        form = request.form
        response = self.get_valor_corrigido(
            form['dataInicial'], form['dataFinal'], form['valorCorrecao']
        )
        valorCorrigido = self.parse_response(response.text)

        return {
            'dataInicial': form['dataInicial'],
            'dataFinal': form['dataFinal'],
            'valorCorrecao': form['valorCorrecao'],
            'valorCorrigido': valorCorrigido,
        }

    def get_valor_corrigido(self, data_inicial, data_final, valor_correcao):
        url = 'https://www3.bcb.gov.br/CALCIDADAO/publico/corrigirPelaSelic.do?method=corrigirPelaSelic'
        values = {
            'dataInicial': data_inicial,
            'dataFinal': data_final,
            'valorCorrecao': valor_correcao,
        }

        return requests.post(url, data=values)

    def parse_response(self, response):
        root = lxml.html.fromstring(response)
        result = root.xpath('//form/div[2]/table/tbody/tr[8]/td[2]/text()')
        return result[0]
