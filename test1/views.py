#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from commonFunc import *
from comSeleFunc import *
from selenium import webdriver
try:
    from django.utils import simplejson as json
except:
    import simplejson as json
# Create your views here.
def index(request):
    return render_to_response('index.html')

def test1(request):
    shieldSteps=['会计报销']
    lastStep='会计报销'
    flowNum=request.GET['flowNum']
    output = open('testreport/test'+flowNum+'.txt', 'w')
    browser = webdriver.Chrome()
    browser.get("http://localhost/mobile-ios/cordova/www/")
    waitAndFindElement(browser, By.NAME, "title")  # 加载bpm首页
    while True:
        curStep,curUser= getUserAccount(browser)
        if curStep not in shieldSteps:
            toMobilePedingList(browser, curUser, "1")
            output.write('当前任务结点：')
            output.write(curStep + '\t')
            output.write('当前执行人：')
            output.write(curUser + '\t')
            returnMark=normalStep(browser, output)
            if not returnMark:
                browser.quit()
                break
            waitAndFindElement(browser, By.XPATH, "//div[contains(@id,'ext-menubutton')]")  # 回到待办列表
            browser.find_element_by_xpath("//div[contains(@id,'ext-menubutton')]").click()
            waitAndFindElement(browser, By.XPATH, "//span[text()='切换用户']")  # 点击切换用户
            browser.find_element_by_xpath("//span[text()='切换用户']").click()
            waitElementDisplay(browser,(By.XPATH, "//*[text()='提交']"))
            waitAndFindElement(browser, By.XPATH, "//*[text()='提交']")  # 点击切换用户
        else:
            output.write('当前任务结点：')
            output.write(curStep + '\t')
            output.write('当前执行人：')
            output.write(curUser + '\t')
            returnMark =shieldStep(browser,curUser,"1",output)
            if not returnMark:
                browser.quit()
                break
        output.write('\n')
        if curStep==lastStep:
            browser.quit()
            break
    tmpresult = {"result": '测试完成'}
    callback = request.GET['callback']
    return HttpResponse('%s(%s)' % (callback, json.dumps(tmpresult)))