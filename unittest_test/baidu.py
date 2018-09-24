from unittest_test.webdriver import WebDriver
import unittest
from selenium import webdriver
from ddt import ddt,data,file_data

baidu_input_element = "kw"
baidu_click_element = "su"
url = "https://www.baidu.com/"
@ddt
class BaiduTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @data('unittest', 'selenium', 'python', 'pycharm', 'pytest', '二次封装')
    def test_BaiduSearch(self,value):
        page = WebDriver(self.driver)
        page.open(url)
        page.id(baidu_input_element).send_keys(value)
        page.id(baidu_click_element).click()


if __name__ =='__main__':
    unittest.main()
