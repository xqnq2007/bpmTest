#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
from time import sleep
def waitNewWindow(driver,n):
    try:
        dr = WebDriverWait(driver, 30).until(lambda the_driver: len(the_driver.window_handles) >= n)
    except  Exception:
        print 'new window加载失败'
def waitElement(driver,locator):
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(locator))
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(locator))
    except:
        print '元素加载失败',locator
def waitAlert(driver):
    try:
        WebDriverWait(driver, 30).until(EC.alert_is_present())
    except:
        print '弹窗加载失败'
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

def getUserAccount(curBrowser):
    js = 'window.open("http://122.4.80.27:8081/csrbpm/");'
    curBrowser.execute_script(js)
    handles = curBrowser.window_handles  # 获取当前窗口句柄集合（列表类型）
    for handle in handles:  # 切换窗口（切换到搜狗）
        if handle != curBrowser.current_window_handle:
            curBrowser.switch_to_window(handle)
    waitAndFindElement(curBrowser, By.XPATH, "//a[text()='登录']")
    curBrowser.find_element_by_name("username").send_keys("admin")
    curBrowser.find_element_by_name("password").send_keys("crrc6699")
    curBrowser.find_element_by_xpath("//a[text()='登录']").click()
    waitAndFindElement(curBrowser, By.XPATH, "//span[text()='流程管理']")
    curBrowser.find_element_by_xpath("//span[text()='流程管理']").click()
    time.sleep(1)
    waitAndFindElement(curBrowser, By.XPATH, "//span[text()='流程任务管理']")
    curBrowser.find_element_by_xpath("//span[text()='流程任务管理']").click()
    waitAndFindElement(curBrowser, By.XPATH, "//iframe[contains(@src,'/csrbpm/platform/bpm/task/list.ht')]")  # 加载流程任务列表
    curBrowser.switch_to.frame(
        curBrowser.find_element_by_xpath("//iframe[contains(@src,'/csrbpm/platform/bpm/task/list.ht')]"))
    waitAndFindElement(curBrowser, By.XPATH, "//table[@id='taskItem']")  # 加载流程任务列表
    tmpStep = curBrowser.find_element_by_xpath("//table[@id='taskItem']/tbody/tr[1]/td[3]").text
    print tmpStep
    tmpa=curBrowser.find_element_by_xpath("//table[@id='taskItem']/tbody/tr[1]/td[4]/a")
    tmpHref=tmpa.get_attribute('href')
    print tmpHref
    shieldHref='http://122.4.80.27:8081/csrbpm/platform/bpm/task/list.ht#'
    if tmpHref!=shieldHref:
        print re.search('userId=(\d+)&', tmpHref).group(1)
        usrAcount = '0' + re.search('userId=(\d+)&', tmpHref).group(1)
    elif tmpHref==shieldHref:
        tmpa.click()
        waitAndFindElement(curBrowser, By.XPATH, "//table[@class='table-detail']")
        tmpHref1=curBrowser.find_element_by_xpath("//table[@class='table-detail']/tbody/tr[1]/td/a").get_attribute('href')
        usrAcount = '0' + re.search('userId=(\d+)&', tmpHref1).group(1)
    curBrowser.close()
    curBrowser.switch_to_window(handles[0])
    return tmpStep,usrAcount
def toMobilePedingList(browser,curUser,curPass):  #进入待办流程列表
    browser.find_element_by_name("title").send_keys(curUser)
    browser.find_element_by_name("content").send_keys(curPass)
    browser.find_element_by_xpath("//*[text()='提交']").click()
    waitAndFindElement(browser, By.ID, "PendingMatters0")  # 加载bpm首页
    browser.find_element_by_id("PendingMatters0").click()
    waitAndFindElement(browser, By.XPATH, "//div[@type='image'][1]")  # 加载待办列表
    curStep = browser.find_element_by_xpath("(//div[@class='name'])[1]/span[1]").text
    #pattern='(.*)\n(.*)'
    out=re.search('(.*)\n(.*)', curStep).group(1)
    return out
    #f.write(curStep+'\n\n')
