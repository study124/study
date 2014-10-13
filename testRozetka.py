# -*- coding: utf-8 -*-
'''
Created on Oct 11, 2014

@author: 
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Rozetka(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://rozetka.com.ua/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_rozetka(self):
        driver = self.driver
        driver.get(self.base_url + "/?gclid=Cj0KEQjwquOhBRCupYiu4an13scBEiQAss2Xkp8W9ArzcOJKJEZSxVhyEWmh0rZWF2--LQKPC3Cu6_waAhxz8P8HAQ")
        driver.find_element_by_link_text(u"Вход в интернет-магазин").click()
        driver.find_element_by_link_text(u"Зарегистрироваться").click()
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("test_123")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("test0000@test.ua")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("pa$$word")
        driver.find_element_by_css_selector("button.button-css-green").click()
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector(u"img[alt=\"Интернет магазин Rozetka.ua - Украина едина и неделима!\"]").click()
        driver.find_element_by_link_text(u"Телефоны, MP3, GPS").click()
        driver.find_element_by_link_text(u"Смартфоны").click()
        driver.find_element_by_css_selector("a[name=\"drop_link\"] > i").click()
        driver.find_element_by_link_text(u"от дешевых к дорогим").click()
         
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
      
        
    def tearDown(self):
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()