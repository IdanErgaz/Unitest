import unittest

class signUpTest(unittest.TestCase):
    def test_signByEmail(self):
        print("Test sign up  by Email")
        self.assertEqual(5, 5)

    def test_signByFacebook(self):
        print("Test sign up  by Facebook")
        self.assertEqual(5, 5)

    def test_signByTwitter(self):
        print("Test signup by Twitter")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()