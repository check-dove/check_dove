import itertools

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
import os
# 下拉框处理
from selenium.webdriver.support.select import Select

# 下载文件,设置
"""
profile.default_content_settings.popups,值为0，表示禁止弹出下载窗口
download.default_directory，设置文件下载路径
"""
# fp = webdriver.ChromeOptions()
# perfs = {'profile.default_content_settings.popups': 0
#          'download.default_directory': os.getcwd()}
# fp.add_experimental_option('perfs', perfs)
# dr = webdriver.Chrome(fp)

dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
time.sleep(1)
dr.maximize_window()

# 鼠标悬停操作
# title = dr.title
# print(title)
# element = dr.find_element_by_xpath('//*[@id="s-top-left"]/div/a')
# ActionChains(dr).move_to_element(element).perform()
# elemne = dr.find_element_by_xpath('//*[@id="s-top-more"]/div[1]/a[1]').click()
#
# # 常见浏览操作：刷新、前进、后退
# dr.set_window_size(480, 600)
# dr.back()
# time.sleep(2)
# dr.forward()
# time.sleep(2)
# dr.refresh()

# 元素属性display:none转变为display:block定位；
# 这里遇到了一个问题,已记录：问题4
# cur_window = dr.current_window_handle
# element = dr.find_element_by_xpath(
#     '//*[@id="s-usersetting-top"]').click()
# dr.find_element_by_partial_link_text("搜索设置").click()
#
# element_xpth = (By.XPATH, '//*[@id="wrapper"]/div[6]')
# try:
#     WebDriverWait(dr, 10, 0.5).until(ec.visibility_of_element_located(element_xpth))
# except:
#     print('xxxxxxxxx!')
# dr.find_element_by_xpath('//*[@id="nr_2"]').click()
# # dr.find_element_by_xpath('//*[@id="wrapper"]/div[6]/div/div/ul/li[2]').click()
# time.sleep(2)
# dr.find_element_by_partial_link_text("保存设置").click()
#
# # 弹窗处理
# alert = dr.switch_to.alert
# alert_text = alert.text
# print(alert_text)
# alert.dismiss()
# time.sleep(1)
#
# # 上传文件思路
# # 普通上传：将本地文件路径作为一个值放在input标签中，通过form表单提交给服务器
# # 插件上传：一般是基于flash\javascript、ajax等技术实现的上传功能，可以使用AutoIt来实现
#

# eachPageNum = 0
# elements = dr.find_elements_by_xpath('//*[@id="se-setting-3"]/span')
#
# for eachone in elements:
#     classname = eachone.find_element_by_tag_name('span').get_attribute('class')
#     print(classname, '\n', type(classname))
#     if 'c-radio-checked' in classname:
#         eachPageNum = eachone.find_element_by_tag_name('input').get_attribute('value')
# dr.find_element_by_partial_link_text("保存设置").click()
#
# # 弹窗处理
# alert = dr.switch_to.alert
# alert_text = alert.text
# print(alert_text)
# alert.dismiss()
# time.sleep(1)
time.sleep(1)

"""
# 百度安全验证网址，两次比较
'https://wappass.baidu.com/static/captcha/tuxing.html?&' \
'logid=12085484428622177881&' \
'ak=c27bbc89afca0463650ac9bde68ebe06&' \
'backurl=https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D1%26rsv_idx%3D1%26tn%3Dbaidu%26wd%3Dselenium%26fenlei%3D256%26rsv_pq%3Da9e948e000088e37%26rsv_t%3Dd93aTCio3NcAMyW9sjlUywt83TlQrqgPkNKd0j9pOYI6%252BT5YrQBUejr9Jpc%26rqlang%3Dcn%26rsv_enter%3D0%26rsv_dl%3Dtb%26rsv_sug3%3D8%26rsv_btype%3Di%26inputT%3D120%26rsv_sug4%3D120%26rsv_jmp%3Dfail&' \
'signature=9c51a73d1e89f8d39b405d27db19384b&' \
'timestamp=1642561085'

"https://wappass.baidu.com/static/captcha/tuxing.html?&" \
"logid=8498932739965230319&" \
"ak=c27bbc89afca0463650ac9bde68ebe06&" \
"backurl=https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D1%26rsv_idx%3D1%26tn%3Dbaidu%26wd%3Dselenium%26fenlei%3D256%26rsv_pq%3D92b1e6620000599c%26rsv_t%3D14abx4FamexHwXxj1wYh6X4obcN01m9U7Rn3tvSVQfTq5jRICThre7%252FT5hE%26rqlang%3Dcn%26rsv_dl%3Dtb%26rsv_enter%3D0%26rsv_sug3%3D8%26rsv_btype%3Di%26inputT%3D155%26rsv_sug4%3D155%26rsv_jmp%3Dfail&" \
"signature=b0c81b815408271e852b5950d00b25fc&" \
"timestamp=1642561336"
"""

"""出现百度安全认证时，网址和参数ak、backurl固定，
另外logid、signature、timestamp为随机数(大概率)、时间戳"""

""" 目前安全验证方式记录：
    百度安全：拖动滑块使图片为正
    12306 ：
          ：数字、文字按照给定顺序点击
          ：数字、字母识别，输入验证
          ：按文字提示，选(点击)含有该提示内容的方块——并且点击分两种，一种一次点一个(分几次，每次会刷新)，一种一次全点
"""

dr.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
dr.find_element_by_xpath('//*[@id="su"]').click()
windowsize = dr.get_window_size()
print(windowsize)
# js = "var q=document.documentElement.scrollTop=800;"
# # js = "Window.scrollTo(10000,document.body.scrollHeight);"
# # js = "$window.scrollTo(1477, 440);" # .format(int(windowsize['height'])/int(eachPageNum) * 5)
# dr.execute_script(js)

time.sleep(10)

"""
    问题：dom的xml解析和etree对xml解析的区别？
    回答：
"""

# dr.quit()

