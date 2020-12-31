import unittest
import time

class test_assertion(unittest.TestCase):
    def test_assertEqual(self):
        print("Test assert equall")
        self.assertEqual(5,5)

    def test_assertIn(self):
        print("Test assertIn")
        names=['Idan', 'Nataly', 'Alma', 'Shira']
        self.assertIn('Nataly', names)

    @classmethod
    def setUp(self):
        print("Before each method")

    @classmethod
    def tearDown(self):
        print("Afte each test")
if __name__ == " __main__":
    unittest.main()

