import lxml.html

from flask import request
from flask_restful import Resource

from calculadoradocidadao.api import CalculadoraDoCidadaoAPI


class HomeView(Resource):
    def get(self):
        return {'msg': 'Hello World!'}


class CorrigirPelaSelicView(Resource):
    api = CalculadoraDoCidadaoAPI()

    def post(self):
        form = request.form

        valor_corrigido = self.api.get_valor_corrigido(
            form['dataInicial'],
            form['dataFinal'],
            form['valorCorrecao'],
        )

        return {
            'dataInicial': form['dataInicial'],
            'dataFinal': form['dataFinal'],
            'valorCorrecao': form['valorCorrecao'],
            'valorCorrigido': valor_corrigido,
        }
