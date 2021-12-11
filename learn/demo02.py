from selenium import webdriver
from time import sleep


def _init_step():
    dr = webdriver.Chrome()
    dr.get("http://www.baidu.com")
    dr.maximize_window()
    sleep(1)
    element = dr.find_element_by_id('kw')
    return dr, element


def _end_step():
    sleep(2)
    dr.close()


dr, element = _init_step()
element.send_keys('智行火车票')
elements = dr.find_element_by_id('su').click()
print(type(element))

_end_step()




