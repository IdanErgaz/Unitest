import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        # driver = webdriver.Chrome(executable_path="C:/Projects/Automation/Drivers/chromedriver.exe")
        # driver.get("https://www.google.com")
        # webTitle=driver.title
        list=["python", "Idan", "Nataly", "Alma", "Shira", "Joy"]
        self.assertIn("Shira", list)  #cerify if an element is part of the list
        self.assertNotIn("boris", list)
if __name__ == "__main__":
    unittest.main()