import unittest

class AppTesting(unittest.TestCase):
    @unittest.SkipTest    #for skipping a test in running
    def test_search(self):
        print("This is search test")

    def test_advancesearch(self):
        print("this is advance test method")

    @unittest.skip("I am skippping this cause I want to!!!")
    def test_prepaidrecharge(self):
        print("this is prepaid recharged test")

    @unittest.skipIf(1==1, "the numbers are NOT equals")
    def test_postpaidrecharged(self):
        print("this is post paid recharged")

    def test_loggingbygemail(self):
        print("this is logging by gmail test")

    def test_loggingbytwitter(self):
        print("logging by twitter test")


if __name__ == '__main__':
    unittest.main()
