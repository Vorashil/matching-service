import unittest
import main.algorithms.erdil_ergin as ee
import test.fixture.common_input_fixture as cif


class TestErdilErgin(unittest.TestCase):
    def test_response(self):
        common_input = cif.create_sample_input()
        self.assertEqual("Erdil Ergin algorithm calculates with the following input: 'we have 3 men and 3 women'",
                         ee.match(common_input))



