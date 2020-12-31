import time, unittest
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
#####################################################################
class test_login(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("Before Each test!(setup method)")
        global driver
        driver = webdriver.Chrome(executable_path="C:/Projects/Automation/Drivers/chromedriver.exe")
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.implicitly_wait(5)


    @classmethod
    def setUpClass(cls):
        print("Open the Application!!!")


    @classmethod
    def tearDownClass(cls):
        print("Closing App AFTER FINISH RUNNING aLL TESTS")

    def test_negative_login(self):
        print("start 1st negative testing!!")
        driver.find_element_by_id('txtUsername').send_keys('Admin2')
        driver.find_element(By.ID, 'txtPassword').send_keys('admin1232')
        time.sleep(1)
        driver.find_element_by_css_selector('#btnLogin').click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#spanMessage'), 'Invalid credentials'))



    def test_login(self):
        print("Login with user and password- positive testing")
        driver.find_element_by_id('txtUsername').send_keys('Admin')
        driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
        time.sleep(1)
        driver.find_element_by_css_selector('#btnLogin').click()
        wait=WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, '/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/h1[1]'), 'Dashboard'))
        db=driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/h1[1]''').text
        self.assertEqual('Dashboard', db)

    def test_loginWithoutPassword(self):
        print("test login without password")
        driver.find_element_by_id('txtUsername').send_keys('Admin')
        driver.find_element_by_css_selector('#btnLogin').click()
        wait=WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#spanMessage'), 'Password cannot be empty'))


    def test_loginWithoutUsername(self):
        print("test login without username")
        driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
        driver.find_element_by_css_selector('#btnLogin').click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#spanMessage'), 'Username cannot be empty'))

    def test_loginWithEmptyFields(self):
        print("test login with empty fields")
        driver.find_element_by_id('txtUsername').clear()
        driver.find_element(By.ID, 'txtPassword').clear()
        time.sleep(1)
        driver.find_element_by_css_selector('#btnLogin').click()
        wait = WebDriverWait(driver, 10)
        print(driver.find_element(By.CSS_SELECTOR, '#spanMessage').text)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#spanMessage'), 'Username cannot be empty'))


    @unittest.skip("Currently I don't know how to verify the invisible password")
    def test_passwordIsNotVisible(self):
        driver.find_element_by_id('txtUsername').send_keys('Admin')
        driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
        time.sleep(1)
        wait=webdriver(driver, 10)


    @classmethod
    def tearDown(self):
        print("Finish testing (TEARDOWN method ))...")
        driver.quit()

if __name__ == "__main__":
    unittest.main()
