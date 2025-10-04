import unittest

from tests.homework.d_repetition import tests_repetition

suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)
unittest.TextTestRunner(verbosity=2).run(suite)
