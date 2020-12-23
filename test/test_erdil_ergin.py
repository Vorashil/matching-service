import unittest
import main.algorithms.erdil_ergin as ee


class TestErdilErgin(unittest.TestCase):
    def test_response(self):
        self.assertEquals(ee.match(), "Erdil Ergin algorithm")
