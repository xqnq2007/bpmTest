#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#driver = webdriver.Chrome()
import time
#options = webdriver.ChromeOptions()

#options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
#options.add_argument("--user-data-dir=C:/Users/CSS/AppData/Local/Google/Chrome/User Data/Default");
def getUserAccount(curBrowser):
    js='window.open("http://122.4.80.27:8081/csrbpm/");'
    curBrowser.execute_script(js)
    handles = curBrowser.window_handles # 获取当前窗口句柄集合（列表类型）
    #print handles # 输出句柄集合 
    for handle in handles:# 切换窗口（切换到搜狗）
        if handle!=curBrowser.current_window_handle:
            #print 'switch to ',handle
            curBrowser.switch_to_window(handle)
    try:
        dr=WebDriverWait(curBrowser,50)#10秒内每隔500毫秒扫描1次页面变化，当出现指定的元素后结束,driver就是上面的句柄    
        dr.until(lambda the_driver:the_driver.find_element_by_xpath("//a[text()='登录']").is_displayed())
    except  Exception:
        print 'bpmPC首页加载失败' 
    pcCommonStep(curBrowser,'admin','crrc6699')   
    #time.sleep(3)
    curBrowser.find_element_by_xpath("//span[text()='流程管理']").click()
    time.sleep(1)
    try:
        dr=WebDriverWait(curBrowser,30)#10秒内每隔500毫秒扫描1次页面变化，当出现指定的元素后结束,driver就是上面的句柄    
        dr.until(lambda the_driver:the_driver.find_element_by_xpath("//span[text()='流程任务管理']").is_displayed())
    except  Exception:
        print '流程任务管理加载失败' 
    curBrowser.find_element_by_xpath("//span[text()='流程任务管理']").click()
    try:
        dr=WebDriverWait(curBrowser,30)#10秒内每隔500毫秒扫描1次页面变化，当出现指定的元素后结束,driver就是上面的句柄    
        dr.until(lambda the_driver:the_driver.find_element_by_xpath("//iframe[contains(@src,'/csrbpm/platform/bpm/task/list.ht')]").is_displayed())
    except  Exception:
        print '流程任务列表加载失败' 
    #time.sleep(3)
    curBrowser.switch_to_frame(curBrowser.find_element_by_xpath("//iframe[contains(@src,'/csrbpm/platform/bpm/task/list.ht')]"))
    tmpHref=curBrowser.find_element_by_xpath("//table[@id='taskItem']/tbody/tr[1]/td[4]/a").get_attribute('href')
    print tmpHref
    print re.search('userId=(\d+)&', tmpHref).group(1)
    usrAcount='0'+re.search('userId=(\d+)&', tmpHref).group(1)
    
    
    curBrowser.close()  
    curBrowser.switch_to_window(handles[0]) 
    return usrAcount    
def commonStep(browser,f,curUser):  #进入待办流程列表
    browser.find_element_by_name("title").send_keys(curUser)
    browser.find_element_by_name("content").send_keys("1")
    browser.find_element_by_xpath("//*[text()='提交']").click()
    try:
        dr=WebDriverWait(browser,10)#10秒内每隔500毫秒扫描1次页面变化，等待登录成功，ext-button-3为待办事宜    
        dr.until(lambda browser:browser.find_element_by_id("ext-button-3").is_displayed())
    except  Exception:
        print '登录失败' 
        f.write('登录失败\n\n' )   
    browser.find_element_by_id("ext-button-3").click()
    try:
        dr=WebDriverWait(browser,10)#10秒内每隔500毫秒扫描1次页面变化，等待待办列表加载成功    
        dr.until(lambda browser:browser.find_element_by_xpath("//div[@type='image'][1]").is_displayed())
    except  Exception:
        print '首页加载失败'
        f.write('首页加载失败\n\n' )     
    curStep= browser.find_element_by_xpath("(//div[@class='name'])[1]/span[1]").text
    f.write(curStep+'\n\n')
def pcCommonStep(browser,curUser,userpwd):  #登录进入PC浏览器
    browser.find_element_by_name("username").send_keys(curUser)
    browser.find_element_by_name("password").send_keys(userpwd)
    browser.find_element_by_xpath("//a[text()='登录']").click()
    try:
        dr=WebDriverWait(browser,30)#10秒内每隔500毫秒扫描1次页面变化，当出现指定的元素后结束,driver就是上面的句柄    
        dr.until(lambda browser:browser.find_element_by_xpath("//span[text()='流程管理']").is_displayed())
        print 'PC浏览器登录成功'
    except  Exception:
        print 'PC浏览器登录失败' 
