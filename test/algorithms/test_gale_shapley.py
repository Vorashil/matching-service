import unittest
import main.algorithms.gale_shapley as gs
import test.fixture.common_input_fixture as cif
from main.exceptions.gale_shapley_exception import GaleShapleyException


class TestGaleShapley(unittest.TestCase):
    def test_count(self):
        common_input = cif.create_sample_input()
        self.assertEquals(gs.count_agents(common_input), (3, 3))

    def test_validation_unequal_men_women_list(self):
        common_input = cif.create_sample_input()
        common_input.men_list.pop()
        with self.assertRaises(GaleShapleyException) as context:
            gs.validate(common_input)
            self.assertEquals('There should be the same number of men and women', str(context.exception))
