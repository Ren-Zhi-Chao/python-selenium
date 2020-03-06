from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlrd
from util.ConfigParser import ConfigParser
import re, os
import time

config = ConfigParser()

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def OpenBrowser(driver, **uris):
    uri = uris['value']
    if not regex.match(uri):
        print(' * 输入的地址不正确.')
        return False
    driver.get(uri)
    driver.maximize_window()
    return True
def ResizeBrowser(driver, **values):
    size_value = values['value']
    if (len(size_value) == 0 or size_value.lower() == 'default'):
        return True
    if size_value.lower() == 'max':
        driver.maximize_window()
        return True
    indexs = [m.start() for m in re.finditer('x', size_value)]
    if len(indexs) == 1:
        index = indexs[0]
        width = size_value[0:index]
        height = size_value[index + 1:]
        driver.set_window_size(width, height)
    print(' * 尺寸设置格式不正确...')
    return False
def BackBrowser(driver, **value):
    driver.back()
    return True
def ForwardBrowser(driver, **value):
    driver.forward()
    return True
def RefreshBrowser(driver, **value):
    driver.refresh()
    return True
def CloseBrowser(driver, **value):
    driver.close()
    return True
def QuitBrowser(driver, **value):
    driver.quit()
    return True

BROWSER_OPETION = {
    "open": OpenBrowser,
    "resize": ResizeBrowser,
    "back": BackBrowser,
    "forward": ForwardBrowser,
    "refresh": RefreshBrowser,
    "close": CloseBrowser,
    "quit": QuitBrowser
}

def WaitBrowser(driver, **seconds):
    second = seconds['value']
    if not second:
        second = 1
    second = float(second)
    time.sleep(second)
    return True
OTHER_OPETION = {
    "wait": WaitBrowser
}

def ClearFun(obj, **value):
    obj.clear()

def SetFun(obj, **value):
    obj.send_keys(value['value'])

def ClearSetFun(obj, **value):
    obj.clear()
    obj.send_keys(value['value'])

def ClickFun(obj, **value):
    obj.click()

def DbClickFun(obj, **value):
    obj.click()
    obj.click()

SELETOR_FUN = {
    'clear': ClearFun,
    'set': SetFun,
    'clear&set': ClearSetFun,
    'click': ClickFun,
    'dbClick': DbClickFun
}

BY_TYPE = {
    'id': By.ID,
    'class': By.CLASS_NAME,
    'name': By.NAME,
    'tag': By.TAG_NAME,
    'xpath': By.XPATH
}

def SeletorFun(driver, **args):
    value = args['value']
    optn = args['optn']
    express = args['express']
    seletor = args['seletor']
    wait_time = args['wait_time']
    frequency = config.WinFrequency()
    if len(express.strip()) == 0:
        print(' * 请输入正确表达式，否则无法定位标签. ')
        return False
    obj = None
    if wait_time:
        obj = WebDriverWait(driver, wait_time, frequency).until(
                      EC.presence_of_element_located((BY_TYPE[seletor], express))
                      )
    else:
        if 'id' == seletor:
            obj = driver.find_element_by_id(express)
        elif 'class' == seletor:
            obj = driver.find_element_by_class_name(express)
        elif 'name' == seletor:
            obj = driver.find_element_by_name(express)
        elif 'tag' == seletor:
            obj = driver.find_element_by_tag_name(express)
        elif 'xpath' == seletor:
            obj = driver.find_element_by_xpath(express)
    SELETOR_FUN[optn](obj, value = value)

ELEMENT_OPETION = {
    "id": SeletorFun,
    "class": SeletorFun,
    "name": SeletorFun,
    "tag": SeletorFun,
    "xpath": SeletorFun
}

class MyWebDrive:
    def GetDrive(this, type):
        functionName = "%sBuilder"%type.capitalize()
        method = getattr(this, functionName)
        driver = method()
        i_time = config.WinImplicitly()
        if i_time:
            # 设置隐式等待
            print(' => 开启隐式等待. 等待时间: ', i_time)
            driver.implicitly_wait(int(i_time))
        ResizeBrowser(driver, value = config.WinSize())
        return driver
    def ChromeBuilder(this):
        plugs_file = config.PlugsFile()
        options = None
        if plugs_file:
            if not os.path.exists(plugs_file):
                print('插件[%d]不存在!'%plugs_file)
            else:
                options = webdriver.ChromeOptions()
                options.add_extension(plugs_file)
                time.sleep(2)
        return webdriver.Chrome(chrome_options = options)
    def FirefoxBuilder(this):
        return webdriver.Firefox()
    def IeBuilder(this):
        return webdriver.Ie()
    def EdgeBuilder(this):
        return webdriver.Edge()
    def OperaBuilder(this):
        return webdriver.Opera()
    def PhantomJSBuilder(this):
        return webdriver.PhantomJS()