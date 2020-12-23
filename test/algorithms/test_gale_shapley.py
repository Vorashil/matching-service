import unittest
import main.algorithms.gale_shapley as gs
import test.fixture.common_input_fixture as cif


class TestErdilErgin(unittest.TestCase):
    def test_count(self):
        common_input = cif.create_sample_input()
        self.assertEquals(gs.count_agents(common_input), (3, 3))



