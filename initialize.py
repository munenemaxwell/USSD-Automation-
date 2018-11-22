from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options



class Initialize:
 def __init__(self):

  self.options=Options()
  self.options.headless=True
  self.driver = webdriver.Firefox(options=self.options, executable_path=r'D:/Gecko_driver_selenium/geckodriver.exe')
	 #assert "OCPanel - Login" in driver.title

 def navigate(self):
  self.driver.get("https://10.25.202.161/occontrolpanel/auth/login")
  username = self.driver.find_element_by_id("loginform-username")
  username.clear()
  username.send_keys("MMunene")
  password = self.driver.find_element_by_id("loginform-password")
  password.clear()
  password.send_keys("burex007*#")
  self.driver.find_element_by_name("login-button").click()
  self.driver.get('https://10.25.202.161/occontrolpanel/index.php?w=ocbrowser/services/index')
  self.driver.get('https://10.25.202.161/occontrolpanel/index.php?w=ocbrowser/tests/auto_detect')
    
 def destroy(self):
  self.driver.close()