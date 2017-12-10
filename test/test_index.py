import unittest

import app
from flask import json


class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello World!')

    def test_get_valor_corrigido_pela_selic(self):
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
    unittest.main()
