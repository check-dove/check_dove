from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver import ActionChains
from time import sleep, localtime, strftime

searchpo = '火车票'
website = "http://www.baidu.com"


class BaiduSearch(object):
    def __init__(self, website, searchpo):
        self.website = website
        self.searchpo = searchpo

        self.dr = webdriver.Chrome()
        self.dr.get(self.website)
        self.dr.maximize_window()
        sleep(1)
        self.element = self.dr.find_element_by_id('kw')
        self.element.send_keys(self.searchpo)
        self.dr.find_element_by_id('su').click()

    def end_step(self):
        sleep(2)
        self.dr.close()


class connenthandle(BaiduSearch):
    def handle(self):
        pass

    def cookieshandle(self):
        cookies = self.dr.get_cookies()
        # cookie = self.dr.get_cookie()
        for i in cookies:
            print(i)

    def openmorewindows(self):
        js = "window.open('https://www.sogou.com');"
        self.dr.execute_script(js)
        sleep(2)
        js1 = "window.open('https://www.google.com');"
        self.dr.execute_script(js1)


class operate(BaiduSearch):
    def downslip(self):
        # java脚本的执行方式，后面学习一下
        # js = "var q=document.documentElement.scrollTop=10000"
        # js = "Window.scrollTo(10000,document.body.scrollHeight)"
        # self.dr.execute_script(js)

        # 这种方式不通用，换一个页面需要重新取值xpath
        ac = self.dr.find_element_by_xpath("//*[@id='rs_new']")
        ActionChains(self.dr).move_to_element(ac).perform()

    def clictopr(self):
        pass

    def screenshot(self):
        '''屏幕截图'''
        self.dr.save_screenshot("{}.png".format(
            strftime("%H-%M-%S")))

    def registration_1(self):
        # 这种方式为什么能找到，不能点击(多重筛选试过了)---找到的是什么
        elment = self.dr.find_elements_by_tag_name('div')
        print(type(elment))
        for eachone in elment:
            tplsss = eachone.get_attribute('id')
            print(tplsss)
            if tplsss == '1':
                subscript = elment.index(eachone)
                print('this')
                break
        elment[subscript].click()

    def mod_registration1(self):
        element = self.dr.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()

    def registration_2(self):
        self.dr.find_element_by_link_text('中国铁路').click()
        # self.dr.find_element_by_xpath('//*[@id="4"]/h3/a').click()
        # self.dr.find_element_by_css_selector("#\34>h3>a").click()
        # ("html>body>div#wrapper>div#wrapper_wrapper>"
        # "div#container>div#content_left>div#4> h3 > a")


try:
    test1 = operate(website, searchpo)
    # test2 = connenthandle(website, searchpo)
    # test2.cookieshandle()
    # test2.openmorewindows()
    sleep(5)
    test1.registration_1()
    sleep(10)
    # test1.screenshot()
finally:
    test1.end_step()
