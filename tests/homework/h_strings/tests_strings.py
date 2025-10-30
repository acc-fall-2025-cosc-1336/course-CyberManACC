import os, sys
_here = os.path.abspath(os.path.dirname(__file__))
_root = os.path.abspath(os.path.join(_here, "..", "..", ".."))
if _root not in sys.path:
    sys.path.insert(0, _root)

import unittest
from src.homework.h_strings.strings import get_hamming_distance, get_dna_complement


class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
        self.assertEqual(
            get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"), 7
        )

    def test_get_dna_complement(self):
        self.assertEqual(get_dna_complement("AAAACCCGGT"), "ACCGGGTTTT")

if __name__ == "__main__":
    unittest.main()
