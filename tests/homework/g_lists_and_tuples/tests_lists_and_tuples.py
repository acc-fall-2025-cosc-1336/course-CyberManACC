import os, sys
_here = os.path.abspath(os.path.dirname(__file__))
_root = os.path.abspath(os.path.join(_here, "..", "..", ".."))
if _root not in sys.path:
    sys.path.insert(0, _root)
import unittest
from src.homework.g_lists_and_tuples.lists import get_p_distance, get_p_distance_matrix

class Test_Config(unittest.TestCase):

    def test_p_distance(self):
        a = ['T','T','T','C','C','A','T','T','T','A']
        b = ['G','A','T','T','C','A','T','T','T','C']
        self.assertAlmostEqual(get_p_distance(a, b), 0.4, places=5)

    def test_get_p_distance_matrix(self):
        data = [
            ['T','T','T','C','C','A','T','T','T','A'],
            ['G','A','T','T','C','A','T','T','T','C'],
            ['T','T','T','C','C','A','T','T','T','T'],
            ['G','T','T','C','C','A','T','T','T','A'],
        ]
        expected = [
            [0.0, 0.4, 0.1, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.1, 0.4, 0.0, 0.2],
            [0.1, 0.3, 0.2, 0.0],
        ]
        result = get_p_distance_matrix(data)
        # element-wise comparison with tolerance
        for i in range(len(expected)):
            for j in range(len(expected)):
                self.assertAlmostEqual(result[i][j], expected[i][j], places=5)

if __name__ == "__main__":
    import unittest
    unittest.main(verbosity=2)

