import unittest
from tests.homework.h_strings import tests_strings

suite = unittest.TestLoader().loadTestsFromModule(tests_strings)
unittest.TextTestRunner(verbosity=2).run(suite)
