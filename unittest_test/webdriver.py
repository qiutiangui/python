import unittest
from selenium import webdriver
class WebDriver():
    """封装webdriver方法"""

    def __init__(self,driver):
        """初始化 启动浏览器方法"""
        self.driver = driver

    def open(self,url):
        """获取url"""
        self.driver.get(url)

    def id(self,id):
        """id定位方法"""
        return self.driver.find_element_by_id(id)

    def xpath(self,xpath):
        """xpath定位方法"""
        return self.driver.find_element_by_xpath(xpath)

    def xpath_send_key(self,xpath,value):
        return self.driver.find_element_by_xpath(xpath).send_keys(value)

    def xpath_click(self,xpath):
        return self.driver.find_element_by_xpath(xpath).click()

    def id_send_key(self,id,value):
        return self.driver.find_element_by_xpath(id).send_keys(value)

    def id_click(self,id):
        return self.driver.find_element_by_xpath(id).click()