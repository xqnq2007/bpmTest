# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://sahitest.com/demo/alertTest.htm')

driver.find_element_by_name('b1').click()
try:
    WebDriverWait(driver, 30).until(EC.alert_is_present())
    #WebDriverWait(driver, 30).until(EC.visibility_of_element_located(locator))
    # WebDriverWait(driver, 30).until(lambda driver:driver.find_element_by_xpath("//div[@class='l-dialog-content' and text()='启动流程成功']").is_displayed())
except:
    print '弹窗加载失败'
a1 = driver.switch_to.alert  # 通过switch_to.alert切换到alert
sleep(1)
print a1.text  # text属性输出alert的文本
a1.accept()  # alert“确认”
sleep(1)

driver.quit()