import  unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def test(self):
        #assertGreater x>y
        self.assertGreater(100, 10, "Test filed!!")
        #assertGreaterEqual x>=y
        self.assertGreaterEqual(12, 12, "Test greater or equal failed!!")
        #assertLess x<y
        self.assertLess(8, 12)
        #assertLessEqual
        self.assertLessEqual(10, 10, "assertLessEqual test failed!!!")

if __name__ == "__main__":
    unittest.main()
