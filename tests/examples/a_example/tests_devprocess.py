import unittest


from src.examples.a_example.devprocess import echo_value

class Test_Config(unittest.TestCase):

    def test_echo_value(self):
        self.assertEqual("Hello, world!", echo_value("Hello, world!"))
        self.assertEqual(5, echo_value(5))
        
