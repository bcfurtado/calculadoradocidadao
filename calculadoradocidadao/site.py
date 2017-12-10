import lxml.html

from flask import Flask, request
from flask_restful import Api, Resource
import requests


app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello():
    return 'Hello World!'


class CorrigirPelaSelic(Resource):

    def post(self):
        form = request.form
        valorCorrigido = self.get_valor_corrigido(
            form['dataInicial'],
            form['dataFinal'],
            form['valorCorrecao']
        )
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

        r = requests.post(url, data=values)

        root = lxml.html.fromstring(r.text)
        result = root.xpath('//form/div[2]/table/tbody/tr[8]/td[2]/text()')
        return result[0]


api.add_resource(CorrigirPelaSelic, '/corrigirpelaselic')
