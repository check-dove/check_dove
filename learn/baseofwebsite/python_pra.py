from selenium import webdriver
# from selenium.common import exceptions
from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
from time import sleep, strftime

searchpo = '火车票'
website = "https://www.python.org"

dr = webdriver.Chrome()
dr.implicitly_wait(10)
dr.get(website)


class BaiduSearch(object):
    def __init__(self, searchpo):
        self.website = "www.baidu.com"
        self.searchpo = searchpo

    def searchsomething(self):
        dr.maximize_window()
        sleep(1)
        self.element = dr.find_element_by_id('kw')
        self.element.send_keys(self.searchpo)
        dr.find_element_by_id('su').click()

    def end_step(self):
        sleep(2)
        dr.close()


class connenthandle(BaiduSearch):
    def handle(self):
        pass

    def cookieshandle(self):
        cookies = dr.get_cookies()
        # cookie = self.dr.get_cookie()
        for i in cookies:
            print(i)

    def openmorewindows(self):
        js = "window.open('https://www.sogou.com');"
        dr.execute_script(js)
        sleep(2)
        js1 = "window.open('https://www.google.com');"
        dr.execute_script(js1)


def downslip(self):
    # java脚本的执行方式，后面学习一下
    # js = "var q=document.documentElement.scrollTop=10000"
    # js = "Window.scrollTo(10000,document.body.scrollHeight)"
    # self.dr.execute_script(js)

    # 这种方式不通用，换一个页面需要重新取值xpath
    ac = dr.find_element_by_xpath("//*[@id='rs_new']")
    ActionChains(dr).move_to_element(ac).perform()


def clictopr():
    pass


def screenshot():
    '''屏幕截图'''
    dr.save_screenshot("{}.png".format(
        strftime("%H-%M-%S")))


def registration_1():
    # 出错
    dr = webdriver.Chrome()
    dr.get(website)

    sleep(2)
    js1 = "document.title='xxxxxxx’;"
    dr.execute_script(js1)

    sleep(2)
    js2 = r"alert($(document).attr('title'));"
    dr.execute_script(js2)

    sleep(5)
    dr.quit()



dr.find_element_by_id('id-search-field').send_keys('pycon')
dr.find_element_by_id('submit').click()



dr.close()
