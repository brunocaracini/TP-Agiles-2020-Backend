import unittest
from clases import Palabra

class TestValidaLetra(unittest.TestCase, Palabra):
    def test_list_int(self):
        self.assertEqual(self.validaLetra('casa', 'z'), True)

if __name__ == '__main__':
    unittest.main()