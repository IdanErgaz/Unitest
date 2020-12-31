import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome(executable_path="C:\Projects\Automation\Drivers\chromedriver.exe")
        driver.get("https://www.google.com")
        titleOfWebPage=driver.title


        #assertEqual
        self.assertEqual("Google", titleOfWebPage, "The webpage title are not the same!!!")
        #assertNotEqual
        self.assertNotEqual("Google123", titleOfWebPage, "The title is not as expected!!")




if __name__ =="__main__":
    unittest.main()