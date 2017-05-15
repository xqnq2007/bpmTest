#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from comSeleFunc import *
import re
def waitNewWindow(driver,n):
    try:
        dr = WebDriverWait(driver, 30).until(lambda the_driver: len(the_driver.window_handles) >= n)
    except  Exception:
        print 'new window加载失败'
def waitElement(driver,locator):

    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(locator))
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(locator))
        #WebDriverWait(driver, 30).until(lambda driver:driver.find_element_by_xpath("//div[@class='l-dialog-content' and text()='启动流程成功']").is_displayed())
    except:
        print '元素加载失败',locator
def waitElementDisplay(driver,by, value=0):
    try:
        WebDriverWait(driver, 30).until(lambda driver:driver.find(by,value).is_displayed())
    except:
        print '元素display失败'
def waitAndFindElement(driver,by, value=0, timedeta=5, timeout=300):
    element = None
    endtime = timeout

    while endtime > 0:
        try:
            element = driver.find_element(by, value)
        except:
            pass
        if element:
            break
        else:
            time.sleep(timedeta)
            endtime = endtime - timedeta

    return element
def isElementPresent(driver,by,value):
    try:
        driver.find_element(by,value)
        return True
    except:
        return False


#curBrowser = webdriver.Firefox();
curBrowser = webdriver.Chrome();

curBrowser.get("http://122.4.80.27:8081/csrbpm/")


waitAndFindElement(curBrowser, By.XPATH, "//a[text()='登录']")
curBrowser.find_element_by_name("username").send_keys("010500017997")
curBrowser.find_element_by_name("password").send_keys("1")
curBrowser.find_element_by_xpath("//a[text()='登录']").click()
waitAndFindElement(curBrowser, By.XPATH, "//span[text()='个人办公']")
curBrowser.find_element_by_xpath("//span[text()='个人办公']").click()
time.sleep(1)
tmp=waitAndFindElement(curBrowser, By.XPATH, "//span[text()='我承接的流程']")
ActionChains(curBrowser).double_click(tmp).perform()
waitAndFindElement(curBrowser, By.XPATH, "//span[text()='待办事宜']")
curBrowser.find_element_by_xpath("//span[text()='待办事宜']").click()
waitAndFindElement(curBrowser, By.XPATH, "//iframe[contains(@src,'/csrbpm/platform/bpm/task/pendingMatters.ht')]")  # 加载流程任务列表
curBrowser.switch_to.frame(
    curBrowser.find_element_by_xpath("//iframe[contains(@src,'/csrbpm/platform/bpm/task/pendingMatters.ht')]"))
waitAndFindElement(curBrowser, By.XPATH, "//iframe[contains(@src,'/csrbpm/platform/bpm/task/pendingMattersList.ht')]")  # 加载流程任务列表
curBrowser.switch_to.frame(
    curBrowser.find_element_by_xpath("//iframe[contains(@src,'/csrbpm/platform/bpm/task/pendingMattersList.ht')]"))
waitAndFindElement(curBrowser, By.XPATH, "//table[@id='taskItem']")  # 加载流程任务列表
curBrowser.find_element_by_xpath("//table[@id='taskItem']/tbody/tr[1]/td[2]/a").click()
waitNewWindow(curBrowser,2)
print curBrowser.current_window_handle
handles = curBrowser.window_handles  # 获取当前窗口句柄集合（列表类型）
for handle in handles:  # 切换窗口（切换到搜狗）
    if handle != curBrowser.current_window_handle:
        curBrowser.switch_to.window(handle)
print curBrowser.current_window_handle
waitAndFindElement(curBrowser,By.XPATH,"//div[@class='l-dialog-btn-inner' and text()='确定']")
curBrowser.find_element_by_xpath("//div[@class='l-dialog-btn-inner' and text()='确定']").click()
curBrowser.find_element_by_id("btnAgree").click()
waitAndFindElement(curBrowser,By.XPATH,"//div[@class='l-dialog-content' and text()='您确定执行此操作吗？']")
curBrowser.find_element_by_xpath("//div[@class='l-dialog-btn-inner' and text()='是']").click()
curBrowser.close()