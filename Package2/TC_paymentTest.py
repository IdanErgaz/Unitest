import unittest

class paymentTest(unittest.TestCase):
    def test_paymentInDollar(self):
        print("Test payment in dollars")
        self.assertEqual(5, 5)

    def test_paymentInRuppe(self):
        print("Test payment in rupees")
        self.assertTrue(True)



if __name__ == "__main__":
    unittest.main()