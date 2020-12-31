import unittest

class LoginTest(unittest.TestCase):

    # @classmethod
    # def setUp(self):
    #     print("Print BEFORE EACH test")
    #
    # @classmethod
    # def tearDown(self):
    #     print("Print After EACH test")

    def test_loginByEmail(self):
        print("Test login by Email")
        self.assertEqual(5, 5)


    def test_loginByFacebook(self):
        print("Test login by Facebook")
        self.assertEqual(5, 5)

    def test_loginByTwitter(self):
        print("Test login by Twitter")
        self.assertTrue(True)

if __name__ =="__main__":
    unittest.main()