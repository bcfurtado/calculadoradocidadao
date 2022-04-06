from unittest import TestCase

from calculadoradocidadao.demo1 import Demo


class TestDemo1(TestCase):
    def test_tested_function(self):
        self.assertEqual(Demo().tested_function(), True)
