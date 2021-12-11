from selenium import webdriver

if __name__ == '__main__':
    dr = webdriver.Chrome()
    dr.implicitly_wait(2)

    dr.get('https://www.baidu.com/')
    dr.find_element_by_id('kw').send_keys('python list')
    dr.find_element_by_id('su').click()
    dr.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div[3]/div[1]/h3/a').click()