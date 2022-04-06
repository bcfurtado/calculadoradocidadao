from unittest import TestCase

from calculadoradocidadao.demo2 import Index


class TestDemo2(TestCase):
    def test_uncovered_if(self):
        self.assertEqual(Index().uncovered_if(), False)

    def test_fully_covered(self):
        self.assertEqual(Index().fully_covered(), True)
