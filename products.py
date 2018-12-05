from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from initialize import Initialize
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

######################database####################
import mysql.connector
from mysql.connector import MySQLConnection, Error

class Product(Initialize):
    def __init__(self, intial_path, max_depth,ignore_choices,description,suite_number):
     Initialize.__init__(self)
     self.intial_path = intial_path
     self.max_depth = max_depth
     self.ignore_choices=ignore_choices
     self.description=description
     self.suite_no=suite_number
    

    def execute(self):
     self.navigate()
     originator_el=self.driver.find_element_by_id('adt-originator')
     destination_el=self.driver.find_element_by_id('adt-destination')
     max_depth_el=self.driver.find_element_by_id('adt-maxdepth')
     initial_path_el=self.driver.find_element_by_id('adt-initialpath')
     ignore_choices_el=self.driver.find_element_by_id('adt-ignorechoices')
     originator_el.send_keys("254740788450")
     destination_el.send_keys("544")
     max_depth_el.send_keys(self.max_depth)
     initial_path_el.send_keys(self.intial_path)
     ignore_choices_el.send_keys(self.ignore_choices)
     self.driver.find_element_by_class_name("btn-success").click()
     self.driver.implicitly_wait(10)

     print("+++++++++++++++++++++"+self.description+"++++++++++++++++++++++")

     try:
      myElem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'kkkmessage')))
      print(self.driver.find_element_by_class_name("at-head").text)
     except TimeoutException:
      text=self.driver.find_element_by_class_name("at-head").text
      text=text[:5]+'\n'+text[5:12]+'\n'+text[12:20]+'\n'+text[20:30]+'\n'+text[30:40]
      print(text)
      
      #####initialize DB########
      conn = mysql.connector.connect(host='localhost',
                                       database='reports',
                                       user='admin',
                                       password='burex007')
       
      try:
       table = self.driver.find_element_by_css_selector("table.test-scenario");
       rows= table.find_elements_by_tag_name("tr")
       td=rows[len(rows)-1].text
       expected=td[9:]
       if "You have successfully purchased" in expected:
        print("Outcome : Test passed ")
        try:
         if conn.is_connected():
          cursor = conn.cursor()
          query = "INSERT INTO aims_exec_hist(run_number,suite_number,description,no_passed,no_failed,collection_no,expected_msg,title)" \
                           " VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
          args = (self.suite_no,self.suite_no, self.description,1,0,0,expected,'544 Bundle Purchase')
          cursor.execute(query, args)
          conn.commit()

        except Error as e:
         print(e)
        finally:
         cursor.close()
         conn.close()

       else:
        print("Outcome : Test Failed ")
        try:
         
         if conn.is_connected():
          cursor = conn.cursor()
          query = "INSERT INTO aims_exec_hist(run_number,suite_number,description,no_passed,no_failed,collection_no,expected_msg,title)" \
                           " VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
          args = (self.suite_no,self.suite_no, self.description,0,1,0,expected,'544 Bundle Purchase')
          cursor.execute(query, args)
          conn.commit()
        except Error as e:
         print(e)
        finally:
         cursor.close()
         conn.close()

      except NoSuchElementException:
       expected='Test execution failed because Opencode failed to render table detailing scenario details'
       print("Outcome :Uknown...Please Verify manually")
       try:
        if conn.is_connected():
         cursor = conn.cursor()
         query = "INSERT INTO aims_error_unknown(run_number,description,err_desc)" \
                           " VALUES(%s,%s,%s)"
         args = (self.suite_no, self.description,expected)
         cursor.execute(query, args)
         conn.commit()
       except Error as e:
        print(e)
       finally:
        cursor.close()
        conn.close()
    
 
    def clear(self):
     originator_el=self.driver.find_element_by_id('adt-originator').clear()
     destination_el=self.driver.find_element_by_id('adt-destination').clear()
     max_depth_el=self.driver.find_element_by_id('adt-maxdepth').clear()
     initial_path_el=self.driver.find_element_by_id('adt-initialpath').clear()
     ignore_choices_el=self.driver.find_element_by_id('adt-ignorechoices').clear()
