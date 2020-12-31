import unittest
from selenium import webdriver

class SearchEnginessTest(unittest.TestCase):
    def test_Google(self):
        self.driver=webdriver.Chrome(executable_path="C:\Projects\Automation\Drivers\chromedriver.exe")
        self.driver.get("https://google.com")
        print("The website title is:", self.driver.title)
        self.driver.close()


    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="C:\Projects\Automation\Drivers\chromedriver.exe")
        self.driver.get("https://bing.com")
        print("The website title is:", self.driver.title)
        self.driver.close()



if __name__=="__main__":
    unittest.main()
