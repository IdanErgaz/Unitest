import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:/Projects/Automation/Drivers/chromedriver.exe")
        self.assertIsNotNone(driver) #it should pass since we have a driver
        driver=None
        self.assertIsNone(driver)  #it should fail since we HAVE A DRIVER

        # driver.get("https://www.google.com")
        # webTitle=driver.title


if __name__ == "__main__":
    unittest.main()