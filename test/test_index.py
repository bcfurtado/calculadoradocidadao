from pathlib import Path
from unittest import main, TestCase

from calculadoradocidadao.site import app
from flask import json
from vcr import VCR

fixtures = Path(__file__).parent.joinpath('fixtures').as_posix()
vcr = VCR(
    cassette_library_dir=fixtures,
    record_mode='once',
    filter_headers=['auth-token'],
    path_transformer=VCR.ensure_suffix('.yaml'),
    decode_compressed_response=True,
)


class AppTestCase(TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_hello_world(self):
        # Act
        response = self.app.get('/')

        # Assert
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['msg'], 'Hello World!')

    @vcr.use_cassette()
    def test_post_valor_corrigido_pela_selic(self):
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
