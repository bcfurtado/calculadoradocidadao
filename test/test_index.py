from unittest import main, TestCase
from unittest.mock import patch

from calculadoradocidadao.site import app
from flask import json


class AppTestCase(TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello World!')

    @patch('calculadoradocidadao.site.requests.post')
    def test_post_valor_corrigido_pela_selic(self, mock_response):
        with open('test/corrigir_pela_selic_result.html', 'r', encoding='iso-8859-1') as file:

            mock_response.return_value.status_code = 200
            mock_response.return_value.text = file.read()

            response = self.app.post('/corrigirpelaselic', data=dict(
                dataInicial='30/09/2015',
                dataFinal='05/12/2017',
                valorCorrecao='2607,90',
            ))

            data = json.loads(response.data)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['dataInicial'], '30/09/2015')
            self.assertEqual(data['dataFinal'], '05/12/2017')
            self.assertEqual(data['valorCorrecao'], '2607,90')
            self.assertEqual(data['valorCorrigido'], 'R$ 3.364,58 (REAL)')


if __name__ == '__main__':
    main()
