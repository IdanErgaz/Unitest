import unittest
from selenium import webdriver
class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:/Projects/Automation/Drivers/chromedriver.exe")
        driver.get("https://www.google.com")
        webTitle=driver.title

        self.assertTrue(webTitle=="Google") #True #verify if the website title is really Google

        self.assertFalse(webTitle=="Bingo")  #False - we expect that the title is NOT simillar


if __name__ == "__main__":
    unittest.main()