def pcSuperUserCommonStep(curBrowser):  #PC浏览器超级用户共用操作，即点击流程管理，流程任务管理，点击当前待办事项
    curBrowser.find_element_by_xpath("//span[text()='流程管理']").click()
    time.sleep(1)
    try:
        dr=WebDriverWait(curBrowser,30)#10秒内每隔500毫秒扫描1次页面变化，当出现指定的元素后结束,driver就是上面的句柄    
        dr.until(lambda the_driver:the_driver.find_element_by_xpath("//span[text()='流程任务管理']").is_displayed())
    except  Exception:
        print '流程任务管理加载失败' 
    curBrowser.find_element_by_xpath("//span[text()='流程任务管理']").click()
    try:
        dr=WebDriverWait(curBrowser,30)#10秒内每隔500毫秒扫描1次页面变化，当出现指定的元素后结束,driver就是上面的句柄    
        dr.until(lambda the_driver:the_driver.find_element_by_xpath("//iframe[contains(@src,'/csrbpm/platform/bpm/task/list.ht')]").is_displayed())
    except  Exception:
        print '流程任务列表加载失败' 
    time.sleep(3)
    
    curBrowser.switch_to_frame(curBrowser.find_element_by_xpath("//iframe[contains(@src,'/csrbpm/platform/bpm/task/list.ht')]"))
    time.sleep(5)
    #curBrowser.find_element_by_xpath("//table[@id='taskItem']/tbody/tr[1]/td[2]/a[@href='#10000061319742' and onclick='javascript:executeTask(10000061319742,'出差申请-部门领导审核')']").click()  
    
def normalStep(browser,f):    # 通用节点处理，直接点击同意，不用选择人或组织
    browser.find_element_by_xpath("//div[@type='image'][1]").click()#点击待办列表第一项
    time.sleep(5)
    try:
        dr=WebDriverWait(browser,15)#10秒内每隔500毫秒扫描1次页面变化，等待审批页面加载成功    
        dr.until(lambda browser:browser.find_element_by_xpath("//span[text()='同意' or text()='提交']").is_displayed())
    except  Exception:
        print '审批页面加载失败'
        f.write('审批页面加载失败\n\n' )        
    browser.find_element_by_xpath("//span[contains(text(), '同意') or contains(text(), '提交')]").click()
    try:
        dr=WebDriverWait(browser,25)#10秒内每隔500毫秒扫描1次页面变化，等待审批结果    
        dr.until(lambda browser: (browser.find_element_by_xpath("//div[contains(text(), '任务')]")).is_displayed())
    except  Exception:
        print '审批结果加载失败'
        f.write('审批结果加载失败\n\n' )     
    try:
        if browser.find_element_by_xpath("//div[contains(text(), '执行任务成功')]"):
            print '执行任务成功'
            f.write('执行任务成功\n\n' )  
    except Exception:
        print '' 
    try:
        if browser.find_element_by_xpath("//div[contains(text(), '任务跳转失败')]"):
            print '任务跳转失败'
            f.write('任务跳转失败\n\n' )  
    except Exception:
        print ''

    browser.find_element_by_xpath("//span[text()='确定']").click()
def shieldStep(browser,f,curUser):#  已屏蔽节点处理
    browser.find_element_by_xpath("//div[@type='image'][1]").click()#点击待办列表第一项
    time.sleep(5)
    try:
        dr=WebDriverWait(browser,15)#10秒内每隔500毫秒扫描1次页面变化，等待审批页面加载成功    
        dr.until(lambda browser:browser.find_element_by_xpath("//span[text()='同意' or text()='提交']").is_displayed())
    except  Exception:
        print '当前结点已屏蔽'
        f.write('当前结点已屏蔽\n\n' )   
    browser=webdriver.Ie();  
    browser.get("http://122.4.80.27:8081/csrbpm/");
    try:
        dr=WebDriverWait(browser,50)#10秒内每隔500毫秒扫描1次页面变化，当出现指定的元素后结束,driver就是上面的句柄    
        dr.until(lambda the_driver:the_driver.find_element_by_xpath("//a[text()='登录']").is_displayed())
    except  Exception:
        print 'bpmPC首页加载失败' 
    pcCommonStep(browser,'admin','crrc6699') 
    handle1=browser.current_window_handle  
    pcSuperUserCommonStep(browser)
    handles = browser.window_handles # 获取当前窗口句柄集合（列表类型）
    for handle in handles:# 切换窗口（切换到搜狗）
        if handle!=handle1:
            #print 'switch to ',handle
            browser.switch_to_window(handle)
            #print handle
    browser.find_element_by_xpath("//a[@onclick='selExeUsers(this,\'UserTask2\')']").click()
    try:
        dr=WebDriverWait(browser,30)#10秒内每隔500毫秒扫描1次页面变化，当出现指定的元素后结束,driver就是上面的句柄    
        dr.until(lambda browser:browser.find_element_by_xpath("//iframe[@id='userListFrame']").is_displayed())
    except  Exception:
        print '用户选择窗口加载失败' 
    handle2=browser.current_window_handle  
    time.sleep(3)
    handles = browser.window_handles # 获取当前窗口句柄集合（列表类型）
    
        #print handles # 输出句柄集合 
    for handle in handles:# 切换窗口（切换到搜狗）
        if handle!=handle1 and handle!=handle2:
            #print 'switch to ',handle
            browser.switch_to_window(handle)
            #print handle
    browser.switch_to_frame('userListFrame')
    time.sleep(3)
    try:
        dr=WebDriverWait(browser,30)#10秒内每隔500毫秒扫描1次页面变化，当出现指定的元素后结束,driver就是上面的句柄    
        dr.until(browser.find_element_by_xpath("//input[@value='10500089680#王雪##']").is_displayed())
    except  Exception:
        print '用户列表加载失败' 
    browser.find_element_by_xpath("//input[@value='10500089680#王雪##']").click()
    browser.find_element_by_xpath("//input[@value='10500089561#矫雪巍 ##']").click()
    