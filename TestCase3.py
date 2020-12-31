import unittest

class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("This is logging test")

    @classmethod
    def tearDown(self):
        print("TEARDOWN!!!  Finish Testing the test")
    @classmethod
    def setUpClass(cls):
        print("Before ALL tests running!!!")
        print("____________________________")
    @classmethod
    def tearDownClass(cls):
        print("____________________________")
        print("TearDown class - After finish running ALL tests!!")

    def test_search(self):
        print("test search")


    def test_advacedsearch(self):
        print("advanced search test")


    def test_prepaid(self):
        print("test prepaid !!!")


if __name__=="__main__":
    unittest.main()
