import unittest, time

class test_login(unittest.TestCase):

    def test1(self):
        print("this is test 1")

    def test2(self):
        print("This is test 2")

    def test3(self):
        print("this is test 3")

    @classmethod
    def setUp(self):
        print("Before each method!")

    @classmethod
    def tearDown(self):
        print("After each method!")

    @classmethod
    def setUpClass(cls):
        print("Once before All tests!!!!(class)")

    @classmethod
    def tearDownClass(cls):
        print("Once AFTER finish running all tests (class)")

if __name__ == "__main__":
    unittest.main()