def normalStep(browser,f):    # 通用节点处理，直接点击同意，不用选择人或组织
    browser.find_element_by_xpath("//div[@type='image'][1]").click()#点击待办列表第一项
    waitAndFindElement(browser, By.XPATH, "//span[text()='同意' or text()='提交']")  # 审批页面加载
    handle1 = browser.current_window_handle
    browser.find_element_by_xpath("//span[contains(text(), '同意') or contains(text(), '提交')]").click()
    #waitAndFindElement(browser, By.XPATH, "//div[contains(text(), '任务')]")  # 审批结果加载
    # try:
    #     if browser.find_element_by_xpath("//div[contains(text(), '执行任务成功')]"):
    #         print '执行任务成功'
    #         f.write('执行任务成功\n\n' )
    # except Exception:
    #     print ''
    # try:
    #     if browser.find_element_by_xpath("//div[contains(text(), '任务跳转失败')]"):
    #         print '任务跳转失败'
    #         f.write('任务跳转失败\n\n')
    # except Exception:
    #     print ''
    #waitAndFindElement(browser, By.XPATH, "//span[text()='确定']")  # 确定加载
    #waitAndFindElement(browser, By.XPATH, "//div[contains(text(), '执行任务成功')]")  # 确定加载
    waitAlert(browser)
    a1 = browser.switch_to.alert  # 通过switch_to.alert切换到alert
    sleep(1)
    if a1.text=='执行任务成功!':
        a1.accept()  # alert“确认”
        f.write('执行任务成功!');
        return True
    else:
        a1.accept()  # alert“确认”
        f.write('执行任务失败!');
        return False
def shieldStep(curBrowser,curUsr,curPwd,f):
    js = 'window.open("http://122.4.80.27:8081/csrbpm/");'
    curBrowser.execute_script(js)
    handles = curBrowser.window_handles  # 获取当前窗口句柄集合（列表类型）
    for handle in handles:  # 切换窗口（切换到搜狗）
        if handle != curBrowser.current_window_handle:
            curBrowser.switch_to_window(handle)
    waitAndFindElement(curBrowser, By.XPATH, "//a[text()='登录']")
    curBrowser.find_element_by_name("username").send_keys(curUsr)
    curBrowser.find_element_by_name("password").send_keys(curPwd)
    curBrowser.find_element_by_xpath("//a[text()='登录']").click()
    waitAndFindElement(curBrowser, By.XPATH, "//span[text()='个人办公']")
    curBrowser.find_element_by_xpath("//span[text()='个人办公']").click()
    time.sleep(1)
    tmp = waitAndFindElement(curBrowser, By.XPATH, "//span[text()='我承接的流程']")
    ActionChains(curBrowser).double_click(tmp).perform()
    waitAndFindElement(curBrowser, By.XPATH, "//span[text()='待办事宜']")
    curBrowser.find_element_by_xpath("//span[text()='待办事宜']").click()
    waitAndFindElement(curBrowser, By.XPATH,
                       "//iframe[contains(@src,'/csrbpm/platform/bpm/task/pendingMatters.ht')]")  # 加载流程任务列表
    curBrowser.switch_to.frame(
        curBrowser.find_element_by_xpath("//iframe[contains(@src,'/csrbpm/platform/bpm/task/pendingMatters.ht')]"))
    waitAndFindElement(curBrowser, By.XPATH,
                       "//iframe[contains(@src,'/csrbpm/platform/bpm/task/pendingMattersList.ht')]")  # 加载流程任务列表
    curBrowser.switch_to.frame(
        curBrowser.find_element_by_xpath("//iframe[contains(@src,'/csrbpm/platform/bpm/task/pendingMattersList.ht')]"))
    waitAndFindElement(curBrowser, By.XPATH, "//table[@id='taskItem']")  # 加载流程任务列表
    curBrowser.find_element_by_xpath("//table[@id='taskItem']/tbody/tr[1]/td[2]/a").click()
    waitNewWindow(curBrowser, 2)
    handle1=curBrowser.current_window_handle
    handles = curBrowser.window_handles  # 获取当前窗口句柄集合（列表类型）
    for handle in handles:  # 切换窗口（切换到搜狗）
        if handle != handle1:
            curBrowser.switch_to.window(handle)
    if EC.presence_of_element_located((curBrowser,By.XPATH, "//div[@class='l-dialog-btn-inner' and text()='确定']")):
        waitAndFindElement(curBrowser, By.XPATH, "//div[@class='l-dialog-btn-inner' and text()='确定']")
        curBrowser.find_element_by_xpath("//div[@class='l-dialog-btn-inner' and text()='确定']").click()
    curBrowser.find_element_by_id("btnAgree").click()
    try:
        waitAndFindElement(curBrowser, By.XPATH, "//div[@class='l-dialog-content' and text()='您确定执行此操作吗？']")
        curBrowser.find_element_by_xpath("//div[@class='l-dialog-btn-inner' and text()='是']").click()
        f.write('PC端执行任务成功!');
    except:
        f.write('PC端执行任务失败!');
    curBrowser.close()
    curBrowser.switch_to.window(handle1)
    curBrowser.close()