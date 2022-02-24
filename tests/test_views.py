from pathlib import Path
from unittest import TestCase, main

from flask import json
from vcr import VCR

from calculadoradocidadao.site import app

fixtures = Path(__file__).parent.joinpath('fixtures').as_posix()
vcr = VCR(
    cassette_library_dir=fixtures,
    record_mode='once',
    filter_headers=['auth-token'],
    path_transformer=VCR.ensure_suffix('.yaml'),
    decode_compressed_response=True,
)


class ViewTestCase(TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()


class TestHomeView(ViewTestCase):
    def test_GET_NoData_ReturnHelloWorld(self):
        # Act
        response = self.app.get('/')

        # Assert
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['msg'], 'Hello World!')


class TestCorrigirPelaSelicView(ViewTestCase):
    @vcr.use_cassette()
    def test_POST_ValidInput_ReturnValorCorrigidoPelaSelic(self):
        # Act
        response = self.app.post(
            '/corrigirpelaselic',
            data={
                'dataInicial': '30/09/2015',
                'dataFinal': '05/12/2017',
                'valorCorrecao': '2607,90',
            },
        )

        # Arrange
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['dataInicial'], '30/09/2015')
        self.assertEqual(data['dataFinal'], '05/12/2017')
        self.assertEqual(data['valorCorrecao'], '2607,90')
        self.assertEqual(data['valorCorrigido'], 'R$ 3.364,58 (REAL)')

    def test_POST_InvalidInput_Return400(self):
        # Act
        response = self.app.post('/corrigirpelaselic', data={})

        # Arrange
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        expected_message = (
            'The browser (or proxy) sent a request that this server'
            ' could not understand.'
        )
        self.assertEqual(data['message'], expected_message